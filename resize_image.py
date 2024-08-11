from PIL import Image
import os


def resize_image(image_path, output_path, size=(100, 100)):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        img.save(output_path, quality=85)

# Directory where your images are stored
image_dir = 'images/'

# Output directory for resized images
output_dir = 'resized_images/'
os.makedirs(output_dir, exist_ok=True)

# Resize all images in the directory
for image_file in os.listdir(image_dir):
    if image_file.endswith(('png', 'jpg', 'jpeg')):
        input_path = os.path.join(image_dir, image_file)
        output_path = os.path.join(output_dir, image_file)
        resize_image(input_path, output_path)

print("Image resizing complete.")
