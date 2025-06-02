import sys
'''
r = open(sys.argv[3], 'r')
w = open(sys.argv[4], 'w')
shift = int(sys.argv[2])
'''
r = open(sys.argv[1], 'r')
w = open(sys.argv[2], 'w')
print("Welcome to the Vigenere Program!")
print("This program can encrypt or decrypt a file using a Vigenere cipher.")
ed = input("Enter 'e' to encrypt or 'd' to decrypt: ")
key = input("Enter a key(letters only): ")

if ed == 'e': # sys.argv[1]
    a = r.read()
    
    w.write(output)

elif ed == 'd': #sys.argv[1]
    a = r.read()
    
    w.write(output)

else:
    print("Invalid option. Please enter 'e' for encrypt or 'd' for decrypt.")
r.close()
w.close()
