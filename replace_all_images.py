import os
import re

file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'
with open(file, 'r', encoding='utf-8') as f:
    html = f.read()

url_intro = "https://lh3.googleusercontent.com/p/AF1QipPIO7irERRQ1oBmt8Rjt68KyYuAAznW3nCo90DC=w1920"
url_th1 = "https://lh3.googleusercontent.com/gps-cs-s/AHVAwepzMnVMBLOt0_vCr2G9bh0FkcHutBhqrI3VliImzqpdvCYccnGKjDoupc4EVa67eZbHULUj20SzKW3aHHm4MlULgUvxRe0Ae34AeJJ_2KNMGUox2-_DtuCbACousomwyOIWbptjVbh_JBR7=w800"
url_th2 = "https://lh3.googleusercontent.com/gps-cs-s/AHVAweorBkULnBCM4cWbPa6njMxozzvd9-gh3eMjIJxBLtEFfO52t_ajrua3FJAfq5gUQClqSKdp9NHWSkZ7Vt2k9REWF2B1_7KHkCBXMWh33Qeq-BS03eQuyntA-4inNsrwRyzYRvllI1MIK5E=w800"
url_bth = "https://lh3.googleusercontent.com/gps-cs-s/AHVAwepo5adhMsNUS0jXJzWurEs2iHD0FDeF2iq49pDw4-wZpRTRBNN86ZjVqSv9wrChvrWYZADdlhkwBfq39MLarhE-Fkh0WCGVFy6JEX_idJXC4lfAnSFiTTS5iBTd_PfzhF5H54xRx9mmEJOG=w800"

# 1. Intro overlay
left_curtain = '<div class="curtain-left w-1/2 h-full flex flex-col items-end justify-center relative overflow-hidden">'
if '<div class="curtain-left w-1/2 h-full flex flex-col items-end justify-center">' in html:
    html = html.replace('<div class="curtain-left w-1/2 h-full flex flex-col items-end justify-center">', left_curtain + f'\n            <img src="{url_intro}" class="absolute inset-0 w-[200vw] max-w-none h-full object-cover object-left opacity-30 z-[-1] pointer-events-none">')

right_curtain = '<div class="curtain-right w-1/2 h-full flex flex-col items-start justify-center relative overflow-hidden">'
if '<div class="curtain-right w-1/2 h-full flex flex-col items-start justify-center">' in html:
    html = html.replace('<div class="curtain-right w-1/2 h-full flex flex-col items-start justify-center">', right_curtain + f'\n            <img src="{url_intro}" class="absolute inset-0 w-[200vw] max-w-none h-full object-cover object-right opacity-30 z-[-1] pointer-events-none" style="transform: translateX(-50vw);">')

# 2. Theater images
# Replace the single theater box with a two-column grid
# I will find the URL and replace the outer div
old_th_url = r'https://lh3\.googleusercontent\.com/gps-cs-s/AHVAweq6HvPoOZo-EwOR17DKxfYUMjHyVXcPcphBpmCn6r0U3hB83ITDprvIBnK4h8jvEiInNY_WEeeXHeIWD6mNIop40lnSF4Tojd9hcej7SN1B4QsGxe264jnASeHLtXo-QdRgRkW_81CmUu71=w1024'
if re.search(old_th_url, html):
    # Locate index
    html = re.sub(r'<div class="relative rounded-3xl overflow-hidden shadow-\[0_0_60px_rgba\(212,175,55,0\.15\)\] border border-gold/20">\s*<img src="' + old_th_url + r'" alt="SPARK Mini Private Theater" class="w-full h-\[300px\] md:h-\[500px\] object-cover">\s*<div class="absolute inset-0 bg-gradient-to-r from-black/40 to-transparent pointer-events-none"></div>\s*</div>', 
    f"""<div class="grid grid-cols-2 gap-2 md:gap-4 shadow-[0_0_60px_rgba(212,175,55,0.15)] rounded-3xl border border-gold/20 overflow-hidden bg-black/50 p-2">
                        <div class="relative rounded-2xl overflow-hidden group">
                            <img src="{url_th1}" alt="SPARK Mini Private Theater 1" class="w-full h-[300px] md:h-[500px] object-cover group-hover:scale-110 transition-transform duration-700">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent pointer-events-none"></div>
                        </div>
                        <div class="relative rounded-2xl overflow-hidden group">
                            <img src="{url_th2}" alt="SPARK Mini Private Theater 2" class="w-full h-[300px] md:h-[500px] object-cover group-hover:scale-110 transition-transform duration-700">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent pointer-events-none"></div>
                        </div>
                    </div>""", html)
else:
    print("Could not find the old theater image url to replace.")

# 3. Birthday block
old_bth_pattern = r'https://images\.unsplash\.com/photo-1544256718-3bcf237f3974[^"]*'
if re.search(old_bth_pattern, html):
    html = re.sub(old_bth_pattern, url_bth, html)
else:
    print(f"Could not find birthday Unsplash pattern.")

with open(file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated all requested images!")
