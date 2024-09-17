import random
import turtle
from turtle import Turtle,Screen
from random import randint

turtle.colormode(255)
tim=Turtle()
tim.speed("fastest")

def forward():
    tim.fd(10)
def backward():
    tim.bk(10)
def right():
    tim.setheading(tim.heading()-10)
def left():
    tim.setheading(tim.heading()+10)
def clear():
    tim.reset()

screen=Screen()
screen.listen()
screen.onkey(key='w',fun=forward)
screen.onkey(key='s',fun=backward)
screen.onkey(key='d',fun=right)
screen.onkey(key='a',fun=left)
screen.onkey(key='c',fun=clear)
screen.exitonclick()










