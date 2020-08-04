import turtle
import time

# Google search
maize = '#FFCB05'
blue = '#00274C'
# Google image search
width = 85.59
height = 61.47
top = 25.40
base = 32.35
outer_notch = 26.6
inner_notch = 16.92
notch = base - top
angle = 74

# Creating variables for plotting on 200x200 pixel grid
screen = 360
base_ratio = base/width
base_rise_ratio = ((height-outer_notch)/2)/height
notch_ratio = notch/width
inner_ratio = inner_notch/height
outer_ratio = outer_notch/height
top_ratio = top/width

wn = turtle.Screen()
wn.bgcolor(blue)

turtle.color(maize)
turtle.pensize(10)
turtle.up()
turtle.goto(-180,-180)
turtle.down()
turtle.forward(base_ratio*screen)
turtle.left(90)
turtle.forward(base_rise_ratio*screen)
turtle.left(90)
turtle.forward(notch_ratio*screen)
turtle.right(90)
turtle.forward(inner_ratio*screen)
turtle.right(90+53)
turtle.forward(150)
turtle.left(180-angle)
turtle.forward(150)
turtle.right(180-37)
turtle.forward(inner_ratio*screen)
turtle.right(90)
turtle.forward(notch_ratio*screen)
turtle.left(90)
turtle.forward(base_rise_ratio*screen)
turtle.left(90)
turtle.forward(base_ratio*screen)
turtle.left(90)
turtle.forward(base_rise_ratio*screen)
turtle.left(90)
turtle.forward(notch_ratio*screen)
turtle.right(90)
turtle.forward(outer_ratio*screen)
turtle.right(90)
turtle.forward(notch_ratio*screen)
turtle.left(90)
turtle.forward(base_rise_ratio*screen)
turtle.left(90)
turtle.forward(top_ratio*screen)
turtle.left(53)
turtle.forward(150)
turtle.right(180-angle)
turtle.forward(150)
turtle.left(53)
turtle.forward(top_ratio*screen)
turtle.left(90)
turtle.forward(base_rise_ratio*screen)
turtle.left(90)
turtle.forward(notch_ratio*screen)
turtle.right(90)
turtle.forward(outer_ratio*screen)
turtle.right(90)
turtle.forward(notch_ratio*screen)
turtle.left(90)
turtle.forward(base_rise_ratio*screen)

time.sleep(60)
