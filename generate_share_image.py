from PIL import Image, ImageDraw, ImageFont
import os

W = H = 1024
img = Image.new('RGB', (W, H), '#000000')
draw = ImageDraw.Draw(img)

# Pure black background, no noise dots

# Decorative border
border = 48
draw.rectangle([border, border, W-border, H-border], outline='#d4a843', width=4)
draw.rectangle([border+16, border+16, W-border-16, H-border-16], outline='#8b6914', width=2)

# Corner ornaments
corner_size = 80
corners = [
    (border, border),
    (W-border-corner_size, border),
    (border, H-border-corner_size),
    (W-border-corner_size, H-border-corner_size)
]
for cx, cy in corners:
    draw.arc([cx, cy, cx+corner_size, cy+corner_size], 0, 90, fill='#d4a843', width=4)

# Fortune character 福
try:
    font_fu = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 420)
    font_title = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 72)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 42)
except:
    font_fu = ImageFont.load_default()
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# Draw 福 with slight shadow
text = "福"
bbox = draw.textbbox((0,0), text, font=font_fu)
tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
x, y = (W-tw)//2, (H-th)//2 - 60

draw.text((x+6, y+6), text, font=font_fu, fill=(0,0,0,120))
draw.text((x, y), text, font=font_fu, fill='#e8c96a')

# Title
title = "福气抽签"
bbox = draw.textbbox((0,0), title, font=font_title)
tw = bbox[2]-bbox[0]
draw.text(((W-tw)//2, y+th+40), title, font=font_title, fill='#f5efe4')

# Subtitle
sub = "每日一签 · 今日运势"
bbox = draw.textbbox((0,0), sub, font=font_sub)
tw = bbox[2]-bbox[0]
draw.text(((W-tw)//2, y+th+140), sub, font=font_sub, fill='#b8a898')

img.save("share-image.png", "PNG")
print("Generated share-image.png")
