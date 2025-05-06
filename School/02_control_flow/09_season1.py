season=input('enter the month (3 letters): ')
if season=='jan' or season=='feb' or season=='dec':
    print('season is winter')
elif season=='mar' or season=='apr' or season=='may':
    print('season is spring')
elif season=='jun' or season=='jul' or season=='aug':
    print('season is summer')
elif season=='sep' or season=='oct' or season=='nov':
    print('season is fall')
else:
    print('this is not a month')
