#!/usr/bin/env python3
import json
import os

# Load all JSON data
with open('color-system.json') as f:
    color_data = json.load(f)

with open('order-bump-bundle.json') as f:
    bundle_data = json.load(f)

with open('testimonials.json') as f:
    testimonials_data = json.load(f)

with open('product-info.json') as f:
    product_data = json.load(f)

# Read template
with open('template.html') as f:
    html = f.read()

# Product images
product_images = [
    "prodsneaker12341 (12).jpg",
    "prodsneaker12341 (13).jpg",
    "prodsneaker12341 (14).jpg",
    "prodsneaker12341 (15).jpg",
    "prodsneaker12341 (16).jpg",
    "prodsneaker12341 (17).jpg",
    "prodsneaker12341 (7).jpg"
]

# Build product images JSON array
product_images_json = json.dumps(product_images)

# Build testimonials JSON
testimonials_json = json.dumps(testimonials_data['testimonials'])
featured_reviews_json = json.dumps(testimonials_data['featured_reviews'])

# Build product description HTML
product_description_html = '\n'.join([
    f'<p style="margin-bottom: 20px; line-height: 1.8; color: #333;">{p}</p>'
    for p in product_data['product_description']['paragraphs']
])

# Build FAQ HTML
faq_html = ''
for faq in product_data['faq_section']:
    faq_html += f'''
    <div style="margin-bottom: 20px;">
      <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 8px; color: #1a1a1a;">{faq['question']}</h3>
      <p style="color: #666; line-height: 1.7;">{faq['answer']}</p>
    </div>
'''

# Build order bump features HTML
order_bump_features = f'''
<li style="margin-bottom:8px;display:flex;align-items:center;gap:8px">
  <svg width="16" height="16" viewBox="0 0 20 20" fill="none"><path d="M7 10L9 12L13 8M19 10C19 14.9706 14.9706 19 10 19C5.02944 19 1 14.9706 1 10C1 5.02944 5.02944 1 10 1C14.9706 1 19 5.02944 19 10Z" stroke="#28a745" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <span>{bundle_data['bundle']['item1']['feature']}</span>
</li>
<li style="margin-bottom:8px;display:flex;align-items:center;gap:8px">
  <svg width="16" height="16" viewBox="0 0 20 20" fill="none"><path d="M7 10L9 12L13 8M19 10C19 14.9706 14.9706 19 10 19C5.02944 19 1 14.9706 1 10C1 5.02944 5.02944 1 10 1C14.9706 1 19 5.02944 19 10Z" stroke="#28a745" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <span>{bundle_data['bundle']['item2']['feature']}</span>
</li>
<li style="margin-bottom:8px;display:flex;align-items:center;gap:8px">
  <svg width="16" height="16" viewBox="0 0 20 20" fill="none"><path d="M7 10L9 12L13 8M19 10C19 14.9706 14.9706 19 10 19C5.02944 19 1 14.9706 1 10C1 5.02944 5.02944 1 10 1C14.9706 1 19 5.02944 19 10Z" stroke="#28a745" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <span>{bundle_data['bundle']['item3']['feature']}</span>
</li>
'''

# All replacements
replacements = {
    # Product
    '{{PRODUCT_NAME}}': 'Navy Blue Rhinestone Bodycon Mini Dress',
    '{{PRODUCT_TAGLINE}}': 'Be Unforgettable in Navy Blue Sparkle',
    '{{PRODUCT_TYPE}}': 'bodycon mini dress',
    '{{PRODUCT_COLOR_NAME}}': 'Navy Blue with Gold Rhinestones',
    '{{PRODUCT_COLOR_NAME_LOWER}}': 'navy blue',
    '{{PRODUCT_COLOR_DESCRIPTION}}': 'rich navy blue with luxurious gold rhinestone accents',
    '{{MATERIAL}}': 'rhinestone-embellished stretch fabric',
    '{{SITE_NAME}}': 'navyrhinestone',
    '{{PRODUCT_SLUG}}': 'navy-rhinestone-dress',
    '{{SITE_URL}}': 'https://navyrhinestone.com',

    # Pricing
    '{{PRICE_ORDER}}': '59',
    '{{PRICE_PREORDER}}': '19',
    '{{PRICE_BUMP}}': '10',
    '{{PRICE_ORIGINAL}}': '129',
    '{{DISCOUNT_PERCENT}}': '54% OFF',

    # Colors
    '{{COLOR_PRIMARY}}': '#1B3A8C',
    '{{COLOR_PRIMARY_LIGHT}}': '#2E52B8',
    '{{COLOR_PRIMARY_LIGHTER}}': '#5B7DD4',
    '{{COLOR_PRIMARY_DARK}}': '#15307A',
    '{{COLOR_PRIMARY_DARKER}}': '#0F2564',
    '{{COLOR_PRIMARY_DARKEST}}': '#0A1A4B',
    '{{COLOR_SECONDARY}}': '#D4A04C',
    '{{COLOR_ACCENT}}': '#F0C674',
    '{{COLOR_PRIMARY_RGB}}': '27,58,140',

    # Order Bump
    '{{HOOK_HEADLINE}}': bundle_data['copy']['hook_headline'],
    '{{ITEM1_SHORT}}': bundle_data['bundle']['item1']['short_name'],
    '{{ITEM1_WHY}}': bundle_data['bundle']['item1']['why_copy'],
    '{{ITEM2_SHORT}}': bundle_data['bundle']['item2']['short_name'],
    '{{ITEM2_WHY}}': bundle_data['bundle']['item2']['why_copy'],
    '{{ITEM3_SHORT}}': bundle_data['bundle']['item3']['short_name'],
    '{{ITEM3_WHY}}': bundle_data['bundle']['item3']['why_copy'],
    '{{TOTAL_VALUE}}': '100',
    '{{CTA_TEXT}}': bundle_data['copy']['cta_text'],
    '{{DECLINE_TEXT}}': bundle_data['copy']['decline_text'],
    '{{ORDER_BUMP_NAME}}': 'Complete Party Look Bundle',
    '{{ORDER_BUMP_PRODUCT_TYPE}}': 'accessories bundle',
    '{{ORDER_BUMP_FEATURES}}': order_bump_features,

    # Product Description
    '{{PRODUCT_DESCRIPTION}}': product_description_html,

    # FAQ
    '{{FAQ_HTML}}': faq_html,

    # JSON Data
    '{{PRODUCT_IMAGES_JSON}}': product_images_json,
    '{{TESTIMONIALS_JSON}}': testimonials_json,
    '{{FEATURED_REVIEWS_JSON}}': featured_reviews_json,

    # Meta
    '{{META_TITLE}}': 'Navy Blue Rhinestone Bodycon Mini Dress - Be Unforgettable',
    '{{META_DESCRIPTION}}': 'Dazzling navy blue rhinestone bodycon mini dress with gold crystal accents. Perfect for clubs, parties & special events. 54% OFF - Only $59.',
    '{{META_DESCRIPTION_LONG}}': 'Stunning navy blue rhinestone bodycon mini dress featuring gold crystal starburst patterns. Square neckline, thigh-high slit, and body-hugging fit. Perfect for nightclubs, bachelorette parties, NYE, and special occasions.',
    '{{META_KEYWORDS}}': 'navy rhinestone dress, blue bodycon mini dress, gold crystal party dress, sparkly cocktail dress, rhinestone club dress',

    # Certification (not applicable but needs placeholder)
    '{{CERTIFICATION_DESCRIPTION}}': 'Premium quality rhinestone embellishments',

    # Testimonials for schema
    '{{TESTIMONIAL_1_TEXT}}': testimonials_data['testimonials'][0]['text'].split('.')[0],
    '{{TESTIMONIAL_2_TEXT}}': testimonials_data['testimonials'][1]['text'].split('.')[0],

    # Additional placeholders
    '{{BRAND_DESCRIPTION}}': 'Stunning navy blue rhinestone party dresses and club wear',
    '{{CERTIFICATION_BADGE}}': '<div style="display:inline-flex;align-items:center;gap:8px;background:#f8fff8;border:2px solid #28a745;border-radius:8px;padding:10px 16px;font-size:13px;font-weight:600;color:#28a745"><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M7 10L9 12L13 8M19 10C19 14.9706 14.9706 19 10 19C5.02944 19 1 14.9706 1 10C1 5.02944 5.02944 1 10 1C14.9706 1 19 5.02944 19 10Z" stroke="#28a745" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Premium Quality Rhinestones</div>',
    '{{CERTIFICATION_SHORT}}': 'Premium Quality',
    '{{FOOTER_DESCRIPTION}}': 'Your destination for stunning rhinestone party dresses and glamorous club wear. Be unforgettable in navy blue sparkle.',
    '{{SITE_DOMAIN}}': 'navyrhinestone.com',
}

# Apply all replacements
for old, new in replacements.items():
    html = html.replace(old, str(new))

# Replace hardcoded product images array
html = html.replace(
    "const productImages = ['product-01.png', 'product-02.png', 'product-03.png', 'product-04.png', 'product-05.png'];",
    f"const productImages = {product_images_json};"
)

# Create custom Gen Z order bump popup
gen_z_order_bump = f'''<!-- Order Bump Popup - Gen Z Version -->
<div id="orderBumpPopup" role="dialog" aria-modal="true" aria-labelledby="popupTitle" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);z-index:10000;align-items:center;justify-content:center;padding:20px;overflow-y:auto">
  <div style="background:#fff;border-radius:16px;max-width:650px;width:100%;padding:40px;position:relative;box-shadow:0 20px 60px rgba(0,0,0,0.3);animation:fadeIn 0.3s ease;margin:auto">
    <button onclick="closeOrderBumpPopup()" aria-label="Close popup" style="position:absolute;top:16px;right:16px;background:none;border:none;font-size:32px;cursor:pointer;color:#999;line-height:1;padding:0;display:flex;align-items:center;justify-content:center;min-width:44px;min-height:44px">&times;</button>

    <!-- Gen Z Hook -->
    <div style="text-align:center;margin-bottom:30px">
      <div style="background:#1B3A8C;color:#fff;display:inline-block;padding:8px 16px;border-radius:20px;font-size:14px;font-weight:700;margin-bottom:20px;text-transform:uppercase;letter-spacing:0.5px">WAIT!</div>
      <h2 id="popupTitle" style="font-size:32px;font-weight:700;margin-bottom:12px;color:#1a1a1a;line-height:1.2">{bundle_data['copy']['hook_headline']}</h2>
      <p style="color:#666;font-size:17px;line-height:1.6">{bundle_data['copy']['subheadline']}</p>
    </div>

    <!-- Why Section -->
    <div style="background:#fff5f7;border-radius:12px;padding:24px;margin-bottom:24px;border-left:4px solid #1B3A8C">
      <p style="font-size:15px;font-weight:700;margin-bottom:12px;color:#1a1a1a">{bundle_data['copy']['why_section']['intro']}</p>
      <ul style="list-style:none;padding:0;margin:0">
        <li style="margin-bottom:10px;padding-left:24px;position:relative;color:#333;font-size:14px;line-height:1.6">
          <span style="position:absolute;left:0;color:#dc3545;font-weight:700">✗</span>
          {bundle_data['copy']['why_section']['bullets'][0]}
        </li>
        <li style="margin-bottom:10px;padding-left:24px;position:relative;color:#333;font-size:14px;line-height:1.6">
          <span style="position:absolute;left:0;color:#dc3545;font-weight:700">✗</span>
          {bundle_data['copy']['why_section']['bullets'][1]}
        </li>
        <li style="padding-left:24px;position:relative;color:#333;font-size:14px;line-height:1.6">
          <span style="position:absolute;left:0;color:#dc3545;font-weight:700">✗</span>
          {bundle_data['copy']['why_section']['bullets'][2]}
        </li>
      </ul>
    </div>

    <!-- 3 Items Grid with Images -->
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:24px">
      <div style="text-align:center;padding:16px;background:#f8f9fa;border-radius:12px">
        <img src="./images/order-bump/item1.jpg" alt="{bundle_data['bundle']['item1']['name']}" style="width:100%;height:140px;object-fit:cover;border-radius:8px;margin-bottom:12px">
        <h4 style="font-size:13px;font-weight:700;margin-bottom:6px;color:#1a1a1a">{bundle_data['bundle']['item1']['short_name']}</h4>
        <p style="font-size:12px;color:#666;line-height:1.4">{bundle_data['bundle']['item1']['why_copy']}</p>
      </div>
      <div style="text-align:center;padding:16px;background:#f8f9fa;border-radius:12px">
        <img src="./images/order-bump/item2.jpg" alt="{bundle_data['bundle']['item2']['name']}" style="width:100%;height:140px;object-fit:cover;border-radius:8px;margin-bottom:12px">
        <h4 style="font-size:13px;font-weight:700;margin-bottom:6px;color:#1a1a1a">{bundle_data['bundle']['item2']['short_name']}</h4>
        <p style="font-size:12px;color:#666;line-height:1.4">{bundle_data['bundle']['item2']['why_copy']}</p>
      </div>
      <div style="text-align:center;padding:16px;background:#f8f9fa;border-radius:12px">
        <img src="./images/order-bump/item3.jpg" alt="{bundle_data['bundle']['item3']['name']}" style="width:100%;height:140px;object-fit:cover;border-radius:8px;margin-bottom:12px">
        <h4 style="font-size:13px;font-weight:700;margin-bottom:6px;color:#1a1a1a">{bundle_data['bundle']['item3']['short_name']}</h4>
        <p style="font-size:12px;color:#666;line-height:1.4">{bundle_data['bundle']['item3']['why_copy']}</p>
      </div>
    </div>

    <!-- Transformation Promise -->
    <div style="text-align:center;padding:20px;background:linear-gradient(135deg,#fff5f7 0%,#ffe8ed 100%);border-radius:12px;margin-bottom:24px">
      <p style="font-size:16px;font-weight:600;color:#1a1a1a;line-height:1.6;margin:0">{bundle_data['copy']['transformation_promise']}</p>
    </div>

    <!-- Value Stack -->
    <div style="background:#fff;border:2px solid #e0e0e0;border-radius:12px;padding:20px;margin-bottom:24px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
        <span style="font-size:15px;color:#666">{bundle_data['copy']['value_anchor']}</span>
        <span style="font-size:18px;color:#999;text-decoration:line-through">$100</span>
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center;padding-top:12px;border-top:2px solid #e0e0e0">
        <span style="font-size:17px;font-weight:700;color:#1a1a1a">{bundle_data['copy']['price_reveal']}</span>
        <span style="font-size:32px;font-weight:700;color:#28a745">$10</span>
      </div>
      <div style="text-align:center;margin-top:12px">
        <span style="background:#28a745;color:#fff;padding:6px 14px;border-radius:16px;font-size:13px;font-weight:700;display:inline-block">{bundle_data['copy']['savings_emphasis']}</span>
      </div>
    </div>

    <!-- Order Summary (Dynamic) -->
    <div id="orderSummary" style="background:#f8f9fa;border-radius:12px;padding:16px;margin-bottom:20px;font-size:14px">
      <!-- Populated by JavaScript -->
    </div>

    <!-- CTA Buttons -->
    <button onclick="acceptOrderBump()" style="width:100%;background:#28a745;color:#fff;border:none;padding:22px;border-radius:12px;font-size:18px;font-weight:700;cursor:pointer;margin-bottom:12px;transition:all 0.2s;min-height:70px;box-shadow:0 4px 12px rgba(40,167,69,0.3)">
      <div style="font-size:19px;margin-bottom:4px;text-transform:lowercase">{bundle_data['copy']['cta_text']}</div>
      <div style="font-size:12px;opacity:0.95;font-weight:600;text-transform:lowercase">{bundle_data['copy']['cta_benefit']}</div>
    </button>
    <button onclick="declineOrderBump()" style="width:100%;background:#fff;color:#666;border:2px solid #ddd;padding:14px;border-radius:12px;font-size:13px;font-weight:600;cursor:pointer;transition:all 0.2s;min-height:50px;text-transform:lowercase">
      {bundle_data['copy']['decline_text']}<br>
      <span style="font-size:11px;color:#999;font-style:italic">({bundle_data['copy']['decline_consequence']})</span>
    </button>
  </div>
</div>'''

# Find and replace the order bump popup section
import re
order_bump_pattern = r'<!-- Order Bump Popup -->.*?</div>\s*</div>\s*</div>'
html = re.sub(order_bump_pattern, gen_z_order_bump, html, flags=re.DOTALL)

# Save output
with open('index.html', 'w') as f:
    f.write(html)

print("✅ index.html created successfully!")

# Check for remaining placeholders
remaining = []
import re
placeholders = re.findall(r'\{\{[A-Z_]+\}\}', html)
if placeholders:
    print(f"\n⚠️  Found {len(set(placeholders))} unique remaining placeholders:")
    for p in sorted(set(placeholders)):
        print(f"   - {p}")
else:
    print("✅ All placeholders replaced!")
