import turtle #Library for drawing graphics
import math #Library for math functions
import random

indu= turtle.Turtle()#Declaring a turtle with name 'indu',yes it's my name
indu.penup()#To move the turtle without making drawings on screen
indu.goto(0,200)
indu.pendown()
'''Code for the base design it is created
   using implematation of cos wave using math lib
   and for loop to keep on creating continous desired pattern'''

indu.color("black", "#F7EC41")#Border/Stroke color, fill color
indu.begin_fill()
indu.speed(12)#To speed the animation process a bit
for i in range(1050):
	indu.forward(20)
	indu.left(math.cos(i/10)*25)
	indu.left(30)
indu.end_fill()
indu.penup()
indu.goto(75,95)
indu.pendown()#To move the turtle without making drawings on screen
indu.color("black", "#2DDB66")#Border/Stroke color, fill color
indu.begin_fill()

'''Code for the green circledesign it is created
   using for loop to keep on creating continous desired circle
   And rt is used to move the circle for each iteration'''
for i in range(50):
  indu.circle(50)
  indu.rt(20)
indu.end_fill()

 
turtle.done()
