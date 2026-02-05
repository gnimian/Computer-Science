import random
L=['a','b','c','d']
print(random.choice(L))

M=['apple','bee','cat','door']
#can do random.choice(M) but we only get 1
print(random.choice(range(len(L))))
random.randrange(4) #same thing
print(L[3])
print(M[3])

