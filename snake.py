from turtle import Turtle

class Snake:
    name = 'sem nome'
    starting_position = [(0,0), (-20, 0), (-40,0)]
    segments = []

    def __init__(self, name):
        self.name = name
        for position in self.starting_position:
            segment = Turtle("square")
            segment.color("green")
            segment.penup() # tira rastro 
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y) 
        self.segments[0].forward(20)
        self.segments[0].left(90)