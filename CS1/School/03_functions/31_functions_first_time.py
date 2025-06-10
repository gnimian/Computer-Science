#Example 1
'''
def foo(x):
    print('Hi'*x)

def boo(a):
    return "bye"*a

for x in range(5): #01234
    foo(x)

for x in range(5):
    foo(x)
'''

#Example 2
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y

print(add(3,4))
print(subtract(9,3))

z=add(8,6)
print(z)
