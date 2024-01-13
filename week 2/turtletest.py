import turtle
t = turtle.Turtle()


def draw_square(a: int, color: str):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(a)
        t.right(90)
    t.end_fill()


def draw_rectangle(a: int, b: int, color: str):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(a)
        t.right(90)
        t.forward(b)
        t.right(90)
    t.end_fill()


def draw_triangle(a: int, color: str):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(a)
        t.left(120)
    t.end_fill()


def draw_table(rows: int, cols: int, square_size: int, color1: str, color2: str):
    color_change = False
    for j in range((rows - 1) * square_size, -1 * square_size, -square_size):
        for i in range(0, cols * square_size, square_size):
            if color_change:
                color = color2
            else:
                color = color1
            t.teleport(i, j)
            draw_square(square_size, color)
            color_change = not color_change
        if cols % 2 == 0:
            color_change = not color_change


t.speed(100)
a1 = int(input('Enter parameters for table:\nrows: '))
b1 = int(input('columns: '))
s1 = int(input('size of cell: '))
c11 = input('first color: ')
c12 = input('second color: ')
draw_table(a1, b1, s1, c11, c12)
t.teleport(-200, 200)
a2 = int(input('Enter parameters for triangle:\nlength of side: '))
c2 = input('color: ')
draw_triangle(a2, c2)
t.teleport(-200, -200)
a3 = int(input('Enter parameters for rectangle:\nwidth: '))
b3 = int(input('height: '))
c3 = input('color: ')
draw_rectangle(a3, b3, c3)
