from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x, y=0)
        self.x = x

    def go_up(self):
            new_y = self.ycor() + 20
            if new_y > 250:
                new_y = 250
            self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
            new_y = self.ycor() - 20
            if new_y < -250:
                new_y = -250
            self.goto(x=self.xcor(), y=new_y)

    def reset_position(self):
        self.goto(x=self.x,y=0)


