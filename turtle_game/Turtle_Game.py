# Turtle Game using the package 'turtle'.

# Import relevant modules
import random
import turtle
import time

# Setting up a screen for the game
screen = turtle.Screen()
screen.bgcolor('lightblue') # Backgound a lighblue color

# We will have two players in this game and the idea is that whoever
# gets to the other side wins.

# Player one - set up
player_one = turtle.Turtle()
player_one.color('black')
player_one.shape('turtle')

# Player two - set up
player_two = player_one.clone()
player_two.color('orange')


# Position players.
player_one.penup()
player_one.goto(-300, 200)
player_two.penup()
player_two.goto(-300, -200)

# Draw a finish line
player_one.goto(300, -250)
player_one.left(90)
player_one.pendown()
player_one.color('darkblue')
player_one.forward(500)
player_one.write('Finish', font=24)

# Allows player one to return to its starting position
player_one.penup()
player_one.color('black')
player_one.goto(-300, 200)
player_one.right(90)

# Need to make sure both players have their pens down
player_one.pendown()
player_two.pendown()

# Create values for the die[zar]
die = [1, 2, 3, 4, 5, 6]

# Create the game!

for i in range(30):
    if player_one.pos() >= (300, 250):
        print('Player One Wins the Race!')
        break
    elif player_two.pos() >= (300, -250):
        print('Player Two Wins the Race!')
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30 * die_roll)
        time.sleep(0.5)
        die_roll2 = random.choice(die)
        time.sleep(0.5)
        player_two.forward(30 * die_roll)

turtle.done()
