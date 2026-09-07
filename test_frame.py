from PIL import Image, ImageDraw, ImageFont
import os

def create_browser_frame(w, h, title, url):
    img = Image.new("RGB", (w, h), "#f8fafc")
    draw = ImageDraw.Draw(img)

    try:
        font_b = ImageFont.truetype("arialbd.ttf", 15)
        font_r = ImageFont.truetype("arial.ttf", 13)
        font_sm = ImageFont.truetype("arial.ttf", 11)
    except:
        font_b = font_r = font_sm = ImageFont.load_default()

    # Browser chrome header (Windows / Chrome style)
    draw.rectangle([0, 0, w, 75], fill="#1e293b")
    # Window controls (min, max, close)
    draw.ellipse([15, 12, 27, 24], fill="#ef4444")
    draw.ellipse([35, 12, 47, 24], fill="#f59e0b")
    draw.ellipse([55, 12, 67, 24], fill="#10b981")

    # Tab
    draw.rectangle([90, 8, 300, 38], fill="#334155")
    draw.text((105, 16), title[:26], fill="#f8fafc", font=font_sm)

    # Address bar
    draw.rectangle([0, 38, w, 75], fill="#0f172a")
    draw.rectangle([100, 44, w - 120, 68], fill="#1e293b", outline="#334155", width=1)
    draw.text((115, 49), url, fill="#94a3b8", font=font_sm)

    return img, draw

if __name__ == "__main__":
    img, draw = create_browser_frame(1440, 900, "HairFidence - Home", "http://127.0.0.1:8000/index.php")
    img.save("test_frame.png")
    print("Frame created successfully!")
