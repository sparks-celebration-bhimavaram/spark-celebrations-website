import glob
import re

files = glob.glob('c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Decrease image pixels for mobile view as requested.
    # Convert large &w=1920 to &w=800 (sufficient for mobile backgrounds, ok for desktop if scaled)
    # Convert medium w=800/900/600 to w=400 (enough for 1/2 or 1 column cards on mobile)
    html = html.replace('w=1920', 'w=800')
    html = html.replace('w=900', 'w=400')
    html = html.replace('w=800', 'w=400')
    html = html.replace('w=600', 'w=400')
    
    # 2. Fix Navbar paddings for mobile (px-10 is too much for small screens)
    html = html.replace('px-10 flex', 'px-6 md:px-10 flex')
    
    # 3. Fix absolute positioning on intro text so it doesn't overflow
    html = html.replace('text-[5rem]', 'text-[4rem] md:text-[5rem]')
    html = html.replace('text-[3rem]', 'text-[2.2rem] md:text-[3rem]')
    
    # 4. Fix fixed heights in reels.html (style="height:450px") 
    # Change to class-based responsive heights
    html = html.replace('style="height:450px"', 'class="h-[350px] md:h-[450px] w-full"')
    
    # 5. Fix heights in index.html (like h-[460px] or h-[500px])
    html = html.replace('h-[460px]', 'h-[350px] md:h-[460px]')
    html = html.replace('h-[500px]', 'h-[300px] md:h-[500px]')
    
    # 6. Button paddings on mobile
    html = html.replace('px-16 py-6', 'px-8 py-4 md:px-16 md:py-6')
    html = html.replace('px-12 py-5', 'px-8 py-4 md:px-12 md:py-5')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Mobile optimizations applied to all HTML files.")
