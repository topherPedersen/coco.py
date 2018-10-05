# Import the Turtle 2D Graphics Module
import turtle 

# Create Game Window
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("green")

pixel = []
newTurtle = turtle.Turtle()
newTurtle.hideturtle()
newTurtle.penup()
newTurtle.goto(-240, 240)
newTurtle.shape("square")
newTurtle.color("white")
newTurtle.showturtle()
pixel.append(newTurtle)

i = 0
while True:
    if i % 100 == 0:
        print("iteration count: " + str(i))
    i = i + 1
