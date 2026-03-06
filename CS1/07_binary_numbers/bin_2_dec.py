while True:
    x=list(input('please enter a binary number: '))
    a=0
    x.reverse()
    for i in range(len(x)):
        if x[i]=='1':
            a+=2**i
    print('the decimal number is:',a)

 