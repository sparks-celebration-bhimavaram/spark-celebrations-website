import os
import re

file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'
with open(file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hero background image URL
# The current URL is like https://images.unsplash.com/photo-1511795409834-ef04bbd61622...
old_url_pattern = r'https://images\.unsplash\.com/photo-1511795409834-ef04bbd61622[^"]*'
new_url = "https://lh3.googleusercontent.com/gps-cs-s/AHVAweqVs3JC3uiwmm8dB-S-_KgWyb8zrsQVX6GfsKgeXzUlAxe1UkuzO9y9Dz1t3WgMLZtK0UuFjw1QdPLCCFFRS8N_qJFvRD2l1y4ofInimFnxcw1IfPlYIRu8E32lPnDatV15BPpEqBI6BUcA=w1920"

if re.search(old_url_pattern, html):
    html = re.sub(old_url_pattern, new_url, html)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated hero background image.")
else:
    print("Could not find the target unsplash URL for the hero section.")
