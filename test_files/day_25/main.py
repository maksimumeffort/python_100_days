
# with open("weather_data.csv") as weather_d:
#     data = weather_d.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temp = int(row[1])
#             temperatures.append(temp)
#
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(type(data))

# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # Get data in columns
#
# list = data["temp"].to_list()
# average = sum(list) / len(list)
# # print(average)
# #
# # '''
# # or
# # data["temp].mean() # in pandas documentation
# # '''
# #
# # # maximum value
# max = data["temp"].max()
# # print(max)
# # print(data.temp)
#
# # get data in Rows
# # print(data[data.temp == "Monday"])
# # print(data[data.temp == max])
#
# monday = data[data.day == "Monday"]
# # convert to Fahrenheit: °F =°C * 1.8000 + 32.00
# monday_temp_f = int(monday.temp) * 1.8000 + 32
# # print(monday_temp_f)
#
# # create dataframe from scratch
# data_dict = {
#     "students": ["amy", "james", "john"],
#     "scores": [76, 56, 65]
# }
#
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# new_data.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# find out the population of each color of squirrel ("Gray," "Cinnamon" or "Black")

grey_list_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_list_count)

red_list_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_list_count)

black_list_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_list_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_list_count, red_list_count, black_list_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("list_counts.csv")

"""
or
list = data["Primary Fur Color"].to_list()
# set up variables for each color
gray = 0
cinnamon = 0
black = 0

# loop through the list and update count for each color
for l in list:
    if l == "Gray":
        gray += 1
    elif l == "Cinnamon":
        cinnamon += 1
    elif l == "Black":
        black += 1

print(f"Gray: {gray}, Cinnamon: {cinnamon}, Black: {black}")




# print(f"gray: {gray.count()}")

# cinnamon = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
# print(f"gray: {cinnamon.count()}")
#
# black = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
# print(f"gray: {black.count()}")
"""
