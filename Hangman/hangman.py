import random
from words import words
import string
from hangman_visual import lives_visual

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the world
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters guessed by user

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("You have", lives, " lives left and you have used these letters: ",' '.join(used_letters))

        # what is current word from guessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual[lives])
        print("Current word: ",' '.join(word_list))

        user_letter = input("Guess a latter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives-=1
                print("Letter is not in word.")
                

        elif user_letter in used_letters:
            print("You have already used that character. Try again")

        else:
            print("Invalid character. Try again.")
    
    if lives == 0:
        print(lives_visual[lives])
        print("You died. The word was ", word)
    else:
        print("You guessed the word ", word)

hangman()





