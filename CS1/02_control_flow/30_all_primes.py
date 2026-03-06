for i in range(2,101):
    for x in range(2,int(i**0.5)+1):
        if i%x == 0:
            break
    else:
        print(i)

'''
for x in range (2,101):
    isprime=True #boolean flag
    #for factor in range (2, int(math.sqrt(x))+1):
    for factor in range (2, int(x**0.5)+1):
        if x%factor==0:
            isprime=False
            break
    if isprime:
        print(x)
'''

'''
for x in range (2,101):
    for factor in range (2, int(math.aqrt(x))+1): #example of for else
        if x%factor==0:
            break
    else: #only executes else if no break
        print(x)
'''
