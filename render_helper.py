import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "C:\\Windows\\Fonts\\consola.ttf"
BOLD_FONT_PATH = "C:\\Windows\\Fonts\\consolab.ttf"

def get_font(size, bold=False):
    path = BOLD_FONT_PATH if bold else FONT_PATH
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def render_terminal_screenshot(title, command, output_text, extra_image_path=None):
    # Padding and styling
    pad_x = 40
    pad_y = 30
    title_bar_height = 45
    line_spacing = 6
    
    font_code = get_font(20)
    font_bold = get_font(22, bold=True)
    font_title = get_font(18, bold=True)
    
    lines = []
    lines.append((f"$ {command}", "#50fa7b")) # Green prompt
    lines.append(("", "#ffffff"))
    for line in output_text.strip().split("\n"):
        lines.append((line, "#f8f8f2"))
        
    # Calculate dimensions
    max_line_width = 700
    for text, _ in lines:
        try:
            bbox = font_code.getbbox(text)
            w = bbox[2] - bbox[0]
            if w > max_line_width:
                max_line_width = w
        except:
            pass
            
    content_width = max(max_line_width + 80, 850)
    
    line_height = 28
    content_height = len(lines) * line_height + 40
    
    extra_img = None
    if extra_image_path and os.path.exists(extra_image_path):
        extra_img = Image.open(extra_image_path)
        # Resize extra image to fit nicely
        max_img_w = content_width - 80
        if extra_img.width > max_img_w:
            ratio = max_img_w / extra_img.width
            extra_img = extra_img.resize((int(extra_img.width * ratio), int(extra_img.height * ratio)), Image.Resampling.LANCZOS)
        content_height += extra_img.height + 40

    total_width = content_width + pad_x * 2
    total_height = title_bar_height + content_height + pad_y * 2
    
    # Create image with outer margin / shadow background
    margin = 30
    img_w = total_width + margin * 2
    img_h = total_height + margin * 2
    
    # Base background (sleek modern slate)
    img = Image.new("RGBA", (img_w, img_h), (24, 26, 31, 255))
    draw = ImageDraw.Draw(img)
    
    # Window rect coordinates
    wx0, wy0 = margin, margin
    wx1, wy1 = margin + total_width, margin + total_height
    
    # Outer terminal window background
    draw.rounded_rectangle([wx0, wy0, wx1, wy1], radius=14, fill=(40, 44, 52, 255), outline=(62, 68, 81, 255), width=2)
    
    # Title bar
    draw.rounded_rectangle([wx0, wy0, wx1, wy0 + title_bar_height], radius=14, fill=(33, 37, 43, 255))
    draw.rectangle([wx0, wy0 + title_bar_height - 10, wx1, wy0 + title_bar_height], fill=(33, 37, 43, 255))
    
    # Terminal buttons (macOS style dots)
    btn_y = wy0 + title_bar_height // 2
    draw.ellipse([wx0 + 18, btn_y - 6, wx0 + 30, btn_y + 6], fill=(255, 95, 86, 255)) # Red
    draw.ellipse([wx0 + 38, btn_y - 6, wx0 + 50, btn_y + 6], fill=(255, 189, 46, 255)) # Yellow
    draw.ellipse([wx0 + 58, btn_y - 6, wx0 + 70, btn_y + 6], fill=(39, 201, 63, 255))  # Green
    
    # Title text in title bar
    title_text = f"Terminal - {title}"
    draw.text((wx0 + 85, wy0 + 12), title_text, fill=(171, 178, 191, 255), font=font_title)
    
    # Content area
    cx = wx0 + pad_x
    cy = wy0 + title_bar_height + 25
    
    for text, color in lines:
        draw.text((cx, cy), text, fill=color, font=font_code)
        cy += line_height
        
    if extra_img:
        cy += 10
        # Draw plot border & paste
        img.paste(extra_img, (cx, cy))
        
    return img.convert("RGB")

print("Rendering helper defined.")
