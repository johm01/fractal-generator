from turtle import *
## Different Fractals and Fractals i made up on my own 
speed(0)

# Triangle
def triangle(size,angle):
    setheading()
    for i in range(3):
        left(angle)
        forward(size)

# Serpinski Triangle
def serpinski(n,size,angle):
    if n == 0:
        triangle(size,angle)
        return
    else:
        serpinski(n - 1,size,angle)
        forward(size * 2 ** (n-1))
        right(angle)
        serpinski(n - 1,size,angle)
        left(angle)
        forward(size * 2 ** (n-1))
        serpinski(n - 1,size,angle)
        forward(size * 2 ** (n-1))

## Fractal Tree
def tree(size,levels,angle):
    if levels ==0:
        color('Green')
        dot(size)
        color('Blue')
        return

    # Right side 
    forward(size)
    right(angle)

    tree(size * 0.8,levels - 1, angle)

    # Left side 
    left(angle *2)

    tree(size * 0.8,levels-1,angle)

    # Back to the start 
    right(angle)
    backward(size)

# Koch Curve 
def koch_curve(n,length,shorten_factor,angle):

    # Drawing at the start 
    if n == 0:
        forward(length)
    else:
        n -= 1
 
        koch_curve(n ,length,shorten_factor,angle)
        left(angle)
        koch_curve(n ,length,shorten_factor,angle)
        right(angle * 2)
        koch_curve(n ,length,shorten_factor,angle)
        left(angle)
        koch_curve(n ,length,shorten_factor,angle)

# Custom fractal 
def shape(n,size):
    if n == 0:
        dot('red')
        return
    forward(size) 
    left(90)
    shape(n-1,size)
    right(90)
    shape(n-1,size)
    left(90)
    shape(n-1,size)
    
shape(3,10)
mainloop()