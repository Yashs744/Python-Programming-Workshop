## Random Number Guessing Game
# Guess a number b/w 1 - 99

import random
n = random.randint(1, 99)

while True:
    print()
    guess = int(input("Enter a number from 1 to 99: "))
    if guess < n:
        print ("Guess is Low")
    elif guess > n:
        print ("Guess is High")
    else:
        break

print ("You Guessed It!")
print ()
