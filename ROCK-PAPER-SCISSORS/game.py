
import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        print("Invalid choice, please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    return 'computer'

def play_game():
    user_wins = 0
    computer_wins = 0
    round_limit = 5
    current_round = 1

    print(f"""Welcome to Rock-Paper-Scissors Game!!  
          Let's play {round_limit} rounds!""")
    while current_round <= round_limit:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            print("User wins this round!")
            user_wins += 1
        elif winner == 'computer':
            print("Computer wins this round!")
            computer_wins += 1
        else:
            print("It's a tie!")
        print(f"Score: User {user_wins} - Computer {computer_wins}")
        current_round += 1

    if user_wins > computer_wins:
        print("User wins the game!")
    elif computer_wins > user_wins:
        print("Computer wins the game!")
    else:
        print("It's a tie!")

def main():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        play_game()
        play_again = input("Do you want to play again? (yes/no) ")

if __name__ == "__main__":
    main()