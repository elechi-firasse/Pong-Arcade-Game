from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Arcade Game")
screen.tracer(0)

padel = Turtle()
padel.shape("square")
padel.color("white")
padel.shapesize(stretch_wid=5,stretch_len=1)
padel.penup()
padel.goto(x=350, y=0)

def go_up():
    new_y = padel.ycor() + 20
    padel.goto(x= padel.xcor(), y= new_y)
def go_down():
    new_y = padel.ycor() - 20
    padel.goto(x= padel.xcor(), y= new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_on = True
while game_on:
    screen.update()


screen.exitonclick()
