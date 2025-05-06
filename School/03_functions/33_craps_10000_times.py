'''
import random
def roll():
    d1=random.randrange(1,7)
    d2=random.randrange(1,7)
    y=d1
    z=d2
    return d1+d2
c=1
x=0
win=0
lose=0
for i in range(1,10001):
    while True:
        b=x
        x= roll()
        if c==1:
            if x in (2,3,12):
                lose+=1
                c+=1
                break
            elif x in (7,11):
                win+=1
                c+=1
                break
            elif x in (4,5,6,8,9,10):
                c+=1
                continue
        if c>1:
            if x==b:
                win+=1
                break
            elif x==7:
                lose+=1
                break
print(f'there are {win} wins and {lose} loses')
'''
import random
def roll():
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    return d1+d2
win=1
lose=1
for i in range(1,10000):
    def wingame():
        froll = roll()
        if froll == 7 or froll == 11:
            win+=1
            return True
        elif froll ==2 or froll == 3 or froll == 12:
            lose+=1
            return False
        else:
            while True:
                newroll = roll()
                if newroll == froll:
                    return True
                elif newroll == 7:
                    return False
    if wingame==True:
        win+=1
    else:
        lose+=1
print(f'you won {win} times and lost {lose} times')

