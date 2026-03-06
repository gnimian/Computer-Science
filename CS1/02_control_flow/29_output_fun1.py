'''
s='hatari'
n=''
for x in range(0, len(s)-1, 2):
    n=s[x+1] + s[x] + n
print(n)
'''

a=10
b=5
x=0
while a+b>0:
    a=a-1
    b=b-a
    x=a-b-x
print(x)
