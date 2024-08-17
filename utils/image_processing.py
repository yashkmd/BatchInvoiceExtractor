from PIL import Image

def get_image_bytes(image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        image_info = [
            {
                "mime_type": "image/jpeg",  # Adjust this if your image is not JPEG
                "data": image_bytes
            }
        ]
        return image_info