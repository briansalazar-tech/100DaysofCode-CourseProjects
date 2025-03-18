# numbers = [1, 2, 3]
# new_numbers = [item + 1 for item in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [item * 2 for item in range(1, 5)]
# print(new_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list = [name.upper() for name in names if len(name) > 5]
# print(new_list)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# print(numbers)
# result = [number for number in numbers if number % 2 == 0]
# print(result)

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)

# passing_students = {student: score for (student, score) in student_scores.items() if score > 60}
# print(passing_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# split_sentence = sentence.split(" ")
# print(split_sentence)

# result = {word: len(word) for word in split_sentence}
# print(result)


# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:((temp * 9 / 5) + 34) for (day, temp) in weather_c.items()}
# print(weather_f)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Loop through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

# import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# for (key, value) in student_data_frame.items():
#     print(key)

# for (index, row) in student_data_frame.iterrows():
#     print(row.score)