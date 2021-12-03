import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

name_count = len(names)

rand_index = random.randint(0, name_count)

#alternatively
rand_choice = random.choice(names)

#print(rand_index)

print(f'It is {names[rand_index]}\'s turn')

