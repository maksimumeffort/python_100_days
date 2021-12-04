student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# can't use max() or min()
max = 0

for score in student_heights:
    if score > max:
        max = score

print(max)