# Import the Tkinter & Turtle Graphics Modules
import Tkinter
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

pixel = []
newTurtle = turtle.Turtle()
newTurtle.hideturtle()
newTurtle.penup()
newTurtle.goto(-240, 240)
newTurtle.shape("square")
newTurtle.color("white")
newTurtle.showturtle()
pixel.append(newTurtle)

# Main Game Loop (Keeps Game Window From Closing)
Tkinter.mainloop()
