L=[]
with open('person.txt','r') as f:
    for line in f:
        L.append(line[:-1])
L.sort()
with open('sortedpeople.txt', 'w') as f:
    for line in L:
        f.write(line+'\n')

