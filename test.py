from turtle import Turtle, Screen

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")

initial = Turtle()



initial.penup()
initial.pencolor("white")
# self.hideturtle()
initial.goto(-260,260)
initial.setheading(0)
initial.pendown()
for x in range(4):
    initial.fd(520)
    initial.rt(90)

s.exitonclick()