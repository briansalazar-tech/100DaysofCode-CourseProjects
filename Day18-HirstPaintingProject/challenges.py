import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")
colormode(255)

# colors = ["red", "blue", "green", "pink", "black", "orange"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color =  (r, g, b)
    return random_color


colors = random_color()

# Challenge 1: Draw a square
# for side in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# Challenge 2: Draw a dashed line
# for space in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Challenge 3: Draw different shapes
# timmy.penup()
# timmy.goto(x=-100, y=300)
# timmy.pendown()
# for index in range(3, 11):
#     timmy.color(random.choice(colors))
#     for side in range (index):
#         timmy.forward(200)
#         timmy.right(360/index)
        

# Challenge 4: Random Walk
# turn = [90, 180, 270, 360]
# timmy.pensize(5)
# timmy.speed(10)
# for step in range(100):
#     timmy.forward(20)
#     # timmy.color(random.choice(colors))
#     timmy.color(random_color())
#     timmy.setheading(random.choice(turn))

# CHallenge 6 Draw a spirograph
timmy.speed(10)
def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()

