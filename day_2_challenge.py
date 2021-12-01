#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#get input, convert to numbers
print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? \n$"))
tip = input("how much tip would you like to give? (%)\n")
split_num = int(input("how many people to split the bill?\n"))

# tip_as_percent = int(tip) / 100
# total_tip = bill * tip_as_percent
# total_bill = bill + total_tip
# bill_per_person = total_bill / split_num
# final_amount = round(bill_per_person, 2)


plus_tip = float("1." + tip)

# print(plus_tip)

how_much = (bill / split_num) * plus_tip

# print(how_much)

how_much_rounded = '%.2f' % round(how_much, 2)
# also can use "{:.2f}".format(how_much)

# print(how_much_rounded)

# message = f'Each person should pay ${final_amount}'
message = f'Each person should pay: ${how_much_rounded}'
print(message)



