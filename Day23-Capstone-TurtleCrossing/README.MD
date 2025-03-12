# Day 23: Turtle Crossing Capstone
![Turtle Crossing Gameplay](../Images/Day23-TurtleCrossingGamePlay.png)
## Lesson Overview
The Turtle Crossing project is the second capstone project in this course. The project tests one’s abilities in the content covered in the previous lessons. Below are some of the areas that this project really touched on.
-	Breaking down complex problems into smaller chunks
-	Understanding programming logic
-	Working with Turtle Graphics
-	Utilizing Object Oriented Programming
## Project
### Modules Used
**Random** - Random is used to specify a random starting x and y coordinate for a car when the car is spawned off screen. Doing so ensures that cars are spaced apart randomly.

**Time** - The time module is used to control the update speed of the screen.

**Turtle graphics** - Turtle graphics is used to create the screen and the various objects used in the game including the turtle, cars, and level counter.

### Project Files
#### Car_manager.py

#### Main.py

#### Player.py
The **player.py** file contains a single class called Player. The **Player** class is used to control the turtle object that is controlled by the player. The class itself has two methods; **move** which moves the turtle forward when the method is called, and **level_up** which resets the turtles starting position when the turtle makes it to the finish line.
#### Scoreboard.py
**Scoreboard.py** contains a single class called Scoreboard. The **Scoreboard** class is used to display the current level and display “Game Over” when the player crashes into a car object.
### Project Walkthrough

![Turtle Crossing Gameover](../Images/Day23-TurtleCrossingGameOver.png)
### Project Flow Chart
![Turtle Crossing Flowchart](../Images/Day23-TurtleCrossingFlow.png)
