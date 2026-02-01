import random
L=[]
for i in range(4):
    l=[]
    num=0
    while len(l)<3:
        a=random.randrange(0,3)
        if a == 0:
            num+=1
        if num>=2:
            continue
        l.append(a)
    L.append(l)

for i in range(len(L)):
    for j in range(len(L[i])):
        print(f'{L[i][j]} ', end='')
    print()
print()
for i in range(len(L)):
    for j in range(len(L[i])):
        if L[i][j]==0:
            print(j,i)

#Teacher Solution
'''
L=[]
for r in range(4):
    t=[]
    while True:
        num=random.randrange(3)
        if num==0 and 0 in t:
            continue
        t.append(num)
        break  
    L.append(t)
for r in range(4):
    for c in range(3):
        print(f'{L[r][c]} ', end='')
    print()
print()
for r in range(4):
    for c in range(3):
        if L[r][c]==0:
            print(r,c)
'''
