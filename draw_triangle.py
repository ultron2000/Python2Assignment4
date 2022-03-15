
import turtle
import validation as v

terry = turtle.Turtle()


def draw_triangle(input_color, input_length):
    global terry

    terry.showturtle()
    terry.penup()
    terry.goto(-100, -100)
    terry.pendown()

    terry.color(input_color)
    terry.begin_fill()

    terry.forward(input_length)
    terry.left(120)
    terry.forward(input_length)
    terry.left(120)
    terry.forward(input_length)
    terry.left(120)

    terry.end_fill()
    terry.penup()


def main():
    print("Drawing a triangle.")
    print("Please enter a color for the shape")
    input_color = input("Pick a color!: ")
    input_length = v.get_float('Please select how long you would like the sides to be: ', 50, 400)
    draw_triangle(input_color, input_length)
    turtle.done()


if __name__ == '__main__':
    main()
