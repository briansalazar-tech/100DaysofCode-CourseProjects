from turtle import Turtle, Screen, colormode
from random import choice
# import colorgram

##  Use colorgram to obtain a list of RGB colors. Create list of rgb colors to be used in turtle graphics ##
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(177, 2, 82), (181, 154, 117), (187, 162, 16), (39, 139, 51), (214, 24, 241), (82, 160, 202), (46, 86, 165), (252, 229, 22), (10, 1, 69), (124, 65, 31), (248, 1, 0), (53, 153, 128), (254, 4, 9), (237, 159, 205), (254, 5, 3), (238, 59, 54), (105, 49, 16), (105, 119, 169), (42, 57, 112), (247, 160, 153), (164, 209, 189)]

## Use Turtle Graphics to draw picture ## 
colormode(255)
starting_y = -220

# Set up screen
screen = Screen()
screen.setup(700, 700)

# Set up brush
brush = Turtle()
brush.hideturtle()
brush.penup()
brush.speed(10)

# Draw picture
for row in range(10):
    brush.goto(x=-225, y=starting_y)
    for dot in range(10):
        brush.dot(20, choice(color_list))
        brush.forward(50)
    starting_y += 50

screen.exitonclick()