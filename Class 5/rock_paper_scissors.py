while True:
    import random
    options = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors"):
        print("Rock crushes scissors and you win !.")
    elif (user_choice == "paper" and computer_choice == "rock"):
        print("Paper covers rock and you win !.")
    elif (user_choice == "scissors" and computer_choice == "paper"):
        print("Scissors cut paper and you win !.")
    elif user_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
    elif (computer_choice == "rock" and user_choice == "scissors"):
        print("Rock crushes scissors. Computer wins!")
    elif (computer_choice == "paper" and user_choice == "rock"):
        print("Paper covers rock. Computer wins!")
    elif (computer_choice == "scissors" and user_choice == "paper"):
        print("Scissors cut paper. Computer wins!")