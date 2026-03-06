L=[6,3,2,5,1,4]
def findsmall(L):
    a=L[0]
    for i in range (len(L)):
        if L[i]<a:
            a=L[i]
    L.remove(a)
    return a

def selsort(e):
    SL=[]
    for i in range (len(L)):
        a=findsmall(L)
        SL.append(a)
    return SL

print(selsort(L))

'''
def findmin(L):
    min=L[0] #assume first item is smallest
    for x in range(len(L)):
        if L[x] < min:
            min = l[x]
    return min
#OR
def findmindex(L): #this uses L.pop
    mind=0
    for x in range(len(L)):
        if L[x] < L[mind]:
            mind = x
    return mind
'''
'''
def selsort(a):
    SL=[]
    for i in range (len(L)):
        b=findmindex(L)
        SL.append(L[b])
        L.pop(b)
    return SL
#OR
def selsort(L):
    sl=[]
    while len(L)>0:
        num=findmin(L)
        #num=min(L)
        L.remove(num)
        sl.append(num)
    return sl
#OR
def selsort(L):
    sl=[]
    while (len(L)>0):
        lowest = 0
        for x in range(len(L)):
            if L[x] < L[lowest]:
                lowest=x
            sl.append(L[lowest])
            L.pop(lowest)
'''
'''
L=[6,3,8,5,2,9,4]
#print('findmin(L))
print(L[findmindex(L)])
print(min(L))
print(selsort(L))
#OR
L=[]
for x in range(10):
    L.append(random.randrange(10,100))
print(L)
print(selsort(L))
'''

