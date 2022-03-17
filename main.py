#!/usr/bin/env python3

"""
The main menu to Draw Shapes
"""

__author__ = 'Joshua Greunke'
__version__ = '1.0'
__copyright__ = "Copyright 2022.03.17, Chapter 4 Assignment"
__github__ = "https://github.com/ultron2000/Python2Assignment4"

# Grabs all modules needed for the program
import draw_square
import draw_rectangle
import draw_triangle
import draw_circle
import validation as v


def menu():
    """
    Displays the main menu.
    :return: none
    """
    print('Welcome to the shape drawing application!')
    print('=' * 40)
    print('Choose your shape!')
    print('Type 1 for square.')
    print('Type 2 for rectangle.')
    print('Type 3 for triangle.')
    print('Type 4 for circle.')
    print('Type 0 to exit.')
    print('=' * 40)


def main():
    """
    Runs the menu and receives user input regarding the shape, color, and side length.
    :return: none
    """
    while True:
        menu()
        choice = v.get_int("Please choose an option: ", 0, 4)
        if choice == 1:
            draw_square.main()
            break

        elif choice == 2:
            draw_rectangle.main()
            break

        elif choice == 3:
            draw_triangle.main()
            break

        elif choice == 4:
            draw_circle.main()
            break

        elif choice == 0:
            break

        else:
            print("Please enter one of the options!")


if __name__ == '__main__':
    main()
