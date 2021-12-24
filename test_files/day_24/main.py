'''read file'''
with open("../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

'''write to the file'''
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

'''append to file'''
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

'''if opening a file in write mode & file doesn't exist, it will create the file from scratch'''
# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text.")
