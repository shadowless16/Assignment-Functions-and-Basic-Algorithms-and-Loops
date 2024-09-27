import random

def number_guessing_game():
    target_number = random.randint(1, 10)
    guess = None
    
    print("U are Welcome to the Number Guessing Game!")
    
    while guess != target_number:
        guess = int(input("Enter your guess: "))

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly.")

number_guessing_game()
