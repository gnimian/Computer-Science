import random
print('guess a number from 1 to 100')
num=random.randint(1,101)
count=1
while True:
    inp=int(input('guess a number: '))
    if inp<0 or inp>100:
        print('Please choose an integer between 1 and 100')
        continue
    elif inp<num:
        print('too low')
    elif inp>num:
        print('too high')
    elif inp==num:
        break
    count+=1
print(f'it took you {count} tries to get the number')
    

