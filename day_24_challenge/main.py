#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# read starting letter
with open("./Input/Letters/starting_letter.txt") as letter:
    origin_string = letter.read()

# get list of names
with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.read().split()

# for each name in list of names add a modified letter
mod_strings = {}
for n in names:
    mod_strings[n] = origin_string.replace("[name]", f"{n}")

# for each modified letter in the array create & write a new file in ReadyToSend
for s in mod_strings:
    with open(f"./Output/ReadyToSend/letter_to_{s}.txt", mode="w") as send_letter:
        send_letter.write(mod_strings[s])



