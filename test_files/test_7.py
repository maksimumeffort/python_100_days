#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f',  'E']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_letters = ''
random_numbers = ''
random_symbols = ''

for l in range(0, nr_letters):
    rand_let_index = random.randrange(len(letters))
    random_letters +=(letters[rand_let_index])

for s in range(0, nr_symbols):
    rand_sym_index = random.randrange(len(symbols))
    random_symbols +=(symbols[rand_sym_index])

for n in range(0, nr_numbers):
    rand_num_index = random.randrange(len(numbers))
    random_numbers +=(numbers[rand_num_index])

password = random_letters + random_symbols + random_numbers

print(password)

'''
or

password = ''

for l in range(0, nr_letters):
    password += random.choice(letters)

for s in range(0, nr_symbols):
    password += random.choice(symbols)

for n in range(0, nr_numbers):
    password += random.choice(numbers)

'''

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

chars = list(password) # converts into list of characters
random.shuffle(chars) # shuffle characters within the list
randomized_password = ''.join(chars)

print(randomized_password)
