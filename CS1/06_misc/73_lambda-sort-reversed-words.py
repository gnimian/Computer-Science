#sort strings based letter from the end of the word
#so alphabetic sort but rerversed
#lambda function have no name
'''
example:
>>> f=lambda x:x**2
>>> f(2)
4
>>> f(3)
9

#this is baically same as a function
def foo(x):
    return x**2
>>> foo(4)
16
'''
def reverseword(s): #boat
    return s[::-1]

L=['boat', 'car', 'house', 'building', 'shack']
print(sorted(L, key=lambda s: s[::-1]))

#same effect as above
print(sorted(L, key=reverseword))

#not the same as reverse order
print(sorted(L, reverse=True))
