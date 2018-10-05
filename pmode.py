# Import the Tkinter & Turtle Graphics Modules
import tkinter
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

# Create an Array Named "pixel" 
# Each "pixel" Will Represent a Dot on the Player's Screen
pixel = []
pixelIndex = 0
for x in range(30):
	pixel.append(True) # Assign Placeholder Value

yCoordinate = 290
for x in range(30):
    if x == 0:
        xCoordinate = -290
    elif x == 1:
        xCoordinate = -270
    elif x == 2:
        xCoordinate = -250
    elif x == 3:
        xCoordinate = -230
    elif x == 4:
        xCoordinate = -210
    elif x == 5:
        xCoordinate = -190
    elif x == 6:
        xCoordinate = -170
    elif x == 7:
        xCoordinate = -150
    elif x == 8:
        xCoordinate = -130
    elif x == 9:
        xCoordinate = -110
    elif x == 10:
        xCoordinate = -90
    elif x == 11:
        xCoordinate = -70
    elif x == 12:
        xCoordinate = -50
    elif x == 13:
        xCoordinate = -30
    elif x == 14:
        xCoordinate = -10
    elif x == 15:
        xCoordinate = 10
    elif x == 16:
        xCoordinate = 30
    elif x == 17:
        xCoordinate = 50
    elif x == 18:
        xCoordinate = 70
    elif x == 19:
        xCoordinate = 90
    elif x == 20:
        xCoordinate = 110
    elif x == 21:
        xCoordinate = 130
    elif x == 22:
        xCoordinate = 150
    elif x == 23:
        xCoordinate = 170
    elif x == 24:
        xCoordinate = 190
    elif x == 25:
        xCoordinate = 210
    elif x == 26:
        xCoordinate = 230
    elif x == 27:
        xCoordinate = 250
    elif x == 28:
        xCoordinate = 270
    elif x == 29:
        xCoordinate = 290
    pixel[pixelIndex] = turtle.Turtle()
    pixel[pixelIndex].hideturtle()
    pixel[pixelIndex].penup()
    pixel[pixelIndex].goto(xCoordinate, yCoordinate)
    pixel[pixelIndex].shape("square")
    pixel[pixelIndex].color("green")
    pixel[pixelIndex].showturtle()
    pixelIndex = pixelIndex + 1

# Main Game Loop (Keeps Game Window From Closing)
tkinter.mainloop()
