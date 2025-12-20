#!/usr/bin/env python3
"""
Generate 11 additional testimonial images using Pollinations AI.
Creates realistic customer testimonial photos for navy blue rhinestone dress.
"""

import subprocess
import os
from pathlib import Path

# Output directory
output_dir = Path("/Users/nelsonchan/Downloads/arina Rhinestone Dress/images/testimonials")
output_dir.mkdir(parents=True, exist_ok=True)

# Base prompt for testimonial images
base_scenarios = [
    "woman wearing navy blue rhinestone bodycon mini dress with gold accents at nightclub, mirror selfie, smartphone photo quality, natural lighting",
    "woman in sparkling navy blue dress with crystals at rooftop bar, city skyline background, golden hour, iPhone photo",
    "woman wearing glittery navy dress at wedding reception, dancing, candid moment, smartphone camera",
    "woman in navy rhinestone dress getting ready in hotel room, full length mirror selfie, excited expression",
    "woman wearing sparkly blue dress at birthday party, holding champagne glass, friends in background, casual photo",
    "woman in navy bodycon dress with gold rhinestones at dinner date, restaurant setting, warm ambient lighting",
    "woman wearing crystal embellished navy dress on vacation, beach resort background, sunset lighting",
    "woman in shimmering navy dress at girls night out, group selfie angle, club lighting",
    "woman wearing navy rhinestone mini dress at concert, festival lights, energetic vibe, smartphone quality",
    "woman in sparkly navy dress trying it on in boutique dressing room, fitting room mirror, fluorescent lighting",
    "woman wearing navy blue crystal dress at New Years Eve party, confetti in air, celebration moment, phone camera"
]

print("🎨 Generating 11 additional testimonial images using Pollinations AI...")
print("=" * 70)

# Count existing testimonials
existing = len([f for f in output_dir.glob("testimonial_*.png")])
print(f"📊 Existing testimonials: {existing}")
print(f"🎯 Target total: 20 testimonials")
print(f"➕ Generating: 11 new images\n")

# Generate 11 new testimonial images
for i, scenario in enumerate(base_scenarios, start=existing + 1):
    image_num = i
    output_file = output_dir / f"testimonial_{image_num:02d}.png"

    # URL-encode the prompt
    encoded_prompt = scenario.replace(" ", "%20").replace(",", "%2C")

    # Pollinations AI URL
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=600&height=800&nologo=true&model=flux"

    print(f"[{image_num}/20] Generating testimonial {image_num:02d}...")
    print(f"    Scenario: {scenario[:60]}...")

    # Download image using curl
    try:
        result = subprocess.run(
            ["curl", "-L", "-s", "-o", str(output_file), url],
            capture_output=True,
            timeout=30
        )

        # Verify file was created and is valid size
        if output_file.exists() and output_file.stat().st_size > 10000:
            file_size_kb = output_file.stat().st_size / 1024
            print(f"    ✅ Generated successfully ({file_size_kb:.1f} KB)\n")
        else:
            print(f"    ⚠️  Failed - retrying...\n")
            # Retry once
            subprocess.run(
                ["curl", "-L", "-s", "-o", str(output_file), url],
                timeout=30
            )
    except Exception as e:
        print(f"    ❌ Error: {e}\n")
        continue

# Final count
final_count = len([f for f in output_dir.glob("testimonial_*.png")])
print("=" * 70)
print(f"✅ Complete! Total testimonial images: {final_count}/20")
print(f"📁 Location: {output_dir}")

if final_count >= 20:
    print("\n🎉 SUCCESS: 20 testimonial images ready for landing page!")
else:
    print(f"\n⚠️  WARNING: Only {final_count} images generated. Expected 20.")
