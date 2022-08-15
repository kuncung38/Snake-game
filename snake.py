from turtle import Turtle,Screen
import random
import os

INITIAL_POSITION = [(20, 0), (0,0), (-20,0)]
MOVE_DISTANCE = 20
COLOURS = ["red", "orange red", "tomato", "orange", "yellow", 
            "green yellow", "green", "lime", "pink", "hot pink",
            "blue", "deep sky blue", "medium slate blue", 
            "dark turquoise", "medium purple", "purple", "magenta"]

t = Turtle("square")
s = Screen()


#Snake head mod storing
head_path = "C:\\Users\\user\\Documents\\Python Experiment\\UDEMY\\Snake game\\snake_head"
os.chdir(head_path)

head_gifs= [file for file in os.listdir(head_path) if file.endswith('.gif')]
print(head_gifs)

for head in head_gifs:
    s.register_shape(head)


class Snake:
    
    def __init__(self):
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]
        user_choice = s.numinput('Choose your head!', '0 for normal head, 1 for cat head, 2 for PSYDUCK',minval= 0, maxval= 2)
        if user_choice == 0:
            self.head_mod_1()
        elif user_choice == 1:
            self.head_mod_cat()
        else:
            self.head_mod_psyduck()
        self.body_cordinates = []
        self.can_move = 0


    def add_segment(self, position):
        t = Turtle("square")
        t.penup()
        t.color(random.choice(COLOURS))
        t.shapesize(0.9, 0.9)
        t.setpos(position)
        self.body_segments.append(t)

    def head_mod_1(self):
        self.head.color("cyan")
        self.head.shape("circle")
        self.head.shapesize(0.6,0.8)

    def head_mod_cat(self):
        self.head.shape(head_gifs[0])

    def head_mod_psyduck(self):
        self.head.shape(head_gifs[1])

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
        if self.can_move == 0:
            if self.body_segments[0].heading() == 0:
                pass
            else:
                self.body_segments[0].seth(180)
                self.can_move += 1

    def headnorth(self):
        if self.can_move == 0:
            if self.body_segments[0].heading() == 270:
                pass
            else:
                self.body_segments[0].seth(90)
                self.can_move += 1

    def headeast(self):
        if self.can_move == 0:
            if self.body_segments[0].heading() == 180:
                pass
            else:
                self.body_segments[0].seth(0)
                self.can_move += 1

    def headsouth(self):
        if self.can_move == 0:
            if self.body_segments[0].heading() == 90:
                pass
            else:
                self.body_segments[0].seth(270)
                self.can_move += 1        
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
        self.can_move = 0