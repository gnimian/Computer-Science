L=['mon','tues','wed','thur','fri','sat','sun']
'''
for day in L:
    print(day)
'''
i=iter(L)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
#print(next(i)) #fails with StopIteration error

#generator function yield data
def myrange(n):
    x=0
    while x<n:
        yield x
        x+=1
'''
for i in myrange(4):
    print(i)
'''
#turn generator function into an iterator
i=myrange(4)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print()
#generator function that yields fibonacci numbers
