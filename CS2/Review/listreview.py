def total(t):
    s=0
    for num in t:
        s=s+t
    return s

L=[]
t=[]
t.append(3)
L.append(t)
L.append([5,6,8])
L.append([9,2,1])
L.append([9,2,1,0,33])
print(L)


for i in range(len(L)):
    for j in range(len(L[i])):
        print(f'{L[i][j]} ', end='')
    print("\n")

#Alternative way to print the same thing
'''
for i in L:
    for j in i:
        print(j, end='')
    print("\n")
'''
