import sys
print(sys.argv,'and it has ',len(sys.argv),'items')
for x in range(len(sys.argv)):
    print('index',x,' = ', sys.argv[x])

with open(sys.argv[1]) as f:
    a=(f.read())
    print(a,end='')

with open(sys.argv[2]) as f:
    b=(f.read())
    print(b,end='')

with open(sys.argv[3], 'w') as f:
    c=a+b
    f.write(c)

'''
f=open(sys.argv[1],'r')
s=f.read()
print(s)
f.close
'''
