"""EX04 - Turtle. A beautiful landscape that includes mountains, trees, and a river."""

___author____ = "730474696"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    splinter: Turtle = Turtle()
    splinter.speed(3000)
    splinter.hideturtle()
    draw_sky(splinter, -600, 700, 2000, 2000)
    draw_mountain(splinter, -70, -50, 300, True)
    draw_mountain(splinter, 400, -50, 300, True)
    draw_mountain(splinter, 150, -50, 300, False)
    draw_grass(splinter, -350, -50, 800, 300)
    draw_sun(splinter, 0, 250, 50)
    draw_river(splinter, -600, -100, 2000, 50)
    draw_tree(splinter, -250, -200, 50, 20, 30)
    draw_tree(splinter, -50, -200, 50, 20, 30)
    draw_tree(splinter, 150, -200, 50, 20, 30)
    draw_tree(splinter, 100, -50, 50, 20, 30)
    draw_tree(splinter, -150, -50, 50, 20, 30)
    done()


def draw_mountain(splinter: Turtle, x: float, y: float, length: float, a: bool) -> None: 
    """Draw a mountain that starts a x,y if a returns false then a light grey mountain is drawn to imitate distance."""
    splinter.penup()
    splinter.goto(x, y) 
    splinter.setheading(0.0)
    splinter.pendown()
    i: int = 0
    splinter.pencolor("black")
    if a is True:
        splinter.begin_fill()
        splinter.fillcolor(85, 85, 85)
        while i < 3:
            splinter.left(120)
            splinter.forward(length)
            i += 1  
        splinter.end_fill()
    else:
        splinter.begin_fill()
        splinter.fillcolor(127, 127, 127)
        while i < 3:
            splinter.left(120)
            splinter.forward(length)
            i += 1
        splinter.end_fill()


def draw_grass(splinter: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draws grass right below the mountains."""
    splinter.penup()
    splinter.goto(x, y) 
    splinter.setheading(0.0)
    splinter.pendown()
    splinter.pencolor(5, 76, 11)
    splinter.begin_fill()
    splinter.fillcolor(16, 175, 15)
    i: int = 0
    while (i < 2):
        splinter.forward(length)
        splinter.right(90)
        splinter.forward(width)
        splinter.right(90)
        i = i + 1
    splinter.end_fill()


def draw_sun(splinter: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a sun above the mountains."""
    splinter.penup()
    splinter.goto(x, y) 
    splinter.setheading(0.0)
    splinter.pendown()
    splinter.pencolor(243, 239, 22)
    splinter.fillcolor(243, 239, 22)
    splinter.begin_fill()
    splinter.circle(radius)
    splinter.end_fill()


def draw_sky(splinter: Turtle, x: int, y: int, width: float, length: float) -> None:
    """Draws a square around the entire drawing and fills it blue to imitate the sky."""
    splinter.penup()
    splinter.goto(x, y) 
    splinter.setheading(0.0)
    splinter.pendown()
    splinter.pencolor("black")
    splinter.begin_fill()
    splinter.fillcolor(12, 197, 219)
    i: int = 0
    while (i < 2):
        splinter.forward(length)
        splinter.right(90)
        splinter.forward(width)
        splinter.right(90)
        i = i + 1
    splinter.end_fill()


def draw_river(splinter: Turtle, x: int, y: int, length: float, width: float) -> None:
    """Draws a River that cuts through the grass."""
    splinter.penup()
    splinter.goto(x, y) 
    splinter.setheading(0.0)
    splinter.pendown()
    splinter.pencolor("black")
    splinter.begin_fill()
    splinter.fillcolor(21, 66, 246)
    i: int = 0
    while i < 2:
        splinter.forward(length)
        splinter.right(90)
        splinter.forward(width)
        splinter.right(90)
        i = i + 1
    splinter.end_fill()


def draw_tree(splinter: Turtle, x: int, y: int, length_trunk: int, width_trunk: int, radius: int) -> None:
    """Draws a tree with trunks and leaves."""
    splinter.penup()
    splinter.goto(x, y) 
    splinter.setheading(0.0)
    splinter.pendown()
    splinter.pencolor("black")
    i: int = 0
    splinter.begin_fill()
    splinter.fillcolor(90, 41, 0)
    while i < 2:
        splinter.forward(width_trunk)
        splinter.right(90)
        splinter.forward(length_trunk)
        splinter.right(90)
        i = i + 1
    splinter.end_fill()
    splinter.pencolor("black")
    splinter.fillcolor(6, 123, 5)
    splinter.forward(width_trunk / 2)
    splinter.begin_fill()
    splinter.circle(radius)
    splinter.end_fill()


if __name__ == "__main__":
    main()
