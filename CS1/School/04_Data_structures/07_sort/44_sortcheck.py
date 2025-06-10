import random
def selsort_ip(L):
    Lsize = len(L)
    for x in range(Lsize):
        mindex = x
        for y in range (x,Lsize):
            if L[y] < L[mindex]:
                mindex = y
        L[mindex],L[x] = L[x],L[mindex]
a=[]
for x in range(10):
    b=random.randrange(1,100)
    a.append(b)
print(selsort_ip(a))
