import re

file_path = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the three anchors
str_contact = '        <!-- Contact / Location -->'
str_booking = '        <!-- Booking Form -->'
str_footer = '        <!-- Footer -->'

idx_contact = html.find(str_contact)
idx_booking = html.find(str_booking)
idx_footer = html.find(str_footer)

if idx_contact != -1 and idx_booking != -1 and idx_footer != -1:
    part1_before_contact = html[:idx_contact]
    part2_contact = html[idx_contact:idx_booking]
    part3_booking = html[idx_booking:idx_footer]
    part4_footer = html[idx_footer:]

    # Reassemble with booking before contact
    new_html = part1_before_contact + part3_booking + part2_contact + part4_footer
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Swapped Booking and Contact sections.")
else:
    print("Could not find section anchors.")
