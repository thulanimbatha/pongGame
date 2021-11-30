# main pong file
from turtle import Screen, width
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Mondeor Pong!🙂")
screen.tracer(0)    # stop animation

paddle = Paddle()

screen.listen() # listen for keystrokes
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_on = True

while game_on:
    screen.update() # update animation

screen.exitonclick()