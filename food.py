from turtle import Turtle
import random

food_list = []
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        food_list.append(self)
        
        
    def refresh(self):    
        x_food = random.randrange(-240, 260, 20)
        y_food = random.randrange(-240, 260, 20)
        self.goto(x_food,y_food)
