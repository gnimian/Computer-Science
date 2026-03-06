print('reading line by line from a file object')
f=open('flowers.txt','r')
for line in f:
    print(line, end='')
f.close()
print()

print('reading into a list')
f=open('flowers.txt','r')
Lines= f.readlines() #readlines returns a list of strings
for line in Lines:
    print(line, end='')
for x in range (len(Lines)):
    print(Lines[x], end='')
f.close
print()

print('reading entire file into a string')
f=open('flowers.txt','r')
text=f.read()
print(text)
f.close
print()

print('reading one char at a time')
f=open('flowers.txt','r')
while True:
    c=f.read(1)
    if not c:
        break
    print(c,end='')
f.close()
print()

print('reading with open')
with open('flowers.txt') as f:
    for line in f:
        print(line, end='')

