import random
import hangman_art
from hangman_words import word_list


words_list = word_list
chosen_word = random.choice(words_list)
word_length = len(chosen_word)

#intializing number of lives
end_of_game = False
lives = 6
#logo
print(hangman_art.logo)

guessed = []
# Create blanks
display = []
for _ in range(word_length):
    display += "_"

#checking to run loop or not
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("you have already guessed: ", guess)
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            guessed.append(guess)
    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        not_in_words = guess
        print(f"You guessed {not_in_words} ,that's not in words, you lose a life")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(hangman_art.stages[lives])
    print("lives left: ", lives)