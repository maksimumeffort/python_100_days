#Guess the number game#

#chooisng random number
import random
rand_num = random.randint(1, 100)

#print(f'Hint: it\'s {rand_num}')

print('Welcome to the number guessing game')
print('I\'m thinking of a number between 1 and 100.')

# set difficulty

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5
else:
    print("not available")

print(f"You have {attempts} attempts remaining to guess the number.")


def high_low(num):
    if num < rand_num:
        print("Too low")
    elif num > rand_num:
        print("Too high")

is_guess_right = False

while attempts > 0 and not is_guess_right:
    guess = int(input("Make a guess: "))
    if guess == rand_num:
        print(f"You got it! The answer was {rand_num}.")
        is_guess_right = True
    else:
        attempts -= 1
        high_low(guess)
        if attempts >= 1:
            print(f"You have {attempts} attempts remaining to guess the number.")

if not is_guess_right:
    print("You've run out of guesses, you lose.")
    