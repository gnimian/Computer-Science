num=int(input('factorial of: '))
x=1
a=1
while a<=num:
    x*=a
    a+=1

print(f'the factorial of {num} is {x}')

n=int(input('factorial of: '))
tot=1
for x in range(2,n+1):
    tot=tot*x

