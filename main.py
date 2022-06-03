import random

userChoice = input("Enter your weapon(Rock, scissor, paper): ")
compChoice = ["Rock", "scissor", "paper"]
choice = random.choice(compChoice)
print(choice)
if userChoice == choice:
    print(f"Both players selected {userChoice}. It's a tie!")
elif userChoice == "Rock":
    if choice == "paper":
        print("Paper covers rock! You lose.")
    else:
        print("Rock smashes scissors! You win.")
elif userChoice == "paper":
    if choice == "rock":
        print("Paper covers rock! You win.")

    else:
        print("Scissors cuts paper! You lose!")
elif userChoice == "scissor":
    if choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
