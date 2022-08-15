from turtle import Screen
import time

from snake import *
from food import Food
from scoreboard import Scoreboard

from tkinter import messagebox as mbox

def initialization():
    #Screen initialization
    s = Screen()
    s.setup(width=600, height=600)
    s.bgcolor("black")
    s.title("Snake game")
    s.tracer(0)

#Game start
game_is_on = True

def game_start():
    global game_is_on
    game_is_on = True
    initialization()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    
    while game_is_on:
        time.sleep(0.1) 
        s.update()  
        snake.move()
        s.listen()

        if snake.head.distance(food) < 15:
            food.refresh()
            #Dont let food spawn on snake's body coordinates
            for each in snake.body_cordinates:
                if food.pos() == each:
                    food.refresh()
            scoreboard.add_score()
            snake.extend()
        
        '''Colition detection'''
        #Wall Colition
        if abs(snake.head.xcor()) >= 300 or abs(snake.head.ycor()) >= 300:
            scoreboard.game_over()
            game_is_on = False
            
        
        for segment in snake.body_segments[1:]:     
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False
                t.showturtle()
                

game_start()
while game_is_on == False:
        retry = mbox.askyesno(title= "Game over noob!", message= "Do you want to retry?" )
        if retry == False:
            s.bye()
            game_is_on = True
        else:
            s.resetscreen()
            s.clearscreen()
            
            game_start()

