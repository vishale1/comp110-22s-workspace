"""A tutorial on how to use turtles."""

__author__ = 730474696


from turtle import Turtle, colormode, done
colormode(255)
side_length: float = 300

leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
leo.up()
leo.goto(-150, -75)
leo.down()
leo.color(127, 127, 127)

i: int = 0
leo.begin_fill()
while i < 3:
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.up()
bob.goto(-150, -75)
bob.down()

a: int = 0
while a < 70:
    bob.forward(side_length)
    bob.left(123)
    a += 1
    side_length = side_length * 0.97

done()