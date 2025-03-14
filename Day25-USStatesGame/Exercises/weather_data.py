import csv

PATH = "./Day25-USStatesGame/weather_data.csv"

# with open(PATH) as data_file:
#     data_list = data_file.readlines()
#     print(data_list)

# with open(PATH) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

# data = pandas.read_csv(PATH)
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"] .to_list()
# print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp)
# print(monday.temp[0])

data_dict = {
    "students": ["Amy", " James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("./Day25-USStatesGame/new_data.csv")
# print(data)