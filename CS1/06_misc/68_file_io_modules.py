import sys

w=int(sys.argv[1])
with open(sys.argv[2]) as f:
    reading = True
    while reading:
        s=''
        for x in range(w):
            c=f.read(1)
            if not c:
                reading = False
            s=s+c
            if c == '\n':
                print(c, end='')
        print(s)


        if not reading:
            break