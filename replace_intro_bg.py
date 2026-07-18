import re
import os

file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'

with open(file, 'r', encoding='utf-8') as f:
    html = f.read()

old_intro_url = r'https://lh3\.googleusercontent\.com/p/AF1QipPIO7irERRQ1oBmt8Rjt68KyYuAAznW3nCo90DC=w1920'
new_intro_url = "https://www.shutterstock.com/shutterstock/videos/3884233387/thumb/1.jpg?ip=x480"

if re.search(old_intro_url, html):
    html = re.sub(old_intro_url, new_intro_url, html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced intro background image successfully.")
else:
    print("Could not find the old intro background image in the file.")
