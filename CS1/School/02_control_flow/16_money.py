total=0.01
day=1
for i in range(1,31):
    total=total*2
    day=day+1

print(f'After {day} days you made ${total:,.2f}')
