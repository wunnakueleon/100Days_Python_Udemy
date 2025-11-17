from turtle import Turtle, Screen

screen = Screen()
POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:


    def __init__(self):
        self.segments = []
        for each_position in POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(each_position)
            self.segments.append(new_segment)
            

    def move(self):
        for each_seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[each_seg - 1].xcor()
            y_cor = self.segments[each_seg - 1].ycor()
            self.segments[each_seg].goto(x_cor, y_cor)
        
        self.segments[0].forward(20)




