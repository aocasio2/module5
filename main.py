#alvin ocasio jr
#10/29/23
# Iterative Programming
#problem 1
count = 1
while count <= 100:
    print("Hello World")
    count += 1
#problem 2
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for number in numbers:
    square = number ** 2
    print(f"Number: {number}, Square: {square}")
#problem 3
import turtle
def draw_and_fill_polygon(sides, side_length, line_color, fill_color):
    angle = 360 / sides
    turtle.fillcolor(fill_color)
    turtle.pencolor(line_color)
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(side_length)
        turtle.right(angle)
    turtle.end_fill()
sides = int(input("Enter the number of sides for the polygon: "))
side_length = float(input("Enter the length of each side: "))
line_color = input("Enter the color of the line: ")
fill_color = input("Enter the fill color: ")
turtle.speed(1)
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
draw_and_fill_polygon(sides, side_length, line_color, fill_color)
turtle.exitonclick()
#problem 4
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by three")
    elif number % 5 == 0:
        print("Divisible by five")
    else:
        print(number)
#problem 5
import turtle

turtle.speed(0)
turtle.bgcolor("black")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(360):
    turtle.color(colors[i % 6])
    turtle.forward(i)
    turtle.right(59)

turtle.hideturtle()
turtle.done()

turtle.exitonclick()

