import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess != number:
    print("Incorrect!")
else:
    print("Congratulations! You guessed the number.")
