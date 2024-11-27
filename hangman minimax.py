import random
def get_word():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    return random.choice(words)
def play_game():
    word = get_word()
    guessed = ['_'] * len(word)
    tries = 6
    guessed_letters = []
    print("Welcome to Hangman!")
    while tries > 0:
        print(f"Word: {' '.join(guessed)}")
        print(f"Tries left: {tries}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            if "_" not in guessed:
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            tries -= 1
            print(f"Wrong guess! {tries} tries left.")
    else:
        print(f"Game over! The word was: {word}")
play_game()
