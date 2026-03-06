import random
print('guess a number from one to 100: ')
a=1
x=random.randrange(1,101)
while True:
    guess=int(input('Take a guess: '))
    if guess==x:
        break
    elif guess<x:
        print('too low')
    else:
        print('too high')
    a+=1
print(f'it took you {a} guesses to win')

'''
import random
lower=int(input('guess from: ')
upper=int(input('guess to: '))

rand= random.randrange(lower, upper+1)
# rand=random.choice(list(range(lower,upper+1)))
print(rand)#cheating
count=0
while True:
    guess=int(input("take a guess: "))
    count=count+1
    if guess == rand:
        break
    elif guess>rand:
        print('too high')
    else: #elif guess<rand
        print('too low')
print('congrats')
print(f'it took you {count} guesses to win')
'''
