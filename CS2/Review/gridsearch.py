import random
L=[]
for i in range(4):
    l=[]
    num=0
    while len(l)<=2:
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

for i in range(len(L)):
    for j in range(len(L[i])):
        if L[i][j]==0:
            print(j,i)
