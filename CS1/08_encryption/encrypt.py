word=input("Enter a word to encrypt: ")
shift=(int(input("enter a shift value:")))
new=''
for i in word:
    new+= chr((ord(i) + (shift))%64+32)
print(f'Encrypted word: {new}')

old=''
for j in new:
    old+=chr((ord(j)-32-shift)%64)
    
print(f'Decrypted word: {old}')

'''
N=''
for let in s:
    E = chr(ord(let) + 3)
    N = N+E
'''
