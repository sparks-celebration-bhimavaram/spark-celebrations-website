import glob
import os

files = glob.glob('c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. 'Cinematic Storytelling' side-by-side slides on mobile
    html = html.replace(
        '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">',
        '<div class="flex overflow-x-auto snap-x snap-mandatory gap-8 pb-4 hide-scrollbar md:grid md:grid-cols-2 lg:grid-cols-4 md:overflow-visible">'
    )
    
    html = html.replace(
        'group relative h-[350px] md:h-[460px] rounded-[2.5rem] overflow-hidden',
        'group relative h-[350px] md:h-[460px] rounded-[2.5rem] overflow-hidden min-w-[85vw] md:min-w-0 snap-center shrink-0 md:shrink-1'
    )

    # 2. 'Mini Private Theater' image right side
    html = html.replace(
        '<div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center mb-12">',
        '<div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-16 items-center mb-12">'
    )

    # 3. Decrease font sizes
    # Headings
    html = html.replace('text-4xl md:text-8xl', 'text-3xl md:text-8xl')
    html = html.replace('text-4xl md:text-6xl', 'text-2xl md:text-6xl')
    html = html.replace('text-3xl md:text-6xl', 'text-2xl md:text-6xl')
    
    # Subtitles
    html = html.replace('text-lg md:text-2xl', 'text-base md:text-2xl')
    html = html.replace('text-xl', 'text-lg md:text-xl')
    html = html.replace('text-lg ', 'text-base md:text-lg ')
    
    # Button texts
    html = html.replace('text-lg uppercase', 'text-sm md:text-lg uppercase')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print('Mobile styling and side-by-side block updates complete.')
