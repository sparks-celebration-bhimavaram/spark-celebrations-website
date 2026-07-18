import glob

files = glob.glob('c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/*.html')
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines):
            if 'font-great-vibes' in line and 'Celebrations' in line:
                # Change font class and make uppercase
                line = line.replace('font-great-vibes', 'font-playfair font-bold uppercase tracking-[0.2em]')
                line = line.replace('Celebrations', 'CELEBRATIONS')
                
                # Adjust negative margins to positive so they stack nicely instead of overlapping
                line = line.replace('-mt-1', 'mt-1')
                line = line.replace('-mt-2', 'mt-1')
                line = line.replace('-mt-4', 'mt-2')
                line = line.replace('-mt-8', 'mt-3')
                
                # Reduce text size slightly so it fits nicely under SPARK
                line = line.replace('text-[3rem]', 'text-[1.8rem]')
                line = line.replace('text-[5rem]', 'text-[3rem]')
                line = line.replace('text-3xl', 'text-xl')
                line = line.replace('text-4xl', 'text-2xl')
                
                lines[i] = line
                
        with open(file, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    except Exception as e:
        print(f"Error processing {file}: {e}")

print('Single font applied.')
