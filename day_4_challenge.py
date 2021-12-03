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

#Write your code below this line 👇
import random

options = [rock, paper, scissors]

num_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if num_choice >= 3 or num_choice < 0:
  print("invalid number. you lose")
else:
  player_choice = options[num_choice]
  bot_choice = random.choice(options)

  print(player_choice)
  print(bot_choice)

  # combinations
  '''
  rock(0) > scissors(2)
  paper(1) > rock(0)
  scissors(2) > paper(1)
  '''
  if player_choice == rock:
    if bot_choice == rock:
      print('draw')
    elif bot_choice == scissors: 
      print('you win')
    else:
      print('you lose')
  if player_choice == scissors:
    if bot_choice == scissors:
      print('draw')
    elif bot_choice == paper: 
      print('you win')
    else:
      print('you lose')
  if player_choice == paper:
    if bot_choice == paper:
      print('draw')
    elif bot_choice == rock: 
      print('you win')
    else:
      print('you lose') 

