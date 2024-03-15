from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for pos in START_POS:
            self.add_body(pos)

    def add_body(self, pos):
        tim = Turtle("square")
        tim.color('white')
        tim.penup()
        tim.goto(pos)
        tim.speed("slowest")
        self.body.append(tim)

    def extend(self):
        self.add_body(self.body[-1].position())

    def move(self):
        for tim_pos in range(len(self.body) - 1, 0, -1):
            x = self.body[tim_pos - 1].xcor()
            y = self.body[tim_pos - 1].ycor()
            self.body[tim_pos].goto(x, y)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def walkthrough(self):
        x = self.body[0].xcor()
        y = self.body[0].ycor()
        if self.body[0].heading() ==UP or self.body[0].heading() ==DOWN:
            self.body[0].goto(x,-y)
        if self.body[0].heading() == LEFT or self.body[0].heading() ==RIGHT:
            self.body[0].goto(-x,y)
