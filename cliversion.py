from multiprocessing.sharedctypes import SynchronizedString


from turtle import *

shape("turtle")

levels = int(input())
sizes = int(input())
anges = int(input())

def draw_tree(level,size,angel):
    if level == 0:
        return 
    forward(size)
    right(angel)
    draw_tree(level - 1,size * 0.9,angel)
    left(angel * 2)
    draw_tree(level - 1,size * 0.8,angel)
    backward(size)
 
def snowflake(size,levels,shorten_factor,angle):
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
