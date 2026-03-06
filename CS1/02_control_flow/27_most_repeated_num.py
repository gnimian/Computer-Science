'''
inp=input('')
for i in inp:
    for j in range(len(inp)+1):
        if i == j:
'''

'''
s=input()

count=1
longest=1
char=s[0] #assume longest seq starts at the beginning of string
for x in range(len(s)-1):
    if s[x]==s[x+1]:
        count+=1
        if count > longest:
            longest = count
            char=s[x]
    else:
        count=1
print(longest,char)
'''

'''
s=input()

x=1
count=1
longest=1
char=s[0] #assume longest seq starts at the beginning of string
while x<len(s)-1:
    if s[x]==s[x+1]:
        count+=1
        if count > longest:
            longest = count
            char=s[x]
    else:
        count=1
print(longest,char)
'''

