from turtle import Screen
import time
from scoreboard import ScoreBoard

from paddel import Paddle

from ball import Ball
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Arcade Game")
screen.tracer(0)

padelR = Paddle(350)
padelL = Paddle(-350)

ball = Ball()

scoreboard = ScoreBoard()

screen.listen()
screen.onkey(padelR.go_up, "Up")
screen.onkey(padelR.go_down, "Down")

screen.onkey(padelL.go_up, "w")
screen.onkey(padelL.go_down, "s")

game_on = True
SLEEP_TIME = 0.01
while game_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.y_bounce()
    # detect collision with wall
    if padelR.distance(ball) < 50 and ball.xcor() > 325 or padelL.distance(ball) < 50 and ball.xcor() < -325:
        #bounce
        ball.x_bounce()
    #detect if Rpaddle misses
    if padelR.distance(ball) > 50 and ball.xcor() > 380:
        ball.reset_position()
        # padelR.reset_position()
        # padelL.reset_position()
        scoreboard.l_point()
        SLEEP_TIME /= 1.5
    # detect if Lpaddle misses
    if padelL.distance(ball) > 50 and ball.xcor() < -380:
        ball.reset_position()
        # padelR.reset_position()
        # padelL.reset_position()
        scoreboard.r_point()
        SLEEP_TIME /= 1.5




screen.exitonclick()
