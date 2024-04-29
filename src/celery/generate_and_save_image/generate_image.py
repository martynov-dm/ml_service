import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from src.celery.celery_logger import celery_logger
from src.config import HUGGING_FACE_TOKEN, MODEL_API_URL
headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}


def query(payload, max_retries=3, backoff_factor=1, timeout=60):
    retry_strategy = Retry(
        total=max_retries,
        status_forcelist=[500],
        backoff_factor=backoff_factor
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    with requests.Session() as session:
        session.mount("https://", adapter)
        try:
            response = session.post(
                MODEL_API_URL,
                headers=headers,
                json=payload,
                timeout=timeout  # Set the timeout for the request
            )
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            return response
        except requests.exceptions.RequestException as e:
            celery_logger.error(f"Error making request to API: {str(e)}")
            return None


def generate_image(text):
    payload = {"inputs": text}
    response = query(payload)
    if response is None:
        return None
    try:
        celery_logger.info(f"API response status code: {response.status_code}")
        celery_logger.info(f"API response content type: {
            response.headers['Content-Type']}")
        if response.status_code == 200 and response.headers['Content-Type'] == 'application/json':
            celery_logger.info(f"API response JSON: {response.json()}")
        else:
            celery_logger.info("Image generated successfully")
        image_bytes = response.content
        return image_bytes
    except Exception as e:
        celery_logger.error(f"Error processing image: {str(e)}")
        return None
