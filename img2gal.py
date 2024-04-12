"""
file: img2gal.py
author: Mason Armand
date created: April 12, 2024
last modified: April 12, 2024
"""

import os
import sys
from PIL import Image
from shutil import copyfile

def create_thumbnail(img_path, thumb_path):
    print(f"Creating thumbnail for {img_path}...")
    img = Image.open(img_path)
    if img.mode == "RGBA":
        img = img.convert("RGB")
    w_percent = (300 / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((300, h_size), Image.LANCZOS)
    img.save(thumb_path, "JPEG")
    return 300, h_size

def is_image(filename):
    ext = (".jpg", ".jpeg", ".png", ".gif", ".tiff", ".webp", ".bmp")
    return filename.lower().endswith(ext)

def genhtml(path, gallery, template, output):
    html = ""
    thumb_path = os.path.join(output, "thumb")
    if not os.path.exists(thumb_path):
        os.makedirs(thumb_path)

    images = []
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path) and is_image(f):
            images.append(f)

    for img in images:
        img_path = os.path.join("..", path, img)
        img_jpeg = img[:-4] + ".jpeg"
        thumb_name = gallery + "_" + img_jpeg
        img_thumb_path = os.path.join("thumb", thumb_name)
        thumb_rel_path = os.path.join(thumb_path, thumb_name)
        tw, th = create_thumbnail(os.path.join(path, img), thumb_rel_path)

        html += f'''
        <a href="{img_path}" class="glightbox">
            <img src="{img_thumb_path}" alt="{img}" width="{tw}" height="{th}">
        </a>
        '''

    final_html = template.replace("{{content}}", html)
    final_html = final_html.replace("{{gallery_name}}", gallery)
    with open(os.path.join(output, gallery + ".html"), 'w') as f:
        f.write(final_html)


def main(output, template_path):
    if not os.path.exists(output):
        os.makedirs(output)

    with open(template_path, 'r') as f:
        template = f.read()

    galleries = []
    for d in os.listdir("gallery"):
        dir_path = os.path.join("gallery", d)
        if os.path.isdir(dir_path):
            galleries.append(d)

    for gal in galleries:
        gal_path = os.path.join("gallery", gal)
        genhtml(gal_path, gal, template, output)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <output_folder> <template_html_file>")
        sys.exit(1)
    output_folder, template_file = sys.argv[1], sys.argv[2]
    main(output_folder, template_file)

