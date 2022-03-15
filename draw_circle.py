
import turtle
import validation as v

terry = turtle.Turtle()


def draw_circle(input_color, input_diam):
    global terry

    terry.showturtle()
    terry.penup()
    terry.goto(0, 0)
    terry.pendown()

    terry.color(input_color)
    terry.begin_fill()

    terry.circle(input_diam)

    terry.end_fill()
    terry.penup()


def main():
    print("Drawing a circle.")
    print("Please enter a color for the shape")
    input_color = input("Pick a color!: ")
    input_diam = v.get_float('Please input how long you would like the diameter to be: ', 50, 400)
    draw_circle(input_color, input_diam)
    turtle.done()


if __name__ == '__main__':
    main()
