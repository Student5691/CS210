import os
from PIL import Image

# Folder containing the PNG images
folder_path = r"G:\My Drive\School\01_Fall2024\CS210\Project1\images\working\PlayerOld"
output_folder = r"G:\My Drive\School\01_Fall2024\CS210\Project1\images\players"  # You can save resized images to the same or a different folder

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):  # Process only PNG files
        img_path = os.path.join(folder_path, filename)
        
        # Open the image file
        with Image.open(img_path) as img:
            # Resize image to 150x150 pixels
            resized_img = img.resize((30, 30), Image.Resampling.LANCZOS) # 135x135 for 1920x1080, 150x150 for 2k
            
            # Save the resized image
            resized_img.save(os.path.join(output_folder, filename))

print("Resizing completed!")