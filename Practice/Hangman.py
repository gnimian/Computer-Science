import random
import os
words=["starfruit", "hazelnut", "cucumber", "mango", "potato", "zucchini", "blackberry", "fig", "balsa", "parsley", "eggplant", "lettuce", "brussels", "celery", "currant", "asparagus", "curry", "rosemary", "carrot", "lemon", "basil", "cumin", "melon", "cauliflower", "tomato", "pistachio", "oak", "nutmeg", "oregano", "corn", "brazilnut", "broccolini", "cantaloupe", "apricot", "mint", "sweetpotato", "tangerine", "greenbean", "kiwi", "peanut", "maple", "broccoli", "chard", "mustard", "plum", "mushroom", "teak", "bamboo", "garlic", "onion", "date", "macadamia", "mustard", "clove", "blueberry", "mandarin", "leek", "cherry", "pine", "almond", "cinnamon", "artichoke", "birch", "radish", "parsnip", "cashew", "chilipepper", "rosewood", "jalapeno", "pumpkin", "chili", "walnut", "orange", "strawberry", "pineapple", "bellpepper", "grapefruit", "paprika", "cherrywood", "peach", "ginger", "lime", "persimmon", "spinach", "willow", "raspberry", "cedar", "beetroot", "turnip", "saffron", "collard", "grape", "watermelon", "jackfruit", "vanilla", "nectar", "banana", "apple", "papaya", "kumquat"]
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print('Welcome to Hangman')
print()
def hangman():
    hang=''
    if a==0:
        for i in range (0,7):
            hang+='|\n'
    elif a==1:
        hang+='___________\n'
        hang+='|         |\n'
        for i in range (0,6):
            hang+='|\n'
    elif a==2:
        hang+='___________\n'
        hang+='|         |\n'
        hang+='|        ____\n'
        hang+='|       |    |\n'
        hang+='|       |____|\n'
        for i in range (0,3):
            hang+='|\n'
    elif a==3:
        hang+='___________\n'
        hang+='|         |\n'
        hang+='|        ____\n'
        hang+='|       |    |\n'
        hang+='|       |____|\n'
        hang+='|         |\n'
        hang+='|         |\n'
        hang+='|\n'
    elif a==4:
        hang+='___________\n'
        hang+='|         |\n'
        hang+='|        ____\n'
        hang+='|       |    |\n'
        hang+='|       |____|\n'
        hang+='|       --|\n'
        hang+='|         |\n'
        hang+='|\n'
    elif a==5:
        hang+='___________\n'
        hang+='|         |\n'
        hang+='|        ____\n'
        hang+='|       |    |\n'
        hang+='|       |____|\n'
        hang+='|       --|--\n'
        hang+='|         |\n'
        hang+='|\n'
    elif a==6:
        hang+='___________\n'
        hang+='|         |\n'
        hang+='|        ____\n'
        hang+='|       |    |\n'
        hang+='|       |____|\n'
        hang+='|       --|--\n'
        hang+='|         |\n'
        hang+='|        /\n'
    elif a==7:
        hang+='___________\n'
        hang+='|         |\n'
        hang+='|        ____\n'
        hang+='|       |    |\n'
        hang+='|       |____|\n'
        hang+='|       --|--\n'
        hang+='|         |\n'
        hang+='|        / \\ \n'
    return hang

word=random.choice(words)
separate=list(word)
guess=list('_'*len(word))
a=0
count=0
guessed=[]
already=''
while a<7 and ('_' in guess):
    c=''.join(guess)
    print(hangman())
    print(f'Word: {c}')
    print()
    d=7-a
    print(f'{d} guesses left')
    print()
    g=''
    for i in range(len(already)):
        if i!=len(already)-1:
            g=g+already[i]+', '
        else:
            g=g+already[i]
    print(f'Already guessed: {g}')
    print()
    e=''.join(letter)
    f=''
    for i in range(len(letter)):
        if i!=len(letter)-1:
            f=f+letter[i]+', '
        else:
            f=f+letter[i]
    print(f'Letters you can still guess: {f}')
    print()
    b=input('Please guess a letter: ')
    b=b.lower()
    if b in guessed:
        os.system('clear')
        print(f'You have already guessed {b}, please guess a different letter')
        print()
        continue
    if b in separate:
        os.system('clear')
        print(f'Nice! {b} is in the word')
        print()
        for i in range(len(separate)):
            if separate[i]==b:
                guess[i]=b
        
    else:
        os.system('clear')
        print(f'Sorry, {b} is not in the word')
        print()
        a+=1
    count+=1
    guessed.append(b)
    letter.remove(b)
    already+=b

if a==7:
    print(f'Sorry, you lose. The word was {word}.')
    print()
else:
    print(f'Good job! You guessed the letter in {count} tries')
    print()
    