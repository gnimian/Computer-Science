def mymin(L):
    sm=L[0]
    for i in range(len(L)):
        if L[i]<sm:
            sm=L[i]
    return sm
L=[6,4,9,1,7,3]
print(mymin(L))
