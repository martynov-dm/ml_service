from dotenv import load_dotenv
import requests
import os
import io
from io import BytesIO
from src.config import HUGGING_FACE_TOKEN
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error making request to API: {str(e)}")
        return None

def generate_image(text):
    payload = {"inputs": text}
    response = query(payload)

    if response is None:
        return None

    try:
        print(f"API response status code: {response.status_code}")
        print(f"API response content type: {response.headers['Content-Type']}")

        if response.status_code == 200 and response.headers['Content-Type'] == 'application/json':
            print(f"API response JSON: {response.json()}")
        else:
            print(f"API response content: {response.content}")

        image_bytes = response.content
        
        return image_bytes
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return None