import os
import re
import base64
import requests
from bs4 import BeautifulSoup

INPUT_FILE = os.path.join("output", "presentazione_finale.html")
OUTPUT_FILE = os.path.join("output", "presentazione_portable.html")

def download_resource(url):
    try:
        print(f"Downloading {url}...")
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"⚠️ Failed to download {url}: {e}")
        return None

def bundle():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ {INPUT_FILE} not found. Run generator.py first.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")

    # Bundle CSS
    for link in soup.find_all("link", rel="stylesheet"):
        href = link.get("href")
        if href and href.startswith("http"):
            css_content = download_resource(href)
            if css_content:
                style_tag = soup.new_tag("style")
                style_tag.string = css_content
                link.replace_with(style_tag)

    # Bundle JS
    for script in soup.find_all("script"):
        src = script.get("src")
        if src and src.startswith("http"):
            js_content = download_resource(src)
            if js_content:
                # Remove defer/async attributes to ensure correct execution order when inlined
                if script.has_attr('defer'): del script['defer']
                if script.has_attr('async'): del script['async']
                del script['src']
                script.string = js_content

    # Bundle Images (Local only)
    for img in soup.find_all("img"):
        src = img.get("src")
        if src and not src.startswith("http") and os.path.exists(src):
            with open(src, "rb") as img_file:
                b64_data = base64.b64encode(img_file.read()).decode('utf-8')
                ext = os.path.splitext(src)[1][1:] # e.g., png
                img['src'] = f"data:image/{ext};base64,{b64_data}"
                print(f"Embedded local image: {src}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(str(soup))
    
    print(f"✅ Portable presentation saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    bundle()
