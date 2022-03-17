#!/usr/bin/env python3

"""
The module to draw a circle
"""

__author__ = 'Joshua Greunke'
__version__ = '1.0'
__copyright__ = "Copyright 2022.03.17, Chapter 4 Assignment"
__github__ = "https://github.com/ultron2000/Python2Assignment4"

# Grabs all modules needed for the program
import turtle
import validation as v

terry = turtle.Turtle()


def draw_circle(input_color, input_diam):
    """
    Draws a circle with the input parameters.
    :param input_color: The color of the circle.
    :param input_diam: The length of the diameter of the circle.
    :return: none
    """
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
    """
    Confirms the selected shape and prompts the user for their desired inputs
    :return: none
    """
    print("Drawing a circle.")
    print("Please enter a color for the shape")
    input_color = input("Pick a color!: ")
    input_diam = v.get_float('Please input how long you would like the diameter to be: ', 50, 400)
    draw_circle(input_color, input_diam)
    turtle.done()


if __name__ == '__main__':
    main()
