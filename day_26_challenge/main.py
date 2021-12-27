student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_df = pandas.DataFrame(data)

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter: row.code for (index, row) in letter_df.iterrows()}
print(new_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# request input
word = input("Type a name you want spelt out").upper()
# print(list(user_input))

# give output
output = [new_dict[letter] for letter in word]

"""
or 
for letter in user_input:
    for (key, value) in code_dict.items():
        if letter is key:
            output.append(value)
"""

print(output)
