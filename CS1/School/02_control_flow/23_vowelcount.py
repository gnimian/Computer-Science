sen=input('enter sentence: ')
b=sen.lower()
x=('a','e','i','o','u')
a=0
for vow in range(len(b)):
    if b[vow] in x:
        a+=1
    else:
        continue
print(f'there are {a} vowels in "{sen}"')

'''
sen=input('enter sentence: ')
vowcount=0
for let in sen:
    let=let.lower
    if let in 'aeiou':
        vowcount=vowcount+1
print(f'there are {vowcount} vowels in "{sen}"')
'''
'''
vowcount=0
for x in range (len(sen)):
    let=sen[x].lower
    if let in 'aeiou':
        vowcount=vowcount+1
'''
