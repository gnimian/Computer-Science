'''
while True:
    num=int(input('Enter Number: '))
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            print(f'no, {num} is not prime')
            break
        else:
            print(f'Yes, {num} is prime')
            break


'''
while True:
    n=int(input('please enter a number: '))
    prime=True
    for x in range(2,int((n**0.5)+1)):
        print(f'{n} / {x}')
        if n%x == 0:
            prime=False
            break
    if prime:
        print('prime')
    else:
        print('not prime')

