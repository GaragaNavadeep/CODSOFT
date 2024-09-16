import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You won!"
    else:
        return "You lost!"

def play_game():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock Paper Scissors Game")

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = winner(user_choice, computer_choice)
        print(result)

        if result == "You won!":
            user_score += 1
        elif result == "You lost!":
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
if __name__ == "__main__":
    play_game()
