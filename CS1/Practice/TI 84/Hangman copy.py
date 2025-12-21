import random

bank = ["starfruit", "hazelnut", "cucumber", "mango", "potato", "zucchini", "blackberry", "fig", "balsa", "parsley", "eggplant", "lettuce", "brussels", "celery", "currant", "asparagus", "curry", "rosemary", "carrot", "lemon", "basil", "cumin", "melon", "cauliflower", "tomato", "pistachio", "oak", "nutmeg", "oregano", "corn", "brazilnut", "broccolini", "cantaloupe", "apricot", "mint", "sweetpotato", "tangerine", "greenbean", "kiwi", "peanut", "maple", "broccoli", "chard", "mustard", "plum", "mushroom", "teak", "bamboo", "garlic", "onion", "date", "macadamia", "mustard", "clove", "blueberry", "mandarin", "leek", "cherry", "pine", "almond", "cinnamon", "artichoke", "birch", "radish", "parsnip", "cashew", "chilipepper", "rosewood", "jalapeno", "pumpkin", "chili", "walnut", "orange", "strawberry", "pineapple", "bellpepper", "grapefruit", "paprika", "cherrywood", "peach", "ginger", "lime", "persimmon", "spinach", "willow", "raspberry", "cedar", "beetroot", "turnip", "saffron", "collard", "grape", "watermelon", "jackfruit", "vanilla", "nectar", "banana", "apple", "papaya", "kumquat"]

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print('Welcome to Hangman')
print()

word = random.choice(bank)
separate = list(word)
sepunder = list('_' * len(word))
wrong = 0
count = 0
guessed = []

while wrong < 7 and ('_' in sepunder):
    underscore = ''.join(sepunder)
    print('Word: ' + underscore)
    left = 7 - wrong
    print(str(left) + ' guesses left')
    
    # Display already guessed letters (all guessed letters, no duplicates)
    if guessed:
        g = ', '.join(guessed)
        print("Already guessed: " + g)
    else:
        print("Already guessed: ")
    
    # Display remaining letters
    f = ', '.join(letter)
    print("Letters you can still guess: " + f)
    
    b = input('Please guess a letter: ')
    b = b.lower()
    
    if b in guessed:
        print("You have already guessed " + b + ", please guess a different letter")
        continue
    
    if b in separate:
        print("Nice! " + b + " is in the word")
        for i in range(len(separate)):
            if separate[i] == b:
                sepunder[i] = b
    else:
        print('Sorry, ' + b + ' is not in the word')
        wrong += 1
    
    count += 1
    guessed.append(b)
    if b in letter:
        letter.remove(b)

if wrong == 7:
    print('Sorry, you lose. The word was ' + word + '.')
else:
    print('Good job! You guessed the word in ' + str(count) + ' tries')