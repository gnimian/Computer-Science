import random
def foo():
    x=list(range(1,7))
    y=random.sample(x,2)
    return y[0]+y[1]

'''
def roll():
    d1=random.randrange(1,7)
    d2=random.randrange(1,7)
    return d1+d2
'''
