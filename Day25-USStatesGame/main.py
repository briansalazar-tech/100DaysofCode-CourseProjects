import turtle

total_guessed = 0

screen = turtle.Screen()
screen.title(f"U.S. States Game")
image = "./Day25-UsStatesGame/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click(x,y):
#     """Get the coordinates of the mouse click on the screen"""
#     print(x,y)

# turtle.onscreenclick(get_mouse_click)

while True:
    try:
        answer_state = screen.textinput(title=f"{total_guessed}/50 States Correct", prompt="Guess the name of a state").title()
        print(answer_state)
        total_guessed += 1
    except AttributeError:
        print("Cancel/Exit button clicked")
        break
turtle.exitonclick()
