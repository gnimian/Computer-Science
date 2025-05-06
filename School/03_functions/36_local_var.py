def foo():
    x=3
    print(x)
x=1
foo()
print(x)

'''
def foo():
    x=x+1
    print(x)
x=1
foo()
print(x) #x is undefined, cannot assess local variable x since it is not associated with a variable)
'''

def foo():
    global x
    x=x+1
x=1
print(x)
foo()
print(x)

