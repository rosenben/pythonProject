# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

n = random.randint(1, 99)
guess = int(input("Enter an integer from 1 to 99: "))
max_guesses = 10
num_guesses = 1
while n != guess and num_guesses < max_guesses:
    print('You have %d guesses left' % (max_guesses - num_guesses))
    num_guesses = num_guesses + 1
    if guess < n:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))

if n == guess:
    print('you guessed it in %d guesses'% num_guesses)
else:
    print('You ran out of guesses.The number was ')
    print(n)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
