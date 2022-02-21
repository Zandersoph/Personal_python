import random
def Guess_game(x):
    rand_number = random.randint(1, x)
    guess = 0
    tries = 0
    while guess != rand_number:
        guess = int(input("Enter you Guess: \n"))
        if guess > rand_number:
            print("Sorry, Guess again. Too high!")
            tries += 1
        elif guess < rand_number:
            print("Sorry, Guess again. Too low!")
            tries += 1
    print("Yay! You guessed the number!!")
    print(f"It took you {tries + 1} attempts to guess the number.")


Guess_game(20)
