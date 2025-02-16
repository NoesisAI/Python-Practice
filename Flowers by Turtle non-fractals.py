from turtle import *
import random
import math

screen = Screen()
screen.bgcolor("MidnightBlue")  # Dark background for better contrast

colors = ["HotPink", "DeepSkyBlue", "Gold", "White", "Lavender", "Cyan", "OrangeRed", "Plum"]

t = Turtle()
t.speed(0)
t.pensize(2)
t.shape("turtle")

# Track positions to prevent overlaps
placed_positions = []

def vshape(size):
    """Creates a 'V' shape at the end of each snowflake arm."""
    angle = random.randint(20, 35)  # Randomize V-shape angles
    t.right(angle)
    t.forward(size)
    t.back(size)
    t.left(angle * 2)
    t.forward(size)
    t.back(size)
    t.right(angle)

def snowflakeArm(size, branches):
    """Creates one full arm of the snowflake with multiple V-shapes."""
    for _ in range(branches):  # More branches for extra detail
        step_size = random.randint(int(size / 4), int(size / 2))  # Vary segment size
        t.forward(step_size)
        vshape(step_size / 2)  # Adjust V-size dynamically
        t.back(step_size)

def snowflake(arms, size, branches):
    """Draws a full snowflake with given arms, size, and branch details."""
    for _ in range(arms):  
        snowflakeArm(size, branches)
        t.right(360.0 / arms)  # Ensure accurate rotation

def is_too_close(new_x, new_y, min_distance=100):
    """Check if new snowflake is too close to existing ones."""
    for x, y in placed_positions:
        if math.sqrt((new_x - x) ** 2 + (new_y - y) ** 2) < min_distance:
            return True  # Too close
    return False  # Safe placement

# Generate multiple snowflakes with complete randomization
for _ in range(20):  # Adjust this number to add more snowflakes
    t.color(random.choice(colors))  
    t.pencolor(random.choice(colors))
    
# Generate random properties for each snowflake
    arms = random.randint(8, 18)  # More arms for complex snowflakes
    size = random.randint(50, 120)  # Random snowflake size
    branches = random.randint(6, 12)  # More V-shapes per arm

# Find a safe position to place the snowflake
    while True:
        x = random.randint(-250, 250)  
        y = random.randint(-250, 250)  
        if not is_too_close(x, y, min_distance=size * 2.0):  # Distance scales with size
            placed_positions.append((x, y))
            break  # Found a good spot

# Move to the safe position
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    snowflake(arms, size, branches)  # Randomized snowflake properties

# Hide turtle and keep window open
t.hideturtle()
screen.mainloop()
