while True:
    sen=input('enter sentence: ')
    sen=sen.strip()
    a=0
    for words in range(len(sen)):
        if sen[words]==' ' and sen[words+1]!=' ':
            a+=1
    print(a+1)

'''
print('searching start of words')
wor=1
for i in range (len(sen)-1):
    if sen[i] == ' ' and sen[i+1] != ' ':
        wor=wor+1
print(wor)
'''





'''
sen=input('enter sentence: ')
sen= sen.strip()
wor=1
for let in sen:
    if let == ' ':
        wor=wor+1
print(wor)
'''
'''
for i in range (len(sen)):
    if sen[i]== ' ':
        wor=wor+1 #wor+=1
print(wor)
'''





'''
sen=input('enter sentence: ').strip()
print('searching end of words')
wor=1
lastlet=' '
for let in sen:
    print(f'"{lastlet}"   "{let}"')
    if lastlet != ' ' and let == ' ':
        wor=wor+1
        print('found end of word')
    lastlet=let
print(wor)
'''

'''
print()
#alternate loop solution
#also searching for end of word
print('searching end of words')
wod=1
if sen == '':
    print(0)
else:
    for i in range(1,len(sen)):
        #print(f'"{sen[i-1]}"   "{sen[i]}"')
        if sen[i] == ' ' and sen[i-1] != ' ':
            wor = wor + 1
            #print('found end of word')
    print(wor)
'''
