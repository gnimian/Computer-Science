import random
L=[]
for r in range(4):
    t=[]
    for c in range(3):
        if 0 in t:
            num=random.randrange(1,3)
        else:
            num=random.randrange(3)
        t.append(num) 
    L.append(t)

for d in range(4):
    for c in range(3):
        print(f'{L[d][c]} ', end='')
    print()
print()

for r in range(len(L)):
    if 0 in L[r]:
        print(r, L[r].index(0))

'''
for r in range(4):
    for c in range(3):
        if L[r][c]==0:
            print(r,c)
'''