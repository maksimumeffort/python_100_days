from random import choice

data_dict = [{'French': 'vers', 'English': 'towards'},
        {'French': 'minutes', 'English': 'minutes'},
        {'French': 'demandé', 'English': 'request'},
        {'French': 'chambre', 'English': 'bedroom'},
        {'French': 'mis', 'English': 'placed'},
        {'French': 'belle', 'English': 'beautiful'},
        {'French': 'droit', 'English': 'law'},
        {'French': 'aimerais', 'English': 'would like to'},
        {'French': "aujourd'hui", 'English': 'today'},
        {'French': 'mari', 'English': 'husband'},
        {'French': 'cause', 'English': 'cause'},
        {'French': 'enfin', 'English': 'finally'},
        {'French': 'espère', 'English': 'hope'},
        {'French': 'eau', 'English': 'water'},
        {'French': 'attendez', 'English': 'Wait'},
        {'French': 'parti', 'English': 'left'},
        {'French': 'nouvelle', 'English': 'new'},
        {'French': 'boulot', 'English': 'job'},
        {'French': 'arrêter', 'English': 'Stop'},
        {'French': 'dirait', 'English': 'would say'}]

word_pair = choice(data_dict)
print(word_pair)
data_dict.remove(word_pair) # works because it's a list
