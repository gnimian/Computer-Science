import sys
'''
r = open(sys.argv[3], 'r')
w = open(sys.argv[4], 'w')
shift = int(sys.argv[2])
'''
r = open(sys.argv[1], 'r')
w = open(sys.argv[2], 'w')
print("Welcome to the Caesar Cipher Program!")
print("This program can encrypt or decrypt a file using a Caesar cipher.")
ed = input("Enter 'e' to encrypt or 'd' to decrypt: ")
shift = int(input("Enter a shift value: "))

if ed == 'e': # sys.argv[1]
    a = r.read()
    output = ''
    for x in a:
        output += chr((ord(x) + shift) % 128)
    w.write(output)

elif ed == 'd': #sys.argv[1]
    a = r.read()
    output = ''
    for x in a:
        output += chr((ord(x) - shift) % 128)
    w.write(output)
else:
    print("Invalid option. Please enter 'e' for encrypt or 'd' for decrypt.")
r.close()
w.close()
