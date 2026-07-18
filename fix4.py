import os

file_path = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/reels.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'mb-3 block' in line and i+2 < len(lines) and 'Proposal' in lines[i+2]:
        lines[i] = '                        <span class="text-6xl mb-3 block">❤️</span>\n'
    if 'mb-3 block' in line and i+1 < len(lines) and 'Proposal' in lines[i+1]:
        lines[i] = '                        <span class="text-6xl mb-3 block">❤️</span>\n'

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Finished fixing heart")
