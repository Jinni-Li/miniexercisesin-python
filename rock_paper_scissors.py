import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# rules are:



#Write your code below this line 👇

# create  list with the possibilities
posibilities = [rock, paper, scissors]
  # select randomly in that list for the computer
while True:
  score = 0
  compscore = 0
  for _ in range (0,5):
    game = random.choice(posibilities)
      # print(scissors)
    choice= input("Which one are you gonna play? (rock, paper, scissors) \n")
    print("Computer choice: \n", game)
      
    if choice == "rock":
      if game == scissors:
        score = score + 1
        print("You win!")
      elif game == rock:
        print("Deat Head!")
      else:
        compscore = compscore + 1
        print("You lose :(")
    elif choice == "paper":
      if game == rock:
        score = score + 1
        print("You win!")
      elif game == paper:
        print("Deat Head!")
      else:
        compscore = compscore + 1
        print("You lose :(")
    elif choice == "scissors":
      if game == paper:
        score = score + 1
        print("You win!")
      elif game == scissors:
        print("Deat Head!")
      else:
        compscore = compscore + 1
        print("You lose :(")
  
  print("Your score:", score,"\nComputer score:", compscore)
  if compscore < score:
    print("Congrats! You're the final winner")
  elif compscore > score:
    print("Sadly you lose :(")
  else:
    print("Seems that we are having a tie here")
  again = input("Wanna play it again? (Yes/No)/n")
  if again.lower() != "yes":
    break