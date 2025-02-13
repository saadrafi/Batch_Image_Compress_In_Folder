import os
from PIL import Image

output_folder = "compressed_images"
type = "webp"

# Function to compress a single image
def compress_image(input_path, output_path, type=type, quality=85):
    with Image.open(input_path) as img:
        img.save(f"{output_path}.{type}", type, quality=quality)

# Function to compress all images in a given folder
def compress_images_in_folder(folder_name, output_folder=output_folder, type=type, quality=85):

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_name):
        print()
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', 'webp')):
            # Get the file name without the extension
            file_name = filename.split(".")[0]
            
            # Construct the full input and output paths
            input_path = os.path.join(folder_name, filename)
            output_path = os.path.join(output_folder, file_name)
            
            # Compress and save the image
            compress_image(input_path, output_path, type=type, quality=quality)
            print(f"Compressed {filename} and saved to {output_path}.{type}")

# Prompt the user to enter the folder path containing images to compress
folder_name = input("Enter the folder path containing images to compress: ")

# Compress images in the specified folder
compress_images_in_folder(folder_name)