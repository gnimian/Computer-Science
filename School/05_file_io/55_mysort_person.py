L=[]
with open('person.txt','r') as f:
    for line in f:
        L.append(line[:-1])
T=[]
for item in L:
    T.append(item.split(','))
def mysort(A):
    return A[1]
T.sort(key=mysort)
print(T)
