import random
def roll():
    d1=random.randrange(1,7)
    d2=random.randrange(1,7)
    y=d1
    z=d2
    return d1+d2
c=1
x=0
while True:
    input('press enter to roll:')
    b=x
    x= roll()
    print(f'you rolled {x}')
    if c==1:
        if x in (2,3,12):
            print('You Lose')
            c+=1
            break
        elif x in (7,11):
            print('You Win')
            c+=1
            break
        elif x in (4,5,6,8,9,10):
            print('roll again')
            c+=1
            continue

    if c>1:
        if x==b:
            print('you win')
            break
        elif x==7:
            print('you lose')
            break
        else:
            print('roll again')

'''
import random
def roll():
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    return d1+d2
def wingame():
    froll = roll()
    print(froll)
    if froll == 7 or froll == 11:
        return False
    elif froll ==2 or froll == 3 or froll == 2:
        return False
    else:
        while True:
            newroll == roll()
            if newroll == froll:
                return True
            elif newroll == 7:
                return False

'''
