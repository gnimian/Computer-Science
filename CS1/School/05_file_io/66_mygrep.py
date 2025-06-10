#grep i 46_flowers.txt (this prints the lines that contain the letter i)
#grep ns 46_flowers.txt
#python3 mygrep.py r flowrers.txt

import sys
a=str(sys.argv[1])
b=sys.argv[2]
with open(b) as f:
    c=f.readlines()
    for line in c:
        if a in line:
            print(line, end='')
        