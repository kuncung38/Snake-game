from turtle import Turtle, Screen

s = Screen()

ALIGNMENT = "right"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.setpos(x=280, y = 270)
        self.write(f"Score : {self.score}", False, ALIGNMENT, font=FONT)
        

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", False, ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, "center", font=('Courier', 15, 'bold'))  
           