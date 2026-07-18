import glob

files = glob.glob('c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if 'mb-3 block' in line and i+1 < len(lines) and 'Proposal' in lines[i+1]:
            lines[i] = '                        <span class="text-6xl mb-3 block">❤️</span>\n'
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
print('Fixed Heart Emoji')
