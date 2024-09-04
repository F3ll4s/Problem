import turtle
turtle.speed(1)
def draw_sq(n):
    """Draw a square with side length n."""
    for _ in range(4):
        turtle.forward(n)
        turtle.right(90)

def spiral_sq(s):
    " 5""Draw spiral squares starting with size s."""
    while s >= 5 :
        turtle.pu()
        turtle.back(s/2)
        turtle.left(90)
        turtle.forward(s/2)
        turtle.right(90)
        turtle.pd()
        draw_sq(s)
        s *= 0.75
        turtle.pu()
        turtle.goto(0,0)# Reduce the size by 25%
        turtle.right(10)  # Rotate the turtle by 10 degrees

# Example usage
turtle.speed(1)  # Fastest drawing speed
spiral_sq(150)
turtle.done()
