import random
'''
#print 20 random numbers from 10-99
for i in range(20):
    print(random.randrange(10,100))

#Put ramdom numbers einto a list (print list)
L = []
for x in range(20):
    L.append(random.randrange(1,100))
print(L)
'''
#create 10 lists, in each list put 5 ramdon numbers from 10-99
for i in range (10):
    P = []
    for j in range (5):
        P.append(random.randrange(10,100))
    print(P)


