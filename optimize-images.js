const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

async function optimizeImages() {
  console.log('🎨 Starting image optimization...\n');

  // Optimize product images: 400, 600, 800, 1200px widths
  console.log('📦 Processing product images...');
  const productImages = fs.readdirSync('./images/product/')
    .filter(f => f.match(/\.(jpg|jpeg|png)$/i));

  let productCount = 0;
  for (const img of productImages) {
    const baseName = path.parse(img).name;
    const input = `./images/product/${img}`;

    // Generate multiple sizes and formats
    const sizes = [400, 600, 800, 1200];
    for (const width of sizes) {
      // AVIF (best compression)
      await sharp(input)
        .resize(width)
        .avif({ quality: 85 })
        .toFile(`./images/product/${baseName}-${width}.avif`);

      // WebP (good compression)
      await sharp(input)
        .resize(width)
        .webp({ quality: 85 })
        .toFile(`./images/product/${baseName}-${width}.webp`);

      // JPG (fallback)
      await sharp(input)
        .resize(width)
        .jpeg({ quality: 85 })
        .toFile(`./images/product/${baseName}-${width}.jpg`);
    }
    productCount++;
    console.log(`  ✓ Optimized ${img} (${productCount}/${productImages.length})`);
  }

  // Optimize testimonial images: 200, 400, 600px widths
  console.log('\n👥 Processing testimonial images...');
  const testimonialImages = fs.readdirSync('./images/testimonials/')
    .filter(f => f.match(/\.(jpg|jpeg|png)$/i));

  let testimonialCount = 0;
  for (const img of testimonialImages) {
    const baseName = path.parse(img).name;
    const input = `./images/testimonials/${img}`;

    const sizes = [200, 400, 600];
    for (const width of sizes) {
      // AVIF (best compression)
      await sharp(input)
        .resize(width)
        .avif({ quality: 85 })
        .toFile(`./images/testimonials/${baseName}-${width}.avif`);

      // WebP (good compression)
      await sharp(input)
        .resize(width)
        .webp({ quality: 85 })
        .toFile(`./images/testimonials/${baseName}-${width}.webp`);

      // JPG (fallback)
      await sharp(input)
        .resize(width)
        .jpeg({ quality: 85 })
        .toFile(`./images/testimonials/${baseName}-${width}.jpg`);
    }
    testimonialCount++;
    console.log(`  ✓ Optimized ${img} (${testimonialCount}/${testimonialImages.length})`);
  }

  console.log('\n✅ All images optimized!');
  console.log(`\n📊 Summary:`);
  console.log(`  • Product images: ${productCount} originals → ${productCount * 4 * 3} optimized files`);
  console.log(`  • Testimonial images: ${testimonialCount} originals → ${testimonialCount * 3 * 3} optimized files`);
  console.log(`  • Total optimized files: ${(productCount * 4 * 3) + (testimonialCount * 3 * 3)}`);
}

optimizeImages().catch(err => {
  console.error('❌ Error optimizing images:', err);
  process.exit(1);
});
