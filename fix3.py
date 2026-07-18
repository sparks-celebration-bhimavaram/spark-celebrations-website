import glob

with open('c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/reels.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace corrupted characters manually
text = text.replace('â ¤ï¸ ', '❤️')
# Remove any accidental \r\r\n
text = text.replace('\r\r\n', '\n')

with open('c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/reels.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/blog.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

text2 = text2.replace('â†’', '→')
text2 = text2.replace('\r\r\n', '\n')
text2 = text2.replace('â€”', '—')

with open('c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/blog.html', 'w', encoding='utf-8') as f:
    f.write(text2)
print("Done final fix")
