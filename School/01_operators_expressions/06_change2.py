change=int(input("enter change: "))
quarters=change//25
a=change%25
b=a%10
c=b%5
dimes=(a)//10
nickels=(b)//5
pennies=(c)//1
print(f'{quarters} quarters')
print(f'{dimes} dimes')
print(f'{nickels} nickels')
print(f'{pennies} pennies')

mon=int(input('enter change: '))
q=mon//25
mon=mon%25
d=mon//10
mon=mon%10
n=mon//5
mon=mon%5
p=mon
print(f'{q} quarters')
print(f'{d} dimes')
print(f'{n} nickels')
print(f'{p} pennies')
