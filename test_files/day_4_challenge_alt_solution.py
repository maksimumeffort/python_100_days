import random

options = ["rock", "paper", "scissors"]

num_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))


# player_choice = options[num_choice]
bot_choice = random.randint(0,2)


'''
rock(0) > scissors(2)
paper(1) > rock(0)
scissors(2) > paper(1)
'''

#check for outliers
if num_choice >= 3 or num_choice < 0:
    print("you typed invalid number. you lose.")
#rock v scissors
print(options[num_choice])
print(options[bot_choice])

if num_choice == 0 and bot_choice == 2:
    print('you win')
#scissors v rock
elif bot_choice == 0 and num_choice == 2:
    print('you lose')
#scissors v paper & paper v rock    
elif bot_choice > num_choice:
    print('you lose')
#paper v scissors & rock v paper
elif bot_choice < num_choice:
    print('you win')
else:
    print('it\'s a draw')


