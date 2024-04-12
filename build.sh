git add .
git commit -m "."
git push
txt2web /var/www/html
python3 img2gal.py /var/www/html gallery/template.html
rm /var/www/html/gallery/template.html
neocities push /var/www/html
