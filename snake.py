from turtle import Turtle,Screen
import random
INITIAL_POSITION = [(20, 0), (0,0), (-20,0)]
MOVE_DISTANCE = 20
COLOURS = ["red", "orange red", "tomato", "orange", "yellow", 
            "green yellow", "green", "lime", "pink", "hot pink",
            "blue", "deep sky blue", "medium slate blue", 
            "dark turquoise", "medium purple", "purple", "magenta"]
t = Turtle("square")

s = Screen()

class Snake:
    
    def __init__(self):
        self.boundaries_creation()
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]
        self.head_mod()
        self.body_cordinates = []


    def boundaries_creation(self):
        t.penup()
        t.pencolor("white")
        t.hideturtle()
        t.goto(-260,260)
        t.seth(0)
        t.pendown()
        for x in range(4):
            t.fd(520)
            t.rt(90)    

    def add_segment(self, position):
        t = Turtle("square")
        t.penup()
        t.color(random.choice(COLOURS))
        t.shapesize(0.9, 0.9)
        t.setpos(position)
        self.body_segments.append(t)

    def head_mod(self):
        self.head.color("cyan")
        self.head.shape("circle")
        self.head.shapesize(0.6,0.8)

    def create_snake(self):
        for position in INITIAL_POSITION:
            self.add_segment(position) 

    def extend(self):
        self.add_segment(self.body_segments[-1].position())

    def update_coordinates(self):
        self.body_cordinates.clear()
        for segment in self.body_segments:   
            self.body_cordinates.append(segment.position())


    """direction"""       
    def headwest(self):
        if self.body_segments[0].heading() == 0:
            pass
        else:
            self.body_segments[0].seth(180)

    def headnorth(self):
        if self.body_segments[0].heading() == 270:
            pass
        else:
            self.body_segments[0].seth(90)

    def headeast(self):
        if self.body_segments[0].heading() == 180:
            pass
        else:
            self.body_segments[0].seth(0)

    def headsouth(self):
        if self.body_segments[0].heading() == 90:
            pass
        else:
            self.body_segments[0].seth(270)        
    """direction end"""

    def move(self):
        for segment in range(len(self.body_segments)-1, 0, -1 ):
            self.body_segments[segment].goto(x= self.body_segments[segment-1].xcor(),
                                             y= self.body_segments[segment-1].ycor())      
        self.body_segments[0].forward(20)
        self.update_coordinates()
        s.onkeypress(self.headwest, "Left")
        s.onkeypress(self.headeast, "Right")
        s.onkeypress(self.headnorth, "Up")
        s.onkeypress(self.headsouth, "Down")

    def clear_snake(self):
        t.re
    