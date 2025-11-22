from turtle import Screen

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

screen.listen()
screen.onkey(padelR.go_up, "Up")
screen.onkey(padelR.go_down, "Down")

screen.onkey(padelL.go_up, "w")
screen.onkey(padelL.go_down, "s")

game_on = True
while game_on:
    screen.update()
    ball.move()

screen.exitonclick()
