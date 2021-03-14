import math
import turtle
import time


# Starting a Working Screen
ws = turtle.Screen()

# initializing a turtle instance
geekyTurtle = turtle.Turtle()
turtle.bgcolor("black")
turtle.fillcolor("white")
turtle.title("Geometric Figures") # and why? when this is working
turtle.fillcolor("red")
turtle.pensize(5)
turtle.pencolor("white")
turtle.speed(1)
time.sleep(1)


geometric_figures = {0: "Quit",
                     1: "Circle",
                     2: "Square",
                     3: "Rectangle",
                     4: "Regural Trapezium",
                     5: "Rhombus",
                     6: "isosceles triangle"}


class Figure:

    def isFigure(self):
        return True

class Circle(Figure):

    def __init__(self):
        self.radius = read_number("Please provide radius size: ")

    def print_area(self):

        area = self.circle_field()
        print("The area is", area)

    def circle_field(self):
        """
        Function return compute field for figure
        :param radius: Take data from user
        :return: figure field
        """
        circle_field = math.pi * (self.radius ** 2)
        return circle_field


    def draw(self):
        turtle.circle(60)
        time.sleep(2)


class Square(Figure):

    def __init__(self):
        self.side = read_number("Please provide side size: ")

    def print_area(self):

        area2 = self.square_field()
        print("The area is", area2)

    def square_field(self):
        """
        Function return compute field for figure
        :param side: Take data from user
        :return: figure field
        """

        square_field = self.side * self.side
        return square_field

    def draw(self):
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.backward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        time.sleep(2)

class Rectangle(Figure):

    def __init__(self):
        self.side_a = read_number("Please provide side_a size: ")
        self.side_b = read_number("Please provide side_b size: ")

    def print_area(self):

        area3 = self.rectangle_field()
        print("The area is", area3)

    def rectangle_field(self):
        """
        Function return compute field for figure
        :param side_a: Take data from user
        :param side_b: Take data from user
        :return: figure field
        """

        rectangle_field = self.side_a * self.side_b
        return rectangle_field

    def draw(self):
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.backward(200)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(200)
        time.sleep(2)

class Regural_Trapezium(Figure):

    def __init__(self):
        self.side_a = read_number("Please provide side_a size: ")
        self.side_b = read_number("Please provide side_b size: ")
        self.h = read_number("Please provide h size: ")

    def print_area(self):
        area4 = self._regural_trapezium_field()
        print("The area is", area4)

    def _regural_trapezium_field(self):

        regural_trapezium_field = (self.side_a + self.side_b) * self.h / 2
        return regural_trapezium_field


    def draw(self):

        turtle.forward(100)
        turtle.goto(140, -100)
        turtle.left(0)
        turtle.backward(190)
        turtle.goto(4, 1)
        time.sleep(1)

class Rhombus(Figure):

    def __init__(self):
        self.side_a = read_number("Please provide side_a size: ")
        self.h = read_number("Please provide side_b size: ")

    def print_area(self):

        area5 = self._rhombus_field()
        print("The area is", area5)

    def _rhombus_field(self):
        """
        Function return compute field for figure
        :param side_a: Take data from user
        :param h: Take data from user
        :return: figure field
        """

        rhombus_field = self.side_a * self.h
        return rhombus_field

    def draw(self):
        turtle.right(90)
        turtle.forward(100)
        turtle.goto(75, -150)
        turtle.backward(100)
        turtle.goto(5, 5)
        time.sleep(1)

class IsoscelesTriangle(Figure):

    def __init__(self):
        self.side_a = read_number("Please provide side_a size: ")
        self.h = read_number("Please provide h size: ")

    def print_area(self):
        area6 = self._isosceles_triangle_field()
        print("The area is", area6)

    def _isosceles_triangle_field(self):
        """
        Function return compute field for figure
        :param side_a: Take data from user
        :param h: Take data from user
        :return: figure field
        """

        isosceles_triangle_field = (self.side_a / 2) * self.h
        return isosceles_triangle_field

    def draw(self):
        turtle.fd(100)
        turtle.lt(120)
        turtle.fd(100)
        turtle.lt(120)
        turtle.fd(100)
        time.sleep(1)


options = {
    1: Circle,
    2: Square,
    3: Rectangle,
    4: Regural_Trapezium,
    5: Rhombus,
    6: IsoscelesTriangle
}

def read_number(text):
    valid_input = False
    while not valid_input:
        try:
            values = input(text)
            values = int(values)
            valid_input = True
        except ValueError:
            print('Input must be a number')
    return values


if __name__ == '__main__':


    quit = False # WHY HERE QUIT IS OUTSIDE THE LOOP AND WITH VALUe FALSE
    while not quit:
        try:
            print(geometric_figures, end='\n')
            choice = input("Please choose geometric figure: ")
            choice = int(choice)
            if choice == 0:
                quit = True
            else:
                print(geometric_figures[choice])
                myFigure = options[choice]()
                myFigure.print_area()
                myFigure.draw()
        except ValueError:
            print('Input must be a number')
        except KeyError as e:
            print("Wrong choice. Please choose something from: ", '\n', geometric_figures.items())
