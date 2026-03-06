import random
L=['cower','prevent','appoint','trait','continuous','fastidious','honest','pop','chip','congress','ensure','executive','pitch','realism','regular','soap','retreat','delete','terms','lose','eternal','creep','expansion','development','agenda','tie','question','communication','thinker','contain','album','taxi','despise','stamp','half','neighborhood','lodge','hunter','passive','bomb','team','enfix','contract','franchise','drill','understanding','structure','trade','pavement','systematic','writer','hardship','water','rhetoric','aid','permanent','complex','pilot','contradiction','case','error','anniversary','unpleasant','stain','cause','seize','breeze','lemon','patrol','omission','effective','apparatus','stake','empire','relief','default','excavation','nightmare','norm','clearance','countryside','nationalism','accountant','eat','dignity','feedback','substitute','lamb','poem','rest','sock','exotic','goalkeeper','glow','dash','loose','peanut','pier','dialogue','hello']
word=random.choice(L)
leng=list('_'*len(word))
count=0
picked=''
ret=''
while '_' in leng:
    a=0
    leng=list(leng)
    print('Please guess a letter')
    print(f'Already picked: {picked}')
    print(''.join(leng))
    inp=input('letter: ')
    inp=inp.lower()
    word=list(word)
    if inp in picked:
            print('You have already guessed this letter, plese choose another one')
            print()
            continue
    for i in range(len(word)):
        if inp==word[i] and a==0:
            print()
            print(f'{inp} is in the word!')
            a+=1
            leng[i]=inp
            ret=leng.copy()
            ret=''.join(ret)
            picked+=inp
        elif inp==word[i] and a!=0:
            leng[i]=inp
            ret=leng.copy()
            ret=''.join(ret)
    if a==0:
        print()
        print(f'Sorry, "{inp}" is not in the word')
        picked+=inp
    count+=1
    print(ret)
    print()
    print()
print(''.join(word))
print(f'you have guessed the word in {count} guesses')

'''
words=['']
secret=random.choice(words)
picekd=''
dashes=list('-'*len(secret))
count=0
while '-' in dashes:
    for c in dashes:
        print(c,end='')
    print()
    print()
    guess=input('guess a letter: ')
    guess=guess.lower()
    count+=1
    if guess in secret:
    print('Hurray you found a letter!)
    for x in range(len(secret)):
        if secret[x] == guess:
            dashes[x] = guess
    else:
        print(f'Sorry, "{guess}" is not in the word')
        picked = picked + guess
    print(f'Already picked: {picked}')
print (secret)
print(f'Well done you solved it in {count} guesses')
'''
