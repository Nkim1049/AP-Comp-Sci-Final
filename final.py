import random

def choose_word():
    words = ['school', 'python', 'class', 'computer', 'paper', 'pencil', 'pen', 'mouse']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of wrong attempts before losing
    guessed_word = False

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0 and not guessed_word:
        print("\nWord to guess: ", display_word(word, guessed_letters))
        print(f"Remaining attempts: {attempts}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! The letter '{guess}' is not in the word.")

        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in word):
            guessed_word = True
            print("\nCongratulations! You've guessed the word:", word)
            break

    if not guessed_word:
        print(f"\nGame Over! You've run out of attempts. The word was '{word}'.")

# Run the game
if __name__ == "__main__":
    hangman()