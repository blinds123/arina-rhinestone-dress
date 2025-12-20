#!/usr/bin/env python3
"""
Intelligent testimonial image cropper.
Analyzes white borders in the collage to detect and crop individual images.
"""

import cv2
import numpy as np
from pathlib import Path

def find_white_borders(image, threshold=150, min_border_size=5):
    """
    Find horizontal and vertical white border lines in the image.

    Args:
        image: Input image
        threshold: Pixel brightness threshold to consider as "white"
        min_border_size: Minimum consecutive white pixels to consider a border

    Returns:
        (horizontal_lines, vertical_lines): Lists of border positions
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find horizontal borders (rows that are mostly white)
    h_borders = []
    for y in range(gray.shape[0]):
        row = gray[y, :]
        if np.mean(row > threshold) > 0.7:  # 70% of row is bright
            h_borders.append(y)

    # Find vertical borders (columns that are mostly white)
    v_borders = []
    for x in range(gray.shape[1]):
        col = gray[:, x]
        if np.mean(col > threshold) > 0.7:  # 70% of column is bright
            v_borders.append(x)

    # Group consecutive border pixels into border regions
    def group_consecutive(lst, max_gap=2):
        if not lst:
            return []
        groups = []
        current_group = [lst[0]]
        for i in range(1, len(lst)):
            if lst[i] - lst[i-1] <= max_gap:
                current_group.append(lst[i])
            else:
                if len(current_group) >= min_border_size:
                    groups.append((current_group[0], current_group[-1]))
                current_group = [lst[i]]
        if len(current_group) >= min_border_size:
            groups.append((current_group[0], current_group[-1]))
        return groups

    h_border_regions = group_consecutive(h_borders)
    v_border_regions = group_consecutive(v_borders)

    # Get center of each border region
    h_lines = [(start + end) // 2 for start, end in h_border_regions]
    v_lines = [(start + end) // 2 for start, end in v_border_regions]

    return h_lines, v_lines

def crop_testimonials(input_path, output_dir):
    """
    Crop testimonial images from collage.

    Args:
        input_path: Path to the collage image
        output_dir: Directory to save cropped images
    """
    # Load image
    image = cv2.imread(str(input_path))
    if image is None:
        raise ValueError(f"Could not load image: {input_path}")

    print(f"Image dimensions: {image.shape[1]}x{image.shape[0]}")

    # Find borders
    h_lines, v_lines = find_white_borders(image)

    print(f"Found {len(h_lines)} horizontal borders at: {h_lines}")
    print(f"Found {len(v_lines)} vertical borders at: {v_lines}")

    # Add image edges to the lists
    h_boundaries = [0] + h_lines + [image.shape[0]]
    v_boundaries = [0] + v_lines + [image.shape[1]]

    print(f"Horizontal boundaries: {h_boundaries}")
    print(f"Vertical boundaries: {v_boundaries}")

    # Create output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Crop each image in the grid
    image_count = 0
    for row_idx in range(len(h_boundaries) - 1):
        for col_idx in range(len(v_boundaries) - 1):
            image_count += 1

            # Skip the last image (bottom-right, #10 with Gemini logo)
            if image_count == 10:
                print(f"Skipping image #{image_count} (Gemini logo)")
                continue

            # Calculate crop boundaries
            y1 = h_boundaries[row_idx]
            y2 = h_boundaries[row_idx + 1]
            x1 = v_boundaries[col_idx]
            x2 = v_boundaries[col_idx + 1]

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
    crop_testimonials(input_image, output_directory)
