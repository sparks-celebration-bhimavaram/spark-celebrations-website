import os
import re

file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'

with open(file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Footer Email pill
html = html.replace('mailto:contact@sparkcelebrations.com', 'mailto:sparkcelebrations759@gmail.com')
html = html.replace('✉️</span> Email Us', '✉️</span> sparkcelebrations759@gmail.com')

# 2. Add Email to the 'Find Us' section
# The Find us section has:
phone_block = """                            <div class="flex gap-4 items-start">
                                <span class="text-gold text-base md:text-lg md:text-xl mt-1">📞</span>
                                <div>
                                    <div class="font-bold text-white mb-1">Phone</div>
                                    <a href="tel:+918143655818" class="hover:text-gold transition-colors">+91 81436 55818</a>
                                </div>
                            </div>"""

email_block = """                            <div class="flex gap-4 items-start">
                                <span class="text-gold text-base md:text-lg md:text-xl mt-1">✉️</span>
                                <div>
                                    <div class="font-bold text-gold mb-1">Email</div>
                                    <a href="mailto:sparkcelebrations759@gmail.com" class="hover:text-gold transition-colors text-gray-300">sparkcelebrations759@gmail.com</a>
                                </div>
                            </div>"""

if phone_block in html:
    html = html.replace(phone_block, phone_block + '\n' + email_block)
else:
    print("Could not find the phone block to append email block in 'Find Us' section.")

with open(file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated email references.")
