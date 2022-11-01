from multiprocessing.sharedctypes import SynchronizedString


from turtle import *

shape("turtle")


def draw_tree(level,size,angel):
    if level == 0:
        return 
    forward(size)
    right(angel)
    draw_tree(level - 1,size * 0.9,angel)
    left(angel * 2)
    draw_tree(level - 1,size * 0.8,angel)
    backward(size)
 
def snowflake(levels,size,shorten_factor,angle):
    if n == 0:
        forward(size)
    else:
        n -= 1
 
    
        size = size / shorten_factor
        snowflake(size ,levels,shorten_factor,angle)
        left(angle)
        snowflake(size ,levels,shorten_factor,angle)
        right(angle * 2)
        snowflake(size ,levels,shorten_factor,angle)
        left(angle)
        snowflake(size ,levels,shorten_factor,angle)

def draw(fract_type):
    levels = int(input())
    sizes = int(input())
    angles = int(input())
    if fract_type == 'tree':
        draw_tree(levels,sizes,angles)
    elif fract_type == 'snowflake':
        snowflake(levels,sizes,angles)

while True:
   frac = input('Pick the type of fractal you would like to draw')

   if frac == 'tree':
      draw('tree')
   elif frac == 'snowflake':
       draw('snowflake')
