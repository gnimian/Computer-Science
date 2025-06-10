while True:
    let=input('please input an even letter word: ')
    if len(let)%2==0:
        x=0
        final=''
        for i in range(0,len(let),2):
            a=let[i]
            b=let[i+1]
            a,b=b,a
            final+=a+b
        print(final)
    else:
        print(f'"{let}" is not an even letter word')

'''
word=input('enter word: ')
shuf=''
for x in range(0.len(word),2):
    pair=word[x:x+2]
    revpair=pair[;;-1]
    shuf=shuf+revpair
print(shuf)

#alternate better solution
shuf=''
evens=word[:-1:2]
odds=word[1::2]
for x in range(len(word)//2)
    shuf = shut+odds[x] + evens[x]
print(shuf)

#alternate solution even better
shuf=''
for x in range(0, len(word), 2):
    shuf = shuf + word[x+1] + word[x]
print(shuf)
'''