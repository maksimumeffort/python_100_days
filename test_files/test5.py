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
player_choice = options[num_choice]
#bot_choice = random.choice(options)
bot_choice = options[num_choice]

print(player_choice)
print(bot_choice)

# combinations
'''
rock > scissors
paper > rock
scissors > paper
'''
if player_choice == rock:
  if bot_choice == rock:
    print('draw')
  if bot_choice == scissors: 
    print('you win')
  else:
    print('you lose')
if player_choice == scissors:
  if bot_choice == scissors:
    print('draw')
  if bot_choice == paper: 
    print('you win')
  else:
    print('you lose')
if player_choice == paper:
  if bot_choice == paper:
    print('draw')
  if bot_choice == rock: 
    print('you win')
  else:
    print('you lose') 

