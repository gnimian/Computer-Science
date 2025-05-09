import itertools

def cycle(L):
    x=0
    while True:
        yield L[x]
        x += 1
        if x >= len(L):
            x = 0
def cycle(L):