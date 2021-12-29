import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
# student_data_frame = pandas.DataFrame(student_dict)
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

"""
or 
for letter in user_input:
    for (key, value) in code_dict.items():
        if letter is key:
            output.append(value)
"""

data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_df = pandas.DataFrame(data)

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter: row.code for (index, row) in letter_df.iterrows()}
print(new_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_code():
    # request input
    word = input("Enter a word\n").upper()
    try:
        # get output
        output = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry , only letters in the alphabet please")
        generate_code()
    else:
        print(output)


generate_code()
