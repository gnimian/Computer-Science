print('please think of a number that is between 1 and 100')
guess=50
b=100
c=0
d=1
while True:
    num=input(f'Is the number {guess}   (Please reply with Correct c/ lower l/ higher h)')
    if num== 'c':
        break
    elif num== 'l':
        print(f'high={guess}')
        print(f'low={c}')
        b=a
        a=(c+a)//2

    elif num== 'h':
        print(f'high={b}')
        print(f'low={guess}')
        c=a
        a=(b+a)//2
    d+=1
print(f'It took me {d} tries to get the answer')

'''
low=0
high=100
input('Secretely pick a random number between 1-100 and remember it.\n Don't cheat. Hit enter when done: ')

count=0
while True:
    guess=round((high+low)/2)
    count+=1
    reply=input(f'Is the number {guess}((Please reply with Correct c/ lower l/ higher h): ')
    reply=reply.lower

    if reply == 'c':
        break
    elif reply == 'h':
        low = guess
    else:
        print('respond not recognized')

    print(f'high={high}')
    print(f'low={low}')
print(f'I guessed the correct number in {count} guesses')


