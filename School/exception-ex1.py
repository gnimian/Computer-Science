try:
    #import coffee
    #print(4+'hi')
    #print(car)
    #print(1/0)
    L=[]
    #print(L[3])
    #f=open('sssssssssssss','r')

except ZeroDivisionError:
    print('**************************          Do not divide zero!         **************************')

except NameError:
    print('that variable does not exist. Check you code')

except IndexError:
    print('You went out of bounds')

except ModuleNotFoundError:
    print('that module is fake')

except Exception as e:
    print('some other error happened')
    print('the error which occured is:', type(e))
    print('the error message is', e)
    