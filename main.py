# main pong file
from turtle import Screen, width
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()


screen.listen() # listen for keystrokes
# control left paddle with: up- and down
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
# control left paddle with: a and z 
screen.onkey(left_paddle.up, "a")
screen.onkey(left_paddle.down, "z")

game_on = True

while game_on:
    time.sleep(0.07)
    screen.update() # update animation
    ball.move()

    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce wall
        # reverse direction
        ball.bounce_y()

    # detect paddle collision -> right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    
    # detect paddle collision -> left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect left paddle miss
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_point()

    # detect right paddle miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()

screen.exitonclick()