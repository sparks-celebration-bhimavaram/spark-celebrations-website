import os
import glob

replacements = {
    "ðŸ‘¶": "👶",
    "ðŸŽ\u0081": "🎁", # \u0081 because Sometimes the invisible space is a control character. Actually, 🎁 is F0 9F 8E 81 -> ðŸŽ<0x81>
    "ðŸŽ ": "🎁",
    "â ¤ï¸ ": "❤️",
    "ðŸŽ¬": "🎬",
    "ðŸŽ‚": "🎂",
    "ðŸ’\u008d": "💍", # 💍 is F0 9F 92 8D -> ðŸ’<0x8D>. Wait, in my grep output it was `ðŸ’ `. Let's just use bytes!
    "ðŸŽ\u00ad": "🎭",
    "âœ¨": "✨",
    "ðŸ“\u008d": "📍",
    "ðŸ“ž": "📞",
    "ðŸ•\u0090": "🕐", 
    "ðŸ“¸": "📸",
    "ðŸŽ‰": "🎉",
    "ðŸŽ¥": "🎥",
    "ðŸ“±": "📱",
    "ðŸ’°": "💰",
    "ðŸš€": "🚀",
    "â€”": "—",
    "â€“": "–",
    "Â·": "·",
    "â€™": "'"
}

def fix_mojibake():
    html_files = glob.glob(r"c:\Users\nk798\OneDrive\Desktop\websites\sparksnew1\*.html")
    for file in html_files:
        with open(file, 'rb') as f:
            content = f.read()

        # The characters are UTF-8 bytes that were read as Windows-1252 and then re-saved as UTF-8!
        # Which means the literal string "ðŸ‘¶" is now in the file encoded in UTF-8.
        # F0 9F 91 B6 -> 👶. In Windows-1252, this is \xf0 \x9f \x91 \xb6
        # When that gets written as UTF-8, it becomes C3 B0 C5 B8 E2 80 98 C2 B6
        try:
            text = content.decode('utf-8')
            for bad, good in replacements.items():
                text = text.replace(bad, good)
            
            # Additional fallback by bytes:
            text = text.replace("ðŸŽ\x81", "🎁")
            text = text.replace("ðŸ’\x8d", "💍")
            text = text.replace("ðŸŽ\xad", "🎭")
            text = text.replace("ðŸ“\x8d", "📍")
            text = text.replace("ðŸ•\x90", "🕐")

            with open(file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Fixed {file}")
        except Exception as e:
            print(f"Error on {file}: {e}")

fix_mojibake()
