# paddle class
from turtle import Turtle

class Paddle(Turtle):

    # constructor
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        
    # move the paddle
    def up(self):
        new_y_coord = self.ycor() + 20
        self.goto(self.xcor(), new_y_coord)

    def down(self):
        new_y_coord = self.ycor() - 20
        self.goto(self.xcor(), new_y_coord)
        