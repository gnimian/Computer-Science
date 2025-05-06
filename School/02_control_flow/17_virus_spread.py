people=1
day=1
while True:
    people=people*2
    if people>= 8e9:
        break
    day=day+1
print(f'It will take {day} days until everyone is infected')


'''
infect=1
tot=0
day=1
print('\tDay\t\t\tinfect\t\t\ttotal')
while tot< 8e9:
    tot=tot+infect
    print(f'{day:>10} {infect:>24,}')
    infect=infect*2
    day=day+1
print(f'the total number of days {day-1}')
