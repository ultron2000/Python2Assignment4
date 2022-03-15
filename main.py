
import turtle
import draw_square
import draw_rectangle
import draw_triangle
import draw_circle
import validation as v


terry = turtle.Turtle()


def menu():
    print('Welcome to the shape drawing application')
    print('Choose your shape!')
    print('Type 1 for square.')
    print('Type 2 for rectangle.')
    print('Type 3 for triangle.')
    print('Type 4 for circle.')
    print('Type 0 to exit.')


def main():
    while True:
        menu()
        choice = v.get_int("Please choose an option: ", 0, 4)
        if choice == 1:
            draw_square.main()

        elif choice == 2:
            draw_rectangle.main()

        elif choice == 3:
            draw_triangle.main()

        elif choice == 4:
            draw_circle.main()

        elif choice == 0:
            break

        else:
            print("Please enter one of the options!")


if __name__ == '__main__':
    main()
