# 🖼️ My Image Converter

A lightweight Python batch image converter that automatically converts multiple images into **lossless WebP format**.

Simply drop your images into the input folder, run the script, and find your converted images in the output folder.

## ✨ Features

- **Batch conversion:** Convert multiple images in one execution.
- **Lossless WebP:** Preserve original pixel quality.
- **Multiple formats:** Supports PNG, JPG, JPEG, BMP, and TIFF.
- **Automatic directories:** Creates input and output folders if they don't exist.
- **Progress tracking:** Displays conversion progress in the terminal.
- **Error handling:** Reports failed conversions without stopping the entire process.
- **File organization:** Keeps original filenames with the `.webp` extension.

## 📁 Project Structure

```text
my-img-converter/
│
├── images-to-convert/       # Input images
├── converted-images/        # Converted WebP images
│
├── .venv/                   # Python virtual environment
├── convert.py               # Main conversion script
├── requirements.txt         # Python dependencies
├── README.md
└── .gitignore