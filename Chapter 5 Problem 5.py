#Kamil Krawczyk
#02/13/2020

#This program draws a gentleman by the name of Drew. 
#Drew is having a great day which is shown by his smile :)

import turtle
turtle.speed(10)
for x in range(1,125):
    turtle.forward(15)
    turtle.left(360/100)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.right(102)
turtle.forward(700)
turtle.right(45)
turtle.forward(450)
turtle.penup()
turtle.goto(0,-700)
turtle.pendown()
turtle.left(90)
turtle.forward(450)
turtle.penup()
turtle.goto(0,-300)
turtle.pendown()
turtle.forward(350)
turtle.penup()
turtle.goto(0,-300)
turtle.pendown()
turtle.right(90)
turtle.forward(350)
turtle.penup()
turtle.goto(-125,400)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
for x in range (1,55):
  turtle.forward(3)
  turtle.left(360/50)
turtle.end_fill()
turtle.penup()
turtle.goto(105,400)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
for x in range (1,55):
  turtle.forward(3)
  turtle.left(360/50)
turtle.end_fill()
turtle.penup()
turtle.goto(-125,200)
turtle.pendown()
for x in range(1,67):
  turtle.forward(7)
  turtle.left(360/100)
turtle.penup()
turtle.goto(-1000,1000)

