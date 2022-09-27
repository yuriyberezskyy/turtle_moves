from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def rotate_left():
    tim.left(10)


def rotate_right():
    tim.right(10)


def move_back():
    tim.back(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='c', fun=clear)

screen.exitonclick()a