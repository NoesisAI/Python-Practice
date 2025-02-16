from turtle import *
import random
import math

# Setup screen
screen = Screen()
screen.bgcolor("LimeGreen")

# Color options
colors = ["HotPink", "DeepSkyBlue", "Gold", "White", "Lavender", "Cyan", "OrangeRed", "Plum"]

# Setup turtle
t = Turtle()
t.speed(0)
t.pensize(4)
t.shape("turtle")

# Track positions to avoid overlaps
placed_positions = []

def vshape():
    """Creates a 'V' shape at the end of each snowflake arm."""
    t.right(25)
    t.forward(30)  
    t.back(30)
    t.left(50)
    t.forward(30)
    t.back(30)
    t.right(25)

def snowflakeArm():
    """Creates one full arm of the snowflake with multiple V-shapes."""
    for _ in range(8):  # Increase this number for more V-shapes per arm
        t.forward(20)  # Shorter distance per step for denser V-shapes
        vshape()
        t.back(20)

def snowflake(arms=12):  
    """Draws a full snowflake with a given number of arms."""
    for _ in range(arms):  
        snowflakeArm()
        t.right(360.0 / arms)  # Ensures accurate rotation!

def is_too_close(new_x, new_y, min_distance=100):
    """Check if new snowflake is too close to existing ones."""
    for x, y in placed_positions:
        if math.sqrt((new_x - x) ** 2 + (new_y - y) ** 2) < min_distance:
            return True  # Too close
    return False  # Safe placement

# Loop to draw multiple snowflakes at non-overlapping positions
for _ in range(20):  # Change this number to draw more snowflakes
    t.color(random.choice(colors))  
    t.pencolor(random.choice(colors))

    # Find a safe position to place the snowflake
    while True:
        x = random.randint(-200, 200)  
        y = random.randint(-200, 200)
        if not is_too_close(x, y, min_distance=120):  # Increase min_distance if needed
            placed_positions.append((x, y))
            break  # Found a good spot

    # Move to the safe position
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    snowflake(arms=random.randint(10, 16))  # Random number of arms per snowflake

# Hide turtle and keep window open
t.hideturtle()
screen.mainloop()
