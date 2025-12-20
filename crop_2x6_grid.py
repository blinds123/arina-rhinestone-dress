#!/usr/bin/env python3
"""
Crop 2×6 grid collage into 12 individual testimonial images.
"""

import cv2
from pathlib import Path

def crop_2x6_grid(input_path, output_dir, start_num=10):
    """
    Crop a 2×6 grid collage (2 columns, 6 rows) into individual images.

    Args:
        input_path: Path to the collage image
        output_dir: Directory to save cropped images
        start_num: Starting number for output files (default: 10)
    """
    # Load image
    image = cv2.imread(str(input_path))
    if image is None:
        raise ValueError(f"Could not load image: {input_path}")

    height, width = image.shape[:2]
    print(f"Image dimensions: {width}x{height}")

    # Calculate grid dimensions
    cols = 2
    rows = 6

    col_width = width // cols
    row_height = height // rows

    print(f"Grid: {cols} columns × {rows} rows")
    print(f"Each cell: {col_width}x{row_height} pixels\n")

    # Create output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Crop each image in the grid
    image_count = start_num
    for row_idx in range(rows):
        for col_idx in range(cols):
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

            print(f"✓ Saved testimonial_{image_count:02d}.png ({cropped.shape[1]}x{cropped.shape[0]})")
            image_count += 1

    print(f"\n✅ Successfully cropped {image_count - start_num} testimonial images!")
    print(f"📁 Saved to: {output_dir}")

if __name__ == "__main__":
    # Paths
    input_image = "/Users/nelsonchan/Downloads/arina Rhinestone Dress/collage-2x6.png"
    output_directory = "/Users/nelsonchan/Downloads/arina Rhinestone Dress/images/testimonials"

    # Crop the testimonials (start at 10 since we already have 01-09)
    crop_2x6_grid(input_image, output_directory, start_num=10)
