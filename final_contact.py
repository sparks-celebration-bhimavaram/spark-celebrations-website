import os

file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'

with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

email_block = """                            <div class="flex gap-4 items-start">
                                <span class="text-gold text-base md:text-lg md:text-xl mt-1">✉️</span>
                                <div>
                                    <div class="font-bold text-gold mb-1">Email</div>
                                    <a href="mailto:sparkcelebrations759@gmail.com" class="text-gray-300 hover:text-gold transition-colors">sparkcelebrations759@gmail.com</a>
                                </div>
                            </div>\n"""

# Insert the email block right before the Phone block
for i, line in enumerate(lines):
    if 'Phone</div>' in line:
        # The line containing 'Phone</div>' is inside the <div> for Phone.
        # We need to backtrack 2 lines to the `<div class="flex gap-4 items-start">`
        # Let's cleanly inject it before the flex gap-4 of the phone block.
        # Which is at i - 2
        lines.insert(i - 2, email_block)
        print("Success inserting email block.")
        break

with open(file, 'w', encoding='utf-8') as f:
    f.writelines(lines)
