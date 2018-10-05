import sys

# Check Python Version Number (Python Version 3+ Required)
if sys.version_info[0] < 3:
    print("ERROR: 'pmode' Module Requires Python Version 3.0 or Higher")
    exit() # kill script
else:
    # Import the Tkinter & Turtle Graphics Modules
    import tkinter
    import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

# Create a Multi-Dimensional Array Which Will Represent Our On-Screen Grid
pixel = []
# Y Position Represents a Row in Our Multi-Dimensional Array
for y in range(30):
    newRow = []
    pixel.append(newRow) 
    # X Position Represents a Single Space in an Individual Row in Our Multi-Dimensional Array
    for x in range(30):
        newTurtle = turtle.Turtle(visible=False)
        newRow.append(newTurtle)


# yCoordinate = 290
for y in range(30):
    # Set yCoordinate
    if y == 0:
        yCoordinate = 290
    elif y == 1:
        yCoordinate = 270
    elif y == 2:
        yCoordinate = 250
    elif y == 3:
        yCoordinate = 230
    elif y == 4:
        yCoordinate = 210
    elif y == 5:
        yCoordinate = 190
    elif y == 6:
        yCoordinate = 170
    elif y == 7:
        yCoordinate = 150
    elif y == 8:
        yCoordinate = 130
    elif y == 9:
        yCoordinate = 110
    elif y == 10:
        yCoordinate = 90
    elif y == 11:
        yCoordinate = 70
    elif y == 12:
        yCoordinate = 50
    elif y == 13:
        yCoordinate = 30
    elif y == 14:
        yCoordinate = 10
    elif y == 15:
        yCoordinate = -10
    elif y == 16:
        yCoordinate = -30
    elif y == 17:
        yCoordinate = -50
    elif y == 18:
        yCoordinate = -70
    elif y == 19:
        yCoordinate = -90
    elif y == 20:
        yCoordinate = -110
    elif y == 21:
        yCoordinate = -130
    elif y == 22:
        yCoordinate = -150
    elif y == 23:
        yCoordinate = -170
    elif y == 24:
        yCoordinate = -190
    elif y == 25:
        yCoordinate = -210
    elif y == 26:
        yCoordinate = -230
    elif y == 27:
        yCoordinate = -250
    elif y == 28:
        yCoordinate = -270
    elif y == 29:
        yCoordinate = -290
    # Set xCoordinate
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
        pixel[x][y].speed(0)
        pixel[x][y].penup()
        pixel[x][y].goto(xCoordinate, yCoordinate)
        pixel[x][y].shape("square")
        pixel[x][y].color("green")
        pixel[x][y].showturtle()

def set(x, y, c):
    global pixel
    pixel[x][y].color(c)


# Define placeholder Function (placeholder function used in place of main game logic in quick-start guide)
placeholder_x = -440
placeholder_y = 0
cycle = 0
ghost = turtle.Turtle(visible=False)
ghost.speed(0)
ghost.penup()
ghost.goto(placeholder_x, placeholder_y)
ghost.shape("square")
ghost.color("black") # set color to black to make ghost invisible
ghost.showturtle()
def busywork():
    global placeholder_x
    global placeholder_y
    global cycle
    global ghost

    if cycle == 0:
        placeholder_x = -500
    elif cycle == 1:
        placeholder_x = -480
    elif cycle == 2:
        placeholder_x = -460
    elif cycle == 3:
        placeholder_x = -440

    ghost.goto(placeholder_x, placeholder_y)

    if cycle == 3:
        cycle = 0
    else:
        cycle = cycle + 1
