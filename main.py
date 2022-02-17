
import turtle

terry = turtle.Turtle()


def draw_square():
    global terry

    terry.showturtle()
    terry.pendown()

    terry.color("green")
    terry.begin_fill()

    terry.forward(200)
    terry.left(90)
    terry.forward(200)
    terry.left(90)
    terry.forward(200)
    terry.left(90)
    terry.forward(200)
    terry.left(90)

    terry.end_fill()
    terry.penup()


def draw_rectangle():
    global terry

    terry.showturtle()
    terry.goto(-100, -300)
    terry.pendown()

    terry.color("yellow")
    terry.begin_fill()

    terry.forward(400)
    terry.left(90)
    terry.forward(200)
    terry.left(90)
    terry.forward(400)
    terry.left(90)
    terry.forward(200)
    terry.left(90)

    terry.end_fill()
    terry.penup()


def draw_triangle():
    global terry

    terry.showturtle()
    terry.goto(-300, 0)
    terry.pendown()

    terry.color("red")
    terry.begin_fill()

    terry.forward(200)
    terry.left(120)
    terry.forward(200)
    terry.left(120)
    terry.forward(200)
    terry.left(120)

    terry.end_fill()
    terry.penup()


def draw_circle():
    global terry

    terry.showturtle()
    terry.goto(-100, 150)
    terry.pendown()

    terry.color("blue")
    terry.begin_fill()

    terry.circle(50)

    terry.end_fill()
    terry.penup()


def main():
    draw_square()
    draw_rectangle()
    draw_triangle()
    draw_circle()
    turtle.done()


if __name__ == '__main__':
    main()
