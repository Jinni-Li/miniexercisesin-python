# HANGMAN

#Step 1:
# TODO-1 - create a words list
# TODO-2 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TODO-3 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-4 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#Step 2:

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#to find the position of the letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

######    ############   ##############   ######
#Step 3:

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

######## ############  #########  ###########
# Step 4:
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.




words = ["badbunny","pepe", "shakira", "gerardpiqué", "illojuan", "quevedo","badgyal"]
import random
chosen_word = random.choice(words)
#print("chosen_word:", chosen_word)

display=[]
length_word = len(chosen_word)
display = length_word* ["_"]
print("secret word:", display)

def find_characters(word, character):
    found = []
    last_index = -1
    while True:
        try:
            last_index = word.index(character, last_index+1)
        except ValueError:
            break
        else:
            found.append(last_index)
    return found

lives=6

while '_' in display and lives > 0:
    guess = input('Guess a letter: ')
    x = sum(char == guess for char in chosen_word)
    print("Times the letter appears in the word: ",x)
    if guess in chosen_word:
      position = find_characters(chosen_word,guess) 
      for i in range(0,len(position)):
        order=position[i]
        display[order] = guess
    else:
      lives=lives-1
      print("lives:", lives)
    print(stages[lives])
    print(display)
if lives == 0:
  print("Pal lobby tontito")
if '_' not in display: 
  print("Winner winner chicken dinner")






