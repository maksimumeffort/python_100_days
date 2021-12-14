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
    
# create a variable equal to a randomly generated entry from data list
  # assign random celebrities to variables A and B

var_a = generate_celeb()
var_b = generate_dif(var_a)

compare_followers(var_a, var_b)

# print celebrities information: name, description, country

print(f'Compare A: {var_a["name"]}, a {var_a["description"]}, from {var_a["country"]}')

print(art.vs)

print(f'Against B: {var_b["name"]}, a {var_b["description"]}, from {var_b["country"]}')



# create a score counter keeping track of all correct answers

total_score = 0


# if guessed correctly
  # random varaible from previous game assigned as variable A against which new comparison made
  # counter goes up by 1
  #clear()
  # wining message
  # display current score


# if guessed wrong
  # losing message
  # print final score

