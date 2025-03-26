# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# try:
#     file = open("./Day30-PasswordManager2.0/a_file.txt")
#     a_dictionary = {"Key": 1}
#     value = a_dictionary["Key2"]
# except FileNotFoundError:
#     file = open("./Day30-PasswordManager2.0/a_file.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# #Execute if no except block entered
# else:
#     content = file.read()
#     print(content)
# # Runs no matter what happens
# finally:
#     file.close()
#     print("File was closed")
#     # Create your own exception
#     raise TypeError("This is an error that I made up")

# # KeyError
# try:
#     a_dictionary = {"Key": 1}
#     value = a_dictionary["Key2"]
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")

# # IndexError
# fruit_list = ["apple", "bannana", "pear"]
# fruit = fruit_list[4]

# # TypeError
# text = "abc"
# print(text + 5)

# height = float(input("Height: "))
# weight = int(input("WeightL "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3 metters") # Useful for catching logical errors

# bmi = weight / height ** 2
# print(bmi)

# CHallenge 1
# fruits = ["Apple", "Pear", "Orange"]

# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except:
#         print("Fruit pie")

# make_pie(4)


# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]


# def count_likes(posts):
    
#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
#         except:
#             total_likes += 0
#     return total_likes


# print(count_likes(facebook_posts))

