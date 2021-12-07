# main pong file
from turtle import Screen, width
from paddle import Paddle
from ball import Ball
import time

RIGHT_COORD = (350, 0)
LEFT_COORD = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Mondeor Pong!🙂")
screen.tracer(0)    # stop animation

right_paddle = Paddle(RIGHT_COORD)
left_paddle = Paddle(LEFT_COORD)

ball = Ball()


screen.listen() # listen for keystrokes
# control left paddle with: up- and down
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
# control left paddle with: a and z 
screen.onkey(left_paddle.up, "a")
screen.onkey(left_paddle.down, "z")

game_on = True

while game_on:
    time.sleep(0.05)
    screen.update() # update animation
    ball.move()

screen.exitonclick()