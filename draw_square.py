
import turtle
import validation as v

terry = turtle.Turtle()


def draw_square(input_color, input_length):
    global terry

    terry.showturtle()
    terry.pendown()

    terry.color(input_color)
    terry.begin_fill()

    terry.forward(input_length)
    terry.left(90)
    terry.forward(input_length)
    terry.left(90)
    terry.forward(input_length)
    terry.left(90)
    terry.forward(input_length)
    terry.left(90)

    terry.end_fill()
    terry.penup()


def main():
    print("Drawing a square.")
    print("Please enter a color for the shape")
    input_color = input("Pick a color!: ")
    input_length = v.get_float('Please select how long you would like the sides to be: ', 50, 400)
    draw_square(input_color, input_length)
    turtle.done()


if __name__ == '__main__':
    main()
