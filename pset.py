# Import the Turtle 2D Graphics Module
import turtle 

# Create Game Window
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("black")

pixel = []
newTurtle = turtle.Turtle()
newTurtle.goto(-240, 240)
newTurtle.shape("square")
newTurtle.color("white")
pixel.append(newTurtle)

i = 0
while True:
    if i % 100 == 0:
        print("iteration count: " + str(i))
    i = i + 1
