import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./Day25-UsStatesGame/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click(x,y):
#     """Get the coordinates of the mouse click on the screen"""
#     print(x,y)

# turtle.onscreenclick(get_mouse_click)

answer_state = screen.textinput(title="Guess the State", prompt="Guess the name of a state").title()
turtle.mainloop()
