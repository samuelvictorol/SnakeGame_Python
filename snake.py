from turtle import Turtle
STARTING_POSITION = [(0,0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
class Snake:
    
    def __init__(self):
        self.segments = []
        self.generateSnake()
        self.head = self.segments[0]
        self.head.color("blue")

    def generateSnake(self):
        for position in STARTING_POSITION:
            segment = Turtle("square")
            segment.color("white")
            segment.penup() # tira rastro 
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y) 
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)
    
    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

