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
import sys
import getpass
if len(sys.argv) != 3:
    print("Usage: python script.py input.txt output.txt [e|d]")
    sys.exit(1)
print('Welcome to the Vigenere encrypter and decrypter')

with open(sys.argv[1], 'r') as r, open(sys.argv[2], 'w') as w:
    ed = input('Please input 'e' for encrypt and 'd' for decrypt)
    key=getpass.getpass("Please enter the key: ")

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

