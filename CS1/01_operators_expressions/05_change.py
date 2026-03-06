change=int(input("enter change: "))
quarters=change//25
dimes=(change-quarters*25)//10
nickels=(change-quarters*25-dimes*10)//5
pennies=(change-quarters*25-dimes*10-nickels*5)//1
print(f'{quarters} quarters')
print(f'{dimes} dimes')
print(f'{nickels} nickels')
print(f'{pennies} pennies')


