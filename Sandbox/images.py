"""
Images
"""
from PIL import Image

IMG_LOCATION = "Sandbox/sample_image.png"

with Image.open(IMG_LOCATION) as img:
    img = img.rotate(45)
    # Save the modified image
    img.save('Sandbox/sample_image_rotated.png')
