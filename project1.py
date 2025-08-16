import random
random_number = random.randint(1,101)
user_guess = int(input("Guess the number from 1 to 100: "))
while random_number != user_guess:
    if random_number > user_guess:
        print("higher.")
    elif random_number < user_guess:
        print("lower.")
    user_guess = int(input("Try again or type 'quit' to exit: "))
if random_number == user_guess:
    print("Correct.")
