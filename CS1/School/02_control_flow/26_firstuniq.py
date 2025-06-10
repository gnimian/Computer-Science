word=input('')
stor=''
for x in word:
    a=0
    for i in word:
        if x==i:
            a+=1
            if a>1:
                break
    if a==1:
        print(x)
        break



'''
set count of that letter to 0
[Iterate over each letter again check if the letters match
if they do, then increment]
check if your count is one

s=input()
print(s)
print()
found=False
for c in s:
    if s.count(c) == 1:
        print(c, 'at', s.index(c). 'is first uniq char')
        found = True
        break
else:
    print('no uniq char in', s)






for let in s:
    count=0
    for char in s:
        if char == let:
            count+=1
            if count>1:
                break
    if count==1:
        print(c):
        break
'''
