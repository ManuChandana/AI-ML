import random
def minimax(player_move, computer_move):
    if player_move == computer_move:
        return 0
    if (player_move == 'rock' and computer_move == 'scissors') or \
       (player_move == 'scissors' and computer_move == 'paper') or \
       (player_move == 'paper' and computer_move == 'rock'):
        return 1
    return -1
def play_game():
    choices = ['rock', 'paper', 'scissors']
    while True:
        player_move = input("Enter your move (rock/paper/scissors): ").lower()
        if player_move not in choices:
            print("Invalid move. Please choose rock, paper, or scissors.")
            continue      
        computer_move = random.choice(choices)
        print(f"Computer chose {computer_move}")
        result = minimax(player_move, computer_move)
        if result == 1:
            print("You win!")
        elif result == -1:
            print("Computer wins!")
        else:
            print("It's a draw!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
play_game()
