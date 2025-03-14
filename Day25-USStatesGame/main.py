import turtle
import pandas
from datetime import datetime

# Get current date and time to append on CSV file name
now = datetime.now()
formated_date = now.strftime("%b-%d-%Y_%I.%M%p")

# Read data from US States CSV file
data = pandas.read_csv("./Day25-UsStatesGame/50_states.csv")

correct_guesses = 0
correct_states = []
all_states = data["state"].to_list()


def check_state_in_csv(state):
    """Checks to see if the value entered is in the CSV files. If it is, return the states coordinates"""
    if state in data.state.values:
        state = data[data.state == state]
        x = int(state.x.values[0])
        y = int(state.y.values[0])
        return (x, y)
    return "Incorrect"

# Screen setup
screen = turtle.Screen()
screen.title(f"U.S. States Game")
image = "./Day25-UsStatesGame/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Pen setup
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

while len(correct_states) < 50:
    try:
        answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="Guess the name of a state").title()
        check_state = check_state_in_csv(answer_state)
        
        if answer_state == "Exit":
            print("Exit typed")
            break

        if check_state != "Incorrect":
            correct_states.append(answer_state)
            correct_guesses += 1
            pen.goto(check_state)
            pen.write(f"{answer_state}", align="center", font=("Arial", 8, "normal"))
            all_states.remove(answer_state)

    except AttributeError:
        print("Cancel/Exit button clicked")
        break

# Create CSV from states user did not guess
states_to_learn = {
    "State Names to Study": all_states
}

states_to_learn_df = pandas.DataFrame(states_to_learn)
states_to_learn_df.to_csv(f"./Day25-USStatesGame/Results/states_to_learn-{formated_date}.csv")    
print("CSV file created in Results folder")