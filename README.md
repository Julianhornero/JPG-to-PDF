
# JPG-to-PDF

Simple JPG to PDF Conversion Using Pillow

---

## Overview

This project provides a straightforward Python script to convert one or multiple JPG images into a single PDF file using the [Pillow](https://python-pillow.org/) library. It is designed to be easy to use and lightweight, making it ideal for quick image-to-PDF conversions.

---

## Features

- Convert multiple JPG images into a single PDF document
- Simple and minimal dependencies (only requires Pillow)
- Easy to modify and extend for custom workflows

---

## Requirements

- Python 3.x (Recommended 3.6+)
- Pillow library

---

## Installation

1. Clone the repository:

```
git clone https://github.com/Julianhornero/JPG-to-PDF.git
cd JPG-to-PDF
```

2. Install the Pillow library:

```
pip install Pillow
```

---

## Usage

The main script (`pil.py`) contains the conversion logic.

To convert all JPG images in a folder to a single PDF, run:

```
python pil.py
```

Make sure to modify the script or provide the path to your images folder and desired output PDF filename inside the script.

---

## Example

Here is a simple example of how the conversion works in the script:

```
from PIL import Image
import os

def jpg_to_pdf(input_folder, output_pdf):
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]
    image_files.sort()

    if not image_files:
        print("No JPG images found in the folder.")
        return

    first_image = Image.open(os.path.join(input_folder, image_files)).convert('RGB')
    image_list = [Image.open(os.path.join(input_folder, f)).convert('RGB') for f in image_files[1:]]

    first_image.save(output_pdf, save_all=True, append_images=image_list)
    print(f"PDF created successfully: {output_pdf}")

# Example usage
jpg_to_pdf('path_to_your_jpg_folder', 'output.pdf')
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

