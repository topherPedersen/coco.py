'''
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
'''



# Import the Tkinter & Turtle Graphics Modules
import Tkinter
import turtle

'''
# Create Game Window
screen = turtle.Screen()
screen.screensize(600, 600, "green")
'''

'''
# Create Game Window
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("green")
'''
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

# Create Sprite
'''
screen.addshape("sprite.gif")
mySprite = turtle.Turtle()
mySprite.hideturtle() # hide turtle until the the duck image replaces the placeholder shape
mySprite.penup() # prevent sprite from drawing on screen as it moves
mySprite.left(90) # rotate sprite for proper placement on screen
mySprite.shape("sprite.gif") # Set Image for Sprite
mySprite.setposition(0, 0)
mySprite.showturtle()
'''


# Main Game Loop (Keeps Game Window From Closing)
Tkinter.mainloop()
