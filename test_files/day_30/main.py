# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_exist"]

# IndexError
# list = [1,2,3]
# number = list[4]

# TypeError
# text = "abc"
# print(text + 5)


# try (might cause exception) / except (if exception happened) / else (if no exception) / finally (no matter what)

# try:
#     file = open("a_file.txt")
#     dict = {"key": "value"}
#     print(dict["key"])
# except FileNotFoundError:
#     open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} exists")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

