from typing import Final
import requests
import os


HUGGING_FACE_TOKEN: Final = os.getenv('HUGGING_FACE_TOKEN')
MODEL_API_URL = "https://api-inference.huggingface.co/models/Melonie/text_to_image_finetuned"


def generate_image(text):
    print(HUGGING_FACE_TOKEN)
    headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}
    payload = {"inputs": text}

    response = requests.post(MODEL_API_URL, headers=headers, json=payload)

    print(response.json())
    
    # if response.status_code == 200:
    #     image_data = response.content
    #     image = Image.open(BytesIO(image_data))
    #     image_path = "generated_image.jpg"
    #     image.save(image_path)
    #     return image_path
    # else:
    #     print(f"Error generating image. Status code: {response.status_code}")
    #     return None