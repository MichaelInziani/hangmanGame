#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'The chosen word is {chosen_word}.')

#Create an empty List called display.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append("_")
    #display += chosen_word

guess = input("Guess a letter: ").lower()

#Loop through each position in the chosen_word;
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
#Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)