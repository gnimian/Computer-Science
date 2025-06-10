'''
def foo(x, y=5):
    return x-y
print(foo(10,8))
'''

def foo(x):
    j=x+1

x=2
j=x
x=3
foo(j)
print(foo(j))
