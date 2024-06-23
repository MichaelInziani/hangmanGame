#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'The chosen word is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display.append("_")
    #display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed
    if "_" not in display:
        end_of_game = True
        print("You win")


