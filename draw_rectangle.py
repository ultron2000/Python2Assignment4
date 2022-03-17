#!/usr/bin/env python3

"""
The module to draw a rectangle.
"""

__author__ = 'Joshua Greunke'
__version__ = '1.0'
__copyright__ = "Copyright 2022.03.17, Chapter 4 Assignment"
__github__ = "https://github.com/ultron2000/Python2Assignment4"

# Grabs the modules needed for the program
import turtle
import validation as v

terry = turtle.Turtle()


def draw_rectangle(input_color, input_long, input_short):
    """
    Draws a rectangle with the input parameters.
    :param input_color: The color of the rectangle.
    :param input_long: The length of the long sides of the rectangle.
    :param input_short: The length of the short sides of the rectangle.
    :return: none
    """
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
    """
    Confirms the selected shape and prompts the user for their desired inputs
    :return: none
    """
    print("Drawing a rectangle.")
    print("Please enter a color for the shape")
    input_color = input("Pick a color!: ")
    input_long = v.get_float('Please select how long you would like the long sides to be: ', 50, 400)
    input_short = v.get_float('Please select how long you would like the short sides to be: ', 50, 400)
    draw_rectangle(input_color, input_long, input_short)
    turtle.done()


if __name__ == '__main__':
    main()
