import random
# Initialize scores
user_score = 0
computer_score = 0

while True:
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ")
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    print(f"Score:You {user_score}-{computer_score} Computer")
    play_again = input("Do you want to play again? yes/no: ")
    if play_again != "yes":
        break
print("Thanks for playing!")
