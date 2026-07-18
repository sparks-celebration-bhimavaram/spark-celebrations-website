import os
import re

file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'

with open(file, 'r', encoding='utf-8') as f:
    html = f.read()

url_th1 = "https://lh3.googleusercontent.com/gps-cs-s/AHVAwepzMnVMBLOt0_vCr2G9bh0FkcHutBhqrI3VliImzqpdvCYccnGKjDoupc4EVa67eZbHULUj20SzKW3aHHm4MlULgUvxRe0Ae34AeJJ_2KNMGUox2-_DtuCbACousomwyOIWbptjVbh_JBR7=w800"

old_grid = r'<div class="grid grid-cols-2 gap-2 md:gap-4 shadow-\[0_0_60px_rgba\(212,175,55,0\.15\)\] rounded-3xl border border-gold/20 overflow-hidden bg-black/50 p-2">.*?<div class="relative rounded-2xl overflow-hidden group">.*?<img src="[^"]*" alt="SPARK Mini Private Theater 2"[^>]*>.*?</div>.*?</div>'
# Wait, regex dotall is safer
if 'SPARK Mini Private Theater 2' in html:
    # Just replace the grid container and the inner divs with the elegant single image layout
    start_str = '<div class="grid grid-cols-2 gap-2 md:gap-4 shadow-[0_0_60px_rgba(212,175,55,0.15)] rounded-3xl border border-gold/20 overflow-hidden bg-black/50 p-2">'
    end_str = '</div>\n                    </div>\n                </div>'
    
    # We will just substitute the entire block. Finding exactly what we need:
    # We'll use re.sub with re.DOTALL to replace the entire grid wrapper
    pattern = r'<div class="grid grid-cols-2 gap-2 md:gap-4 shadow-\[0_0_60px_rgba\(212,175,55,0\.15\)\] rounded-3xl border border-gold/20 overflow-hidden bg-black/50 p-2">.*?</div>\s*</div>\s*</div>'
    
    single_image_block = f"""<div class="relative rounded-3xl overflow-hidden shadow-[0_0_60px_rgba(212,175,55,0.15)] border border-gold/20 group">
                        <img src="{url_th1}" alt="SPARK Mini Private Theater" class="w-full h-[300px] md:h-[500px] object-cover group-hover:scale-105 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-r from-black/40 to-transparent pointer-events-none"></div>
                    </div>"""
    
    html = re.sub(pattern, single_image_block, html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Reverted to a single theater image and removed the second one!")
else:
    print("Could not find the 2-column theater grid.")
