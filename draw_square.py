#!/usr/bin/env python3

"""
The module to draw a square
"""

__author__ = 'Joshua Greunke'
__version__ = '1.0'
__copyright__ = "Copyright 2022.03.17, Chapter 4 Assignment"
__github__ = "https://github.com/ultron2000/Python2Assignment4"

# Grabs all modules needed for the program
import turtle
import validation as v

terry = turtle.Turtle()


def draw_square(input_color, input_length):
    """
    Draws a square with the input parameters
    :param input_color: The color of the square.
    :param input_length: The length of the sides of the square
    :return: none
    """
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
    """
    Confirms the selected shape and prompts the user for their desired inputs
    :return: none
    """
    print("Drawing a square.")
    print("Please enter a color for the shape")
    input_color = input("Pick a color!: ")
    input_length = v.get_float('Please select how long you would like the sides to be: ', 50, 400)
    draw_square(input_color, input_length)
    turtle.done()


if __name__ == '__main__':
    main()
