import os

directories = [
    r'C:\Users\nk798\OneDrive\Desktop\websites\sparksnew1',
    r'C:\Users\nk798\OneDrive\Desktop\SPARK_Platform',
    r'C:\Users\nk798\OneDrive\Desktop\websites\spark-celebrations-luxury',
    r'C:\Users\nk798\OneDrive\Desktop\websites\spark-celebrations-premium'
]
meta_tag = '<meta name="google-site-verification" content="46aPNrYZYtecrf4vN7ib_GL7Fpe5Ov_xUeBHK2OcYow" />'

for directory in directories:
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        continue
    print(f"Processing directory: {directory}")
    for filename in os.listdir(directory):
        if filename.endswith('.html') and filename != 'index.bak.html':
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if meta_tag not in content:
                # Insert after <head>
                if '<head>' in content:
                    new_content = content.replace('<head>', f'<head>\n    {meta_tag}')
                elif '</head>' in content:
                    new_content = content.replace('</head>', f'    {meta_tag}\n</head>')
                else:
                    print(f"No <head> tag found in {filename}")
                    continue
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                print(f"Tag already exists in {filename}")
