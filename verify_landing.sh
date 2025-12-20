#!/bin/bash
echo "=== LANDING PAGE VERIFICATION ==="
echo ""
echo "✓ Product Name:"
grep -m 1 "Navy Blue Rhinestone Bodycon Mini Dress" index.html && echo "  FOUND" || echo "  MISSING"
echo ""
echo "✓ Navy Blue Color (#1B3A8C):"
grep -c "#1B3A8C" index.html
echo ""
echo "✓ Product Images Array:"
grep -c "prodsneaker12341" index.html
echo ""
echo "✓ Testimonials JSON:"
grep -c '"name": "Emma K."' index.html
echo ""
echo "✓ Featured Reviews JSON:"
grep -c '"name": "Olivia R."' index.html
echo ""
echo "✓ Order Bump - Gen Z Hook:"
grep -c "girl don't walk in half ready" index.html
echo ""
echo "✓ Order Bump Images (item1, item2, item3):"
grep -c "order-bump/item" index.html
echo ""
echo "✓ Pricing - Order Today ($59):"
grep -c '>59<\|>\$59<' index.html
echo ""
echo "✓ Pricing - Pre-order ($19):"
grep -c '>19<\|>\$19<' index.html
echo ""
echo "✓ Checkout Endpoint (/buy-now):"
grep -c "/buy-now" index.html
echo ""
echo "✓ Remaining Placeholders (should be 0):"
grep -o '{{[A-Z_]*}}' index.html | sort | uniq | wc -l
echo ""
