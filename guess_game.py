import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1-10): "))

    if guess == number:
        print("Correct! You win ")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")