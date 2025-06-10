L=[1,2,2,4,6,6,6,7,8,8,9]
U=[]
D=[]
for i in range(len(L)):
    a=L.count(L[i])
    if a>1 and (L[i] not in D):
        D.append(L[i])
    elif a==1:
        U.append(L[i])
print(f'Unique={U}')
print(f'Duplicate={D}')

'''
import random
for x in range(15):
    L.append(random.randrange(10))
U=[]
D=[]
for mun in L:
    if L.count(num) > 1:
        D.append(num)
    else:
        U.append(num)
D=set(D)
D=list(D)
'''
