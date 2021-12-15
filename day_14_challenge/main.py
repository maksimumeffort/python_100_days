

# import the file containing art
import art 
# display art
print(art.logo)
# import random module
from random import randint, choice
# import game data
from game_data import data
        
# both celebrities cannot be identical

def generate_dif(celeb_a):
    celeb = choice(data)
    while celeb_a["follower_count"] == celeb["follower_count"]:
        celeb = choice(data)
    return celeb

# function that uses follower count to make comparison between A and B

def check_answer(guess, a_followers, b_followers):
  """take user's guess and follower counts and returns if got it right"""
  if a_followers["follower_count"] > b_followers["follower_count"]:
    return guess == "a"
  else:
    return guess == "b"  
    
# create a variable equal to a randomly generated entry from data list
  # assign random celebrities to variables A and B
is_game_over = False  
# use an array for variables?
# variables = [var_a, var_b]

# create a score counter keeping track of all correct answers
total_score = 0

while not is_game_over:
    if 'var_a' in locals():
        var_a = var_b
        #clear()
        print(f"You're right! Current score: {total_score}")
    else:
        var_a = choice(data)
    var_b = generate_dif(var_a)

    # print celebrities information: name, description, country

    print(f'Compare A: {var_a["name"]}, a {var_a["description"]}, from {var_a["country"]}')

    print(art.vs)

    print(f'Against B: {var_b["name"]}, a {var_b["description"]}, from {var_b["country"]}')

    # ask who has more followers and use input to compare followers

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # assign answer to the correct variable
    # carry out comparison function
    
    if check_answer(answer, var_a, var_b):
        total_score += 1  
    else:
        is_game_over = True
        print(f"Sorry, that's wrong. Final score: {total_score}")
        
        


