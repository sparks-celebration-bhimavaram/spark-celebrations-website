import glob
import re

files = glob.glob('c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # We want to replace the dual-font block with a single-font block.
    # The current block usually looks like:
    # <span class="font-playfair ... uppercase ...">SPARK</span>
    # <span class="font-great-vibes ...">Celebrations</span>
    
    # We will use regex to find:
    pattern_nav = r'<span class="font-playfair[^>]*>SPARK</span>\s*<span class="font-great-vibes[^>]*>Celebrations</span>'
    
    # Wait, the exact strings in HTML:
    # <span class="font-playfair font-black text-4xl tracking-wide text-gold leading-none uppercase" style="text-shadow: 0 4px 10px rgba(0,0,0,0.8);">SPARK</span>
    # <span class="font-great-vibes text-3xl text-gold leading-none -mt-2" style="text-shadow: 0 4px 10px rgba(0,0,0,0.8);">Celebrations</span>
    
    # For index footer maybe different sizes. We can match 'font-great-vibes' and replace it with 'font-playfair'.
    # So wherever 'font-great-vibes' is used for "Celebrations", we change it to 'font-playfair'.
    
    # Replace the class
    html = re.sub(r'<span class="font-great-vibes([^"]*)"([^>]*)>Celebrations</span>', 
                  r'<span class="font-playfair font-black tracking-widest\1"\2>CELEBRATIONS</span>', html)
    
    # There might be "-mt-2" which makes them overlap. Let's adjust margins too.
    # Let's adjust sizes if needed. For instance, in index.html:
    # text-[5rem] to text-[3rem], text-[3rem] to text-[2rem]
    # Let's just do a string replace for the exact blocks to be safe if possible, or use regex carefully.

    # Let's clean up the exact blocks:
    # 1. Standard (Nav and Secondary Footers)
    block1_find = """<span class="font-playfair font-black text-4xl tracking-wide text-gold leading-none uppercase" style="text-shadow: 0 4px 10px rgba(0,0,0,0.8);">SPARK</span>
            <span class="font-great-vibes text-3xl text-gold leading-none -mt-2" style="text-shadow: 0 4px 10px rgba(0,0,0,0.8);">Celebrations</span>"""
    block1_rep = """<span class="font-playfair font-black text-4xl tracking-wide text-gold leading-none uppercase" style="text-shadow: 0 4px 10px rgba(0,0,0,0.8);">SPARK</span>
            <span class="font-playfair font-bold text-2xl tracking-[0.2em] text-gold leading-none uppercase mt-1" style="text-shadow: 0 4px 10px rgba(0,0,0,0.8);">CELEBRATIONS</span>"""
            
    # 2. Large (Index Footer)
    block2_find = """<span class="font-playfair font-black text-6xl tracking-wide text-gold leading-none uppercase">SPARK</span>
            <span class="font-great-vibes text-[3rem] text-gold leading-none -mt-2">Celebrations</span>"""
    block2_rep = """<span class="font-playfair font-black text-6xl tracking-wide text-gold leading-none uppercase">SPARK</span>
            <span class="font-playfair font-bold text-3xl tracking-[0.2em] text-gold leading-none uppercase mt-2">CELEBRATIONS</span>"""

    # 3. Index Hero
    block3_find = """<span class="text-gold font-playfair font-black uppercase tracking-wider block text-[5rem] md:text-[8rem] leading-none mb-0" style="text-shadow: 0 10px 30px rgba(212,175,55,0.3);">SPARK</span>
            <span class="font-great-vibes text-gold block text-[3rem] md:text-[5rem] leading-none -mt-4 md:-mt-8" style="text-shadow: 0 10px 30px rgba(212,175,55,0.3);">Celebrations</span>"""
    block3_rep = """<span class="text-gold font-playfair font-black uppercase tracking-wider block text-[5rem] md:text-[8rem] leading-none mb-0" style="text-shadow: 0 10px 30px rgba(212,175,55,0.3);">SPARK</span>
            <span class="font-playfair font-bold tracking-[0.2em] text-gold uppercase block text-[2.5rem] md:text-[4rem] leading-none mt-2 md:mt-4" style="text-shadow: 0 10px 30px rgba(212,175,55,0.3);">CELEBRATIONS</span>"""

    html = html.replace(block1_find, block1_rep)
    html = html.replace(block2_find, block2_rep)
    html = html.replace(block3_find, block3_rep)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated fonts to single Playfair font.")
