import os
import re

# 1. Update script.js with the ambient sparkles logic
script_path = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/assets/js/script.js'
with open(script_path, 'r', encoding='utf-8') as f:
    script_content = f.read()

ambient_sparkles_code = """
    // Ambient Sparkles for selected sections
    const sparkleSections = document.querySelectorAll('.sparkle-bg');
    sparkleSections.forEach(section => {
        setInterval(() => {
            const spark = document.createElement('div');
            spark.className = 'absolute pointer-events-none w-1 h-1 md:w-1.5 md:h-1.5 bg-gold rounded-full shadow-[0_0_10px_#D4AF37] z-0';
            
            const startX = Math.random() * 100 + '%';
            const startY = Math.random() * 100 + '%';
            
            spark.style.left = startX;
            spark.style.top = startY;
            section.appendChild(spark);

            gsap.fromTo(spark, 
                { opacity: 0, scale: 0, y: 0 },
                {
                    opacity: 0.6 + Math.random() * 0.4,
                    scale: 1,
                    y: -30 - Math.random() * 50,
                    duration: 1.5 + Math.random() * 2,
                    ease: "power1.out",
                    onComplete: () => {
                        gsap.to(spark, {
                            opacity: 0,
                            scale: 0,
                            duration: 1,
                            onComplete: () => spark.remove()
                        });
                    }
                }
            );
        }, 350); // density of sparkles
    });
"""

# Insert this before exactly the closing tag inside the DOMContentLoaded
if 'const sparkleSections' not in script_content:
    script_content = script_content.replace('});\n\n// Skip intro and scroll', ambient_sparkles_code + '\n    // Skip intro and scroll')
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)

# 2. Add sparkle-bg classes to index.html
index_file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/index.html'
with open(index_file, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<section class="py-20 border-y border-white/5 bg-white/[0.02]">', '<section class="py-20 border-y border-white/5 bg-white/[0.02] sparkle-bg relative overflow-hidden">')
html = html.replace('<section class="pt-4 pb-12 bg-black">', '<section class="pt-4 pb-12 bg-black sparkle-bg relative overflow-hidden">')
html = html.replace('<section id="contact" class="pt-16 pb-24 relative" style="background:#080000">', '<section id="contact" class="pt-16 pb-24 relative sparkle-bg overflow-hidden" style="background:#080000">')
# Home Mini Gallery just in case they meant the mini gallery
html = html.replace('<section class="pb-16 bg-black border-b border-white/5">', '<section class="pb-16 bg-black border-b border-white/5 sparkle-bg relative overflow-hidden">')

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Add to gallery.html and join-team.html
gallery_file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/gallery.html'
if os.path.exists(gallery_file):
    with open(gallery_file, 'r', encoding='utf-8') as f:
        gh = f.read()
    # Let's just add it to the main tag
    gh = gh.replace('<main class="pt-20">', '<main class="pt-20 sparkle-bg relative overflow-hidden">')
    with open(gallery_file, 'w', encoding='utf-8') as f:
        f.write(gh)

team_file = 'c:/Users/nk798/OneDrive/Desktop/websites/sparksnew1/join-team.html'
if os.path.exists(team_file):
    with open(team_file, 'r', encoding='utf-8') as f:
        th = f.read()
    th = th.replace('<main class="pt-20">', '<main class="pt-20 sparkle-bg relative overflow-hidden">')
    with open(team_file, 'w', encoding='utf-8') as f:
        f.write(th)

print("Added ambient sparkles successfully.")
