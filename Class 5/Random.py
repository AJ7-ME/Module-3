import random
playing = True
num = str(random.randint(10, 20))
print("I will generate a random number between 10 and 20. Can you guess it one digit at a time?")
while playing:
    guess = input("Give me your best guess: ")
    if num == guess:
        print("Congratulations! You guessed it right.")
        playing = False
    else:
        print("Wrong guess. Try again!")