'''
word='hello'
for x in range(len(word)-1,-1,-1):
    print(word[x])
'''

word=input('enter a word: ')
nw=''
for letter in range(len(word)-1,-1,-1):
    nw+=(word[letter])
if nw==word:
    print('this is a palindrome')
else:
    print('this is not a palindrome')
'''
rev=''
for x in range(len(word)):
    let=word[len(word)-1-x]
    rev=rev+let
    print(rev)
'''
'''
rev=''
for letter in word:
    rev=letter+rev
    print(rev)
'''
