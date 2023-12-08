import random

def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_again():
    while True:
        user_input = input("Do you want to play again? (yes/no): ").lower()
        if user_input in ["yes", "no"]:
            return user_input == "yes"
        else:
            print("Invalid choice. Please enter yes or no.")

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        print(f"You chose {user_choice}")
        
        computer_choice = get_computer_choice()
        print(f"The computer chose {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            user_score += 1
            print("You win!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins!")
        else:
            print("It's a tie!")

        if not play_again():
            break

    print(f"Final score: You - {user_score}, Computer - {computer_score}")

if __name__ == "__main__":
    main()