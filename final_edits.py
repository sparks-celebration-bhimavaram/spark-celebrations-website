import os

file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'
with open(file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add venue decoration
target_option = '<option value="Wedding">Wedding Event</option>'
if target_option in html:
    html = html.replace(target_option, target_option + '\n                            <option value="Venue Decoration">Venue Decoration</option>')
else:
    print("Could not find Wedding Event option.")

# 2. Fix whatsapp sticky logo
target_wa = 'class="fixed bottom-10 right-10 z-[90] bg-[#25D366] p-5 rounded-full shadow-2xl hover:scale-110 transition-transform"'
if target_wa in html:
    html = html.replace(target_wa, 'class="fixed bottom-10 right-10 z-[90] bg-[#25D366] w-16 h-16 rounded-full shadow-[0_4px_20px_rgba(37,211,102,0.4)] hover:scale-110 transition-transform flex items-center justify-center"')
    
    html = html.replace('<svg class="w-8 h-8 text-white fill-current"', '<svg class="w-9 h-9 text-white fill-current"')
else:
    print("Could not find WA sticky class.")

# 3. Replace Footer links
# Search for Facebook or YouTube broadly
import re
target_socials = re.search(r'<div class="flex justify-center gap-10 mb-16">.*?</div>', html, re.DOTALL)
if target_socials:
    new_socials = """<div class="flex flex-wrap justify-center gap-6 md:gap-10 mb-16">
                    <a href="https://www.instagram.com/spark.celebrations.bhimavaram/" target="_blank" class="flex items-center gap-2 text-gray-400 hover:text-gold transition-all uppercase tracking-widest font-bold text-sm border border-white/10 px-4 py-2 rounded-full">
                        <span class="text-xl">📸</span> Instagram
                    </a>
                    <a href="mailto:contact@sparkcelebrations.com" class="flex items-center gap-2 text-gray-400 hover:text-gold transition-all uppercase tracking-widest font-bold text-sm border border-white/10 px-4 py-2 rounded-full">
                        <span class="text-xl">✉️</span> Email Us
                    </a>
                    <a href="tel:+918143655818" class="flex items-center gap-2 text-gray-400 hover:text-gold transition-all uppercase tracking-widest font-bold text-sm border border-white/10 px-4 py-2 rounded-full">
                        <span class="text-xl">📞</span> +91 81436 55818
                    </a>
                </div>"""
    html = html.replace(target_socials.group(0), new_socials)
else:
    print("Could not find social footer links.")

with open(file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied final edits.")
