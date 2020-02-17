#Kamil Krawczyk
#02/13/2020

import turtle
wn = turtle.Screen()
jimmy = turtle.Turtle()
jimmy.speed(1)


sides = int(input("How many sides will this polygon have? - "))
length = int(input("How long will each line be? - "))
# asks the user for how many sides and how long each line should be

line_color = input("What should the color of the line be? - ")
fill_color = input("What color should the inside of the polygon be? - ")
# asks the user for the color of both the line and the inside fill of the polygon
#Add two lines to correct the fill color requirement
#jimmy.begin_fill()
jimmy.color(line_color)
jimmy.fillcolor(fill_color)
# function that changes the color of the line and the fill depending on the user input

for shape in range(int(sides)):
  jimmy.forward (int(length))
  jimmy.right (int(360/sides))
#jimmy.end_fill()

#for-loop that takes the user input and creates the shape
