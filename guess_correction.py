import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Initialize the number of guesses
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I've selected a random number between 1 and 10. Try to guess it.")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < random_number:
            print("Too low! Try a higher number.")
        elif user_guess > random_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")

print("Thanks for playing!")
