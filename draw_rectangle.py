
import turtle
import validation as v

terry = turtle.Turtle()


def draw_rectangle(input_color, input_long, input_short):
    global terry

    terry.showturtle()
    terry.penup()
    terry.goto(-100, -100)
    terry.pendown()

    terry.color(input_color)
    terry.begin_fill()

    terry.forward(input_long)
    terry.left(90)
    terry.forward(input_short)
    terry.left(90)
    terry.forward(input_long)
    terry.left(90)
    terry.forward(input_short)
    terry.left(90)

    terry.end_fill()
    terry.penup()


def main():
    print("Drawing a rectangle.")
    print("Please enter a color for the shape")
    input_color = input("Pick a color!: ")
    input_long = v.get_float('Please select how long you would like the long sides to be: ', 50, 400)
    input_short = v.get_float('Please select how long you would like the short sides to be: ', 50, 400)
    draw_rectangle(input_color, input_long, input_short)
    turtle.done()


if __name__ == '__main__':
    main()
