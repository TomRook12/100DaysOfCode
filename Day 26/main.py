# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)
# range(1, 5)

# new_list = ["Alfa", "November", "Golf", "Echo", "Lima", "Alfa,]

# ---------------------------------------------------

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [num * num for num in numbers]

# Write your code 👆 above:

print(squared_numbers)

# ---------------------------------------------------

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [num for num in numbers if num % 2 == 0]

# Write your code 👆 above:

print(result)

# ---------------------------------------------------

with open("file1.txt", mode="r") as list1, open("file2.txt", mode="r") as list2:
    file_1_data = list1.readlines()
    file_2_data = list2.readlines()
    result = [int(num) for num in file_1_data if num in file_2_data]

# Write your code above 👆

print(result)

# ---------------------------------------------------

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

listy = sentence.split()
print(listy)

result = {word:len(word) for word in listy}

print(result)

# ---------------------------------------------------

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:temp_c * 9/5 + 32for (day, temp_c) in weather_c.items()}

print(weather_f)

# ---------------------------------------------------

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

#Loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)

#Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)