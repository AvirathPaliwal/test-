import random

number = random.randrange(1,20)
guess = int(input("Enter any number: "))

while number!= guess :
    if guess < number:
        print("Too low")
        guess = int(input("Enter number again: "))