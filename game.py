import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def main():
    print("\nWelcome to the Rock-Paper-Scissors Game!")
    print("Instructions: Choose rock, paper, or scissors. The game will tell you who wins.")

    user_score = 0
    computer_score = 0

    while True:
        print("\nMake your choice:")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nScores: You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
