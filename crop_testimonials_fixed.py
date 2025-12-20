#!/usr/bin/env python3
"""
Fixed testimonial image cropper using calculated grid positions.
For a 2x5 grid collage (2 columns, 5 rows).
"""

import cv2
import numpy as np
from pathlib import Path

def crop_testimonials_grid(input_path, output_dir):
    """
    Crop testimonial images using calculated grid positions.

    Args:
        input_path: Path to the collage image
        output_dir: Directory to save cropped images
    """
    # Load image
    image = cv2.imread(str(input_path))
    if image is None:
        raise ValueError(f"Could not load image: {input_path}")

    height, width = image.shape[:2]
    print(f"Image dimensions: {width}x{height}")

    # Calculate grid dimensions
    # 2 columns, 5 rows
    cols = 2
    rows = 5

    col_width = width // cols
    row_height = height // rows

    print(f"Grid: {cols} columns × {rows} rows")
    print(f"Each cell: {col_width}x{row_height} pixels")

    # Create output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Crop each image in the grid
    image_count = 0
    for row_idx in range(rows):
        for col_idx in range(cols):
            image_count += 1

            # Skip the last image (bottom-right, #10 with Gemini logo)
            if image_count == 10:
                print(f"Skipping image #{image_count} (Gemini logo)")
                continue

            # Calculate crop boundaries
            x1 = col_idx * col_width
            x2 = (col_idx + 1) * col_width
            y1 = row_idx * row_height
            y2 = (row_idx + 1) * row_height

            # Crop the image
            cropped = image[y1:y2, x1:x2]

            # Save the cropped image
            output_path = output_dir / f"testimonial_{image_count:02d}.png"
            cv2.imwrite(str(output_path), cropped)

            print(f"Saved image #{image_count}: {output_path} ({cropped.shape[1]}x{cropped.shape[0]})")

    print(f"\n✅ Successfully cropped {image_count - 1} testimonial images!")
    print(f"📁 Saved to: {output_dir}")

if __name__ == "__main__":
    # Paths
    input_image = "/Users/nelsonchan/Downloads/Gemini_Generated_Image_h1mc92h1mc92h1mc (1).png"
    output_directory = "/Users/nelsonchan/Downloads/arina Rhinestone Dress/images/testimonials"

    # Crop the testimonials
    crop_testimonials_grid(input_image, output_directory)
