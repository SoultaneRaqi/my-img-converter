from PIL import Image
from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "images-to-convert"
OUTPUT_DIR = BASE_DIR / "converted-images"

# Supported image formats
SUPPORTED_FORMATS = {
    ".png", ".jpg", ".jpeg", ".bmp", ".tiff"
}

def convert_images():
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

    images = [
        file for file in INPUT_DIR.iterdir()
        if file.is_file() and file.suffix.lower() in SUPPORTED_FORMATS
    ]

    if not images:
        print("No images found in images-to-convert/")
        return

    print(f"Found {len(images)} images. Starting conversion...\n")

    successful = 0
    failed = 0

    for index, image_path in enumerate(images, start=1):
        output_path = OUTPUT_DIR / f"{image_path.stem}.webp"

        try:
            with Image.open(image_path) as img:
                img.save(
                    output_path,
                    "WEBP",
                    lossless=True,
                    method=6
                )

            print(f"[{index}/{len(images)}] OK: {image_path.name}")
            successful += 1

        except Exception as error:
            print(f"[{index}/{len(images)}] FAILED: {image_path.name} - {error}")
            failed += 1

    print("\n========== RESULTS ==========")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Output: {OUTPUT_DIR}")

if __name__ == "__main__":
    convert_images()
