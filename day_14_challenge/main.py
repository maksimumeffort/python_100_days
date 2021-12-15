

# import the file containing art
import art 
# display art
print(art.logo)
# import random module
from random import randint
# import game data
from game_data import data

# generate random celebrity
        
def generate_celeb():
    rand_num = randint(0, len(data)-1)
    return data[rand_num]

# both celebrities cannot be identical

def generate_dif(celeb_a):
    rand_num = randint(0, len(data)-1)
    celeb = data[rand_num]
    if celeb_a["follower_count"] == celeb["follower_count"]:
        return generate_celeb()
    else:
        return celeb

# function that uses follower count to make comparison between A and B
def compare_followers(a, b):
    if a["follower_count"] > b["follower_count"]:
        return 1
    else:
        return 0

# function that keeps one of the variables from previous comparisson

#def keep_one():
    
    
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
        var_a = generate_celeb()
    var_b = generate_dif(var_a)

    # print celebrities information: name, description, country

    print(f'Compare A: {var_a["name"]}, a {var_a["description"]}, from {var_a["country"]}')

    print(art.vs)

    print(f'Against B: {var_b["name"]}, a {var_b["description"]}, from {var_b["country"]}')

    # ask who has more followers and use input to compare followers

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # assign answer to the correct variable
    # carry out comparison function
    if answer == "a":
        higher_lower = compare_followers(var_a, var_b)
    elif answer == "b":
        higher_lower = compare_followers(var_b, var_a)
    
    if higher_lower < 1:
        is_game_over = True
        print(f"Sorry, that's wrong. Final score: {total_score}")
    else:
        total_score += 1
        
        


