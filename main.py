
import turtle

terry = turtle.Turtle()


def draw_square(input_color):
    global terry

    terry.showturtle()
    terry.pendown()

    terry.color(input_color)
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


def draw_rectangle(input_color):
    global terry

    terry.showturtle()
    terry.penup()
    terry.goto(-100, -300)
    terry.pendown()

    terry.color(input_color)
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


def draw_triangle(input_color):
    global terry

    terry.showturtle()
    terry.penup()
    terry.goto(-300, 0)
    terry.pendown()

    terry.color(input_color)
    terry.begin_fill()

    terry.forward(200)
    terry.left(120)
    terry.forward(200)
    terry.left(120)
    terry.forward(200)
    terry.left(120)

    terry.end_fill()
    terry.penup()


def draw_circle(input_color):
    global terry

    terry.showturtle()
    terry.penup()
    terry.goto(-100, 150)
    terry.pendown()

    terry.color(input_color)
    terry.begin_fill()

    terry.circle(50)

    terry.end_fill()
    terry.penup()


def main():
    print("Please enter a shape, the choices are: square, rectangle, triangle, circle.")
    input_shape = input("Please choose your desired shape: ")
    print("Please enter a color for the shape")
    input_color = input("Pick a color!: ")
    if input_shape == "square":
        draw_square(input_color)

    if input_shape == "rectangle":
        draw_rectangle(input_color)

    if input_shape == "triangle":
        draw_triangle(input_color)

    if input_shape == "circle":
        draw_circle(input_color)

    turtle.done()


if __name__ == '__main__':
    main()
