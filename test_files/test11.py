'''def format_name(f_name, l_name):
  if f_name == '' or l_name == '':
    # early return, will terminate function without running code below
    return
  format_first = f_name.title()
  format_last = l_name.title()

  # return keyword is important to get output
  return f'{format_first} {format_last}'
  # return tells program it's the last line of code, nothing after will run
  print("This will not print")
  

format_string = format_name(input("What is your first name?: "), input('What is your last name?: '))

print(format_string)'''

def is_leap(year):
  """checks if the year in the input is a leap year"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year_given, month_given):
  # DOCTSRING: """ <insert here> """
  # DOCSTRING: explains what the function does, has to go on the first line after function declared

  if month_given > 12 or month < 1:
      return "invalid input"
  
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if is_leap(year_given):
    month_days[1] = 29
    return month_days[month_given - 1]
  else:
    return month_days[month_given - 1]

'''
or
def days_in_month(year_given, month_given):
  non_leap_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year_given):
    return leap_month_days[month_given - 1]
  else:
    return non_leap_month_days[month_given - 1]
'''
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)