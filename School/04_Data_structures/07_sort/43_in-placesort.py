def selsort_ip(L):
    Lsize= len(L)
    for x in range(Lsize):
        mindex=x
        for y in range(x,Lsize):
            if L[y] < L[mindex]:
                mindex = y
        L[mindex],L[x]=L[x],:[mindex]
    return L
L=list(range(10**4))
random.shuffle(L)
