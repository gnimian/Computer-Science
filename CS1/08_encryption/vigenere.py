import sys
import getpass
if len(sys.argv) != 4:
    print("Usage: python script.py input.txt output.txt [e|d]")
    sys.exit(1)

with open(sys.argv[1], 'r') as r, open(sys.argv[2], 'w') as w:
    ed = sys.argv[3]
    key=getpass.getpass("Enter the key: ")

    def key_shift():
        while True:
            for i in key:
                yield i
    shift=key_shift()

    if ed == 'e':
        a = r.read()
        out=''
        for i in a:
            x = ord(i) + ord(next(shift))
            out += chr(x)
        w.write(out)
    elif ed == 'd':
        a = r.read()
        out=''
        for i in a:
            x= ord(i) - ord(next(shift))
            out += chr(x)
        w.write(out)

    else:
        print("Invalid mode. Please input 'e' for encrypt or 'd' for decrypt.")
print("done")

'''
import sys, getpass
def foo(p):
    x=0
    while True:
        yield p[x%len(p)]
        x += 1
with open(sys.argv[1],r) as f:
    text=f.read()

p=getpass.getpass('Enter password: ')
#passlet=foo(p)
passlet = it.cycle(p)
sht='' #shifted text
for let in text:
    cn = ord(let)
    pn = ord(next(passlet))
    if sys.argv[3][0].lower() == 'e':
        num = (cn + pn) % 128
    elif sys.argv[3][0].lower() == 'd':
        num = (cn - pn) % 128
    else:
        print('Error: third arg must either be E or D to Encrypt or Decrypt. Program terminated')
        sys.exit(1)
    sht = sht + chr(num)
with open(sys.argv[2], 'w') as f:
    f.write(sht)
'''
