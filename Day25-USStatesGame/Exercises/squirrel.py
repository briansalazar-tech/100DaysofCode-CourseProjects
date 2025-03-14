import pandas
# Create CSV with totals of each squirrel fur color 

data = pandas.read_csv("./Day25-USStatesGame/squirrel_data.csv")
gray = (data["Primary Fur Color"] == "Gray").sum()
red = (data["Primary Fur Color"] == "Cinnamon").sum()
black = (data["Primary Fur Color"] == "Black").sum()

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray, red, black],
}

df = pandas.DataFrame(data_dict)
print(df)

df.to_csv("./Day25-USStatesGame/squirrel_count.csv")