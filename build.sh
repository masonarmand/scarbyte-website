#!/bin/bash
txt2web /var/www/html
python3 img2gal.py /var/www/html gallery/template.html
rm /var/www/html/gallery/template.html

if [[ "$1" == "--push" ]]; then
    git add .
    git commit -m "."
    git push
    neocities push /var/www/html
fi
