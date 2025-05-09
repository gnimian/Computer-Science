L=[4,6,6,5,1,6,6,7]
L.reverse()
print(L)

for i in range(len(L)-1,-1,-1):
    if L[i]==6:
        L.pop(i)
print(L)
'''
while 6 in L:
    L.remove(6)
'''
