import turtle
import pandas

total_guessed = 0
correct_states = []

# Read data from US States CSV file
data = pandas.read_csv("./Day25-UsStatesGame/50_states.csv")


def check_state_in_csv(state):
    """Checks to see if the value entered is in the CSV files. If it is, return the states coordinates"""
    if state in data.state.values:
        state = data[data.state == state]
        x = int(state.x.values[0])
        y = int(state.y.values[0])
        return (x, y)
    return "Incorrect"
# state = data[data.state == "Texas"]
# print(state)
# print(state.x.values[0])
# print(state.y.values[0])
# x = state["x"]
# y = state["y"]

# cor = (x, y)
# print(cor)
# states_dict = data.to_dict()

# for states in states_dict:
#     print(states)

# check = check_state_in_csv("California")





# Screen setup
screen = turtle.Screen()
screen.title(f"U.S. States Game")
image = "./Day25-UsStatesGame/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0,0)
pen.write("San Francisco", align="center", font=("Arial", 8, "normal"))



# def get_mouse_click(x,y):
#     """Get the coordinates of the mouse click on the screen"""
#     print(x,y)
# turtle.onscreenclick(get_mouse_click)

while True:
    try:
        answer_state = screen.textinput(title=f"{total_guessed}/50 States Correct", prompt="Guess the name of a state").title()
        check_state = check_state_in_csv(answer_state)
        if check_state != "Incorrect":
            correct_states.append(answer_state)
            total_guessed += 1
            pen.goto(check_state)
            pen.write(f"{answer_state}", align="center", font=("Arial", 8, "normal"))

    except AttributeError:
        print("Cancel/Exit button clicked")
        break
turtle.exitonclick()
