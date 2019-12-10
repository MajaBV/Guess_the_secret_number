secret = 12

guess = int(input("Guess the number between 1 and 50: "))

if guess == secret:
    print("Congratulations! You guessed the secret number.")
else:
    print("Wrong number. Better luck next time.")
