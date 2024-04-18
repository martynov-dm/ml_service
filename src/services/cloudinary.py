import cloudinary
import cloudinary.uploader
from io import BytesIO

import cloudinary

from src.config import CLOUDINARY_SECRET
          
cloudinary.config( 
  cloud_name = "martynov-dm", 
  api_key = "742326812825276", 
  api_secret = CLOUDINARY_SECRET
)

def upload_image(image_bytes):
    try:
        print("Uploading image to Cloudinary...")

        # Upload the image to Cloudinary
        upload_result = cloudinary.uploader.upload(
            image_bytes,
            folder="generated_images",
            public_id=None,
            overwrite=True,
            resource_type="image"
        )

        # Get the URL of the uploaded image
        image_url = upload_result['url']
        return image_url

    except cloudinary.exceptions.Error as e:
        print(f"Error uploading image to Cloudinary: {str(e)}")
        return None

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return None