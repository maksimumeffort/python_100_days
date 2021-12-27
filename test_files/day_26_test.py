code_dict = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}

user_input = input("Type a name you want spelt out").upper()

#output = [code for (letter, code) in code_dict.items() if letter in list(user_input)]

output = [code_dict[letter] for letter in user_input]

'''
or
for letter in user_input:
    output.append(code_dict[letter])


or
for letter in user_input:
    for (key, value) in code_dict.items():
        print(letter)
        if letter is key:
            output.append(value)
        print(output)
'''
        
print(output)