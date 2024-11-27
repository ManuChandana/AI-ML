def minimax(low, high, depth, is_maximizing):
    if low > high:
        return 0
    mid = (low + high) // 2
    if is_maximizing:
        return minimax(mid + 1, high, depth + 1, False)
    else:
        return minimax(low, mid - 1, depth + 1, True)
def guess_number(low, high):
    guess = (low + high) // 2
    print(f"Computer's guess: {guess}")
    return guess
def play_game():
    low, high = 1, 100
    print("Guess the number game!")
    while True:
        guess = guess_number(low, high)
        feedback = input(f"Is your number {guess}? (high/low/correct): ").lower()
        if feedback == "correct":
            print("Computer guessed it right!")
            break
        elif feedback == "high":
            high = guess - 1
        elif feedback == "low":
            low = guess + 1
        else:
            print("Invalid input, please respond with 'high', 'low', or 'correct'.")

play_game()
