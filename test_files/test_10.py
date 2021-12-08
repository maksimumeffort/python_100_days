programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#retrieving items in dictionary
#print(programming_dictionary["Bug"])

#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary)

#creating new dictionary
empty_dictionary = {}

#wipe an existing dictionary
# useful for wiping out stats/ scores
'''programming_dictionary = {}
print(programming_dictionary'''

#edit an item in dictionary
programming_dictionary["Bug"] = "moth in computer"
#print(programming_dictionary)

#loop through dictionary
for key in programming_dictionary:
  '''#only prints out keys
  print(key)
  #only prints out values
  print(programming_dictionary[key])'''

##################################################

# Nesting
  # ordinary dictionary
capitals = {
  "france" :"paris",
  "geramany" :"berlin",
}

cities_visited = {
  "Paris": "Culture capital",
  "Calais": "Meditarranean city",
  "Marseille": "Fishing Port"
}
  
travel_log = {
  # nested list in dictionary
  "Germany" : ["Berlin", "Hanburg", "Munich"],
  # nested dictionary in dictionary
  "UK" : {"cities_visited": ["London", "Cardiff", "Ramsgate", "Bristol"]},
  # nested dictionary in dictionary inside dictionary
  "France" : {
    "cities": {
      "Paris": "Culture capital",
      "Calais": "Meditarranean city",
      "Marseille": "Fishing Port"
    }
  }
}
# print(travel_log["Germany"])
# print(travel_log["UK"]["cities_visited"])
# print(travel_log["France"]["cities"]["Paris"])

  # nesting dictionary in a list
gym_log = [ 
  {
    "day": "Chest", 
    "exercises": ["Bench Press", "Dumbell Flys"], 
    "total_time": 45
  },
  {
    "day": "Arms", 
    "exercises": ["Hammer Curls", "Chinups"], 
    "total_time": 30
  }
]

def add_new_log(day_type, exercise_list, log_time):
    gym_log.append(
        {
            "day": day_type, 
            "exercises": exercise_list, 
            "total_time": log_time 
        }
    )
'''
    or 
    new_log = {}
    new_log["day"] = day_type
    new_log["exercises"] = exercise_list
    new_log["total_time"] = log_time
    gym_log.append(new_log)
'''
