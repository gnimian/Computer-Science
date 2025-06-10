avg=0
a=0
while True:
    x=input('Enter a Number: ')
    if x=='done':
        break
    b=int(x)
    avg=b+avg
    a=a+1


print(f'average is {avg/a}')





