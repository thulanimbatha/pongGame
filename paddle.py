# paddle class
from turtle import Turtle

class Paddle(Turtle):

    # constructor
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(-500, 0)
        