import random
import hangman_art, hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display.append("_")

letters_guessed = []
repeated_letter = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if(guess in letters_guessed):
      print(f"You already have choosen the letter: {guess}.")
      repeated_letter = True
    else:
      letters_guessed.append(guess)
      repeated_letter = False

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong or if he choose a repeated letter.
    if guess not in chosen_word and not repeated_letter:
        print(f"Letter {guess} is not in the word. You lose 1 life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
