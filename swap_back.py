import os

file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'
with open(file, 'r', encoding='utf-8') as f:
    html = f.read()

s_contact = '        <!-- Contact / Location -->'
s_booking = '        <!-- Booking Form -->'
s_footer = '        <!-- Footer -->'

idx_contact = html.find(s_contact)
idx_booking = html.find(s_booking)
idx_footer = html.find(s_footer)

if all(i != -1 for i in [idx_contact, idx_booking, idx_footer]):
    if idx_booking < idx_contact:
        # Current: Booking -> Contact
        part1 = html[:idx_booking]
        part_book = html[idx_booking:idx_contact]
        part_cont = html[idx_contact:idx_footer]
        part_foot = html[idx_footer:]
        
        # Swap so Contact is above Booking
        new_html = part1 + part_cont + part_book + part_foot
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Swapped: Contact is now above Booking.")
    else:
        print("Contact is already above Booking. No changes made.")
else:
    print("Could not find section anchors.")
