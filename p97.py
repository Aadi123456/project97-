import random
print('Number Guessing Game')
randomNumber=random.randint(1,9)

chances = 0

print('Guess a number(between 1 and 9):')

while chances < 5:

guess=int(input('Enter a Number:-'))

    if guess == randomNumber:
        print("Congratulations You Won!!!")
        break
    
    elif guess < randomNumber:
        print('Your guess was too low: Guess a number high than', guess)

    else:
        print('Your guess was too high: Guess a number lower than', guess)

    chances +=1

if not chances < 5:
    print('You Lose ! THE NUMBER IS ',randomNumber )