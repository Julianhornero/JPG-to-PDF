from PIL import Image
import os

def jpg_to_pdf(input_folder, output_pdf):
    # Collect all JPG files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]
    image_files.sort()  # optional: sort files by name

    if not image_files:
        print("No JPG images found in the folder.")
        return

    # Open the first image and convert to RGB (required for PDF)
    first_image = Image.open(os.path.join(input_folder, image_files[0])).convert('RGB')

    # Open the rest of the images
    image_list = []
    for img_file in image_files[1:]:
        img_path = os.path.join(input_folder, img_file)
        img = Image.open(img_path).convert('RGB')
        image_list.append(img)

    # Save all images into a single PDF file
    first_image.save(output_pdf, save_all=True, append_images=image_list)
    print(f"PDF created successfully: {output_pdf}")

# Example usage
jpg_to_pdf('path_to_jpg_folder', 'output.pdf')
