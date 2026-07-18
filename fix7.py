import os

file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'
with open(file, 'r', encoding='utf-8') as f:
    html = f.read()

s_reviews = '        <!-- Reviews / Trust Signal: Directly Below Mini Theater -->'
s_gallery = '        <!-- Home Mini Gallery -->'
s_services = '        <!-- Services Section Grid -->'
s_booking = '        <!-- Booking Form -->'

# Find the exact indices
idx_rev = html.find(s_reviews)
idx_gal = html.find(s_gallery)
idx_serv = html.find(s_services)
idx_book = html.find(s_booking)

if all(i != -1 for i in [idx_rev, idx_gal, idx_serv, idx_book]):
    part1_before = html[:idx_rev]
    part_reviews = html[idx_rev:idx_gal]    # Includes reviews and testimonial
    part_gallery = html[idx_gal:idx_serv]   # Home mini gallery
    part_booking = html[idx_book:]          # Booking form onwards
    
    # We drop part_services entirely!
    
    # The user asked to "place review below the gallery"
    # So the order is: Gallery, then Reviews.
    new_html = part1_before + part_gallery + part_reviews + part_booking
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully replaced layout structure.")
else:
    print(f"Indices: rev={idx_rev}, gal={idx_gal}, serv={idx_serv}, book={idx_book}")
