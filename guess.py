## Random Number Guessing Game
# Guess a number b/w 1 - 99

import random
n = random.randint(1, 99)

guess = int(input("Enter a number from 1 to 99: "))

while n != guess:
    print()
    if guess < n:
        print ("Guess is Low")
        guess = int(input("Enter a number from 1 to 99: "))
    elif guess > n:
        print ("Guess is High")
        guess = int(input("Enter a number from 1 to 99: "))
    else:
        break

print ("You Guessed It!")
print ()