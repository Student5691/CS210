import os
from PIL import Image

# Directory containing the images
input_dir = r"G:\My Drive\School\01_Fall2024\CS210\Project1\images\working\newImgs"  # Replace with your directory path
output_dir = r"G:\My Drive\School\01_Fall2024\CS210\Project1\images\working\croppedImgs"    # Replace with your desired output directory

# # Ensure the output directory exists
# os.makedirs(output_dir, exist_ok=True)

# Iterate through all files in the directory
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):
        # Construct full file path
        img_path = os.path.join(input_dir, filename)
        
        # Open the image
        with Image.open(img_path) as img:
            # Define the cropping box (left, upper, right, lower)
            # Crop the top 30 pixels
            cropped_img = img.crop((0, 50, img.width, img.height))
            
            # Save the cropped image to the output directory
            cropped_img.save(os.path.join(output_dir, filename))

print("Cropping complete!")
