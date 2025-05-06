'''
head -n 3 46_flowers.txt
python3 65_myhead.py 3 46_flowers.txt 
#these two line are the same 
'''
import sys
#usage python myhead.py 3 file.txt
#print the first n lines of file 

fname=sys.argv[2]
lcount=int(sys.argv[1])

with open(fname) as f:
    L=f.readlines()
    for x in range(0, lcount):
        print(L[x], end='')

print('-------------------------')

with open(fname, 'r') as f:
    L=f.readlines()[:lcount]#slice
    for line in L:
        print(line, end='')
