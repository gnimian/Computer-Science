'''
x=0
while True:
    b=int(input('Enter number: '))
    if b==0:
        break
    c=b+x
    print(f'total = {c}')
    x=c
'''
tot=0
while True:
    x=input('Enter number: ')
    if x== 'done':
        break
    integer=int(x)
    tot=integer+tot
print(f'total is {tot}')



