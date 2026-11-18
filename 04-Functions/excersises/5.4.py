# Turtle figures

def draw_square(pen, length):  # rysowanie kwadratu

    for i in range(4):

        pen.forward(length)

        pen.right(90)

def draw_triangle(pen, length):  # rysowanie trójkąta

    for i in range(3):

        pen.forward(length)

        pen.left(120)

def draw_rectangle(pen, a, b):  # rysowanie prostokąta

    for i in range(2):

        pen.forward(a)

        pen.right(90)

        pen.forward(b)

        pen.right(90)