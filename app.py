import os
from PIL import Image

def create_silhouette(input_path, output_path):
    # Open the image
    img = Image.open(input_path).convert("RGBA")
    
    # Create a new image for the silhouette
    silhouette = Image.new("RGBA", img.size, (0, 0, 0, 0))
    width, height = img.size
    
    # Process each pixel
    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            if a > 0:  # If the pixel is not fully transparent
                silhouette.putpixel((x, y), (0, 0, 0, a))
            else:
                silhouette.putpixel((x, y), (255, 255, 255, 255)) # Set to white
    
    # Save the silhouette image
    silhouette.save(output_path, "PNG")
    print(f"Silhouette saved to {output_path}")

def process_directory(dir):
    # Supported image file extensions
    valid_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".tiff"}
    
    for filename in os.listdir(dir):
        # Check file extension
        if any(filename.lower().endswith(ext) for ext in valid_extensions):
            name, ext = filename.rsplit(".", 1)
            new_filename = f"{name}_silhouette.{ext}"
            try:
                create_silhouette(os.path.join(dir, filename), os.path.join(dir, new_filename))
            except Exception as e:
                print(f"Failed to process : {e}")

input_directory = "images"  # Replace with your input images directory path
process_directory(input_directory)
