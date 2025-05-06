import pickle
try:
    f=open('phonebook.data','rb')
    book = pickle.load(f)
    f.close
except:
    print('Error: no data (must be first time running this program, phonebook empty)')
    print('or phonebook may have been deleted')
    book={} #if file no exist make dict empty

def upper(x):
    x=x.list()
while True:
    inp=input('(A)dd/modify, (D)elete, (S)earch, (Q)uit: ')
    inp=inp.lower()
    if inp=='a':
        name=input('Enter name of person to add/modify: ')
        name=name.lower()
        number=input('Enter telephone #: ')
        book[name]=number
        print('Done')
        print()
    elif inp=='d':
        name=input('Enter the name of the person you want to delete: ')
        name=name.lower()
        if name.lower in book:
            print(f'{name} {book[name]} deleted!')
            book.pop(name)
            print()
        else:
            print(f'{name} not found')
            print()
    elif inp=='s':
        name=input('Enter name of person to search: ')
        name=name.lower()
        if name in book:
            print(f'the telephone number of {name} is {book[name]}')
            print()
        else:
            print(f'{name} not found')
            print()
    elif inp=='q':
        break
    else:
        print('please type a valid letter')
        print()

f2 = open('phonebook.data','wb')
pickle.dump(book, f2)
f2.close
