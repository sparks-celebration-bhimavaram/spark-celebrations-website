import os
import glob
import re

files = glob.glob('c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/*.html')
old_url = r'https://images\.unsplash\.com/photo-1489599849927-2ee91cede3ba[^"]*'
new_url = "https://lh3.googleusercontent.com/gps-cs-s/AHVAweq6HvPoOZo-EwOR17DKxfYUMjHyVXcPcphBpmCn6r0U3hB83ITDprvIBnK4h8jvEiInNY_WEeeXHeIWD6mNIop40lnSF4Tojd9hcej7SN1B4QsGxe264jnASeHLtXo-QdRgRkW_81CmUu71=w1024"

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if re.search(old_url, html):
        html = re.sub(old_url, new_url, html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Replaced theater image in {os.path.basename(filepath)}")
