import cloudinary
import cloudinary.uploader
from io import BytesIO

# Настройка учетных данных Cloudinary
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

def upload_image(image_data):
    try:
        # Загрузка изображения на Cloudinary
        upload_result = cloudinary.uploader.upload(BytesIO(image_data), folder="generated_images")
        image_url = upload_result['url']
        return image_url
    except Exception as e:
        print(f"Error uploading image to Cloudinary: {str(e)}")
        return None