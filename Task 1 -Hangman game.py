import random

# Hangman stages (from 6 lives down to 0)
hangman_stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """
]

# Word lists by difficulty
easy_words = ["cat", "dog", "sun", "pen", "hat", "book", "car", "fish", "star", "tree"]
medium_words = ["python", "cricket", "church", "guitar", "school", "computer", "holiday", "friend", "garden", "football"]
hard_words = ["elephant", "butterfly", "keyboard", "mountain", "sunshine", "basketball", "bicycle", "rainbow", "friendship", "hangman"]

# Ask difficulty
print("Welcome to Haaannngggman!")
print("Choose difficulty: easy / medium / hard")
difficulty = input("Enter difficulty: ").lower()

if difficulty == "easy":
    word_list = easy_words
elif difficulty == "medium":
    word_list = medium_words
elif difficulty == "hard":
    word_list = hard_words
else:
    print("Invalid choice! Defaulting to medium.")
    word_list = medium_words

# Choose a random word
chosen_word = random.choice(word_list)

print("\nI have chosen a word for you to guess.")
print("Difficulty level:", difficulty)
print("ok..! ,Let's start..")

# Create blanks
display = ["_"] * len(chosen_word)
print(" ".join(display))

# Game setup
lives = 6
score = 0
game_over = False

# Game loop
while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        correct_guess = False
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess and display[position] == "_":
                display[position] = guess
                score += 10   # ✅ 10 points per correct letter
                correct_guess = True
        if correct_guess:
            print(f"✅ Good job! +10 points. Current score: {score}")
    else:
        lives -= 1
        print(f"❌ Wrong guess! You have {lives} lives left.")

    # Show hangman and progress
    print(hangman_stages[lives])
    print(" ".join(display))

    # Win condition
    if "_" not in display:
        bonus = lives * 5  # ✅ Bonus points for lives left
        score += bonus
        print(f"🎉 You win! The word was: {chosen_word}")
        print(f"🏆 Final Score: {score} (including {bonus} bonus points)")
        game_over = True

    # Lose condition
    if lives == 0:
        print(f"💀 You lost! The word was: {chosen_word}")
        print(f"Final Score: {score}")
        game_over = True
