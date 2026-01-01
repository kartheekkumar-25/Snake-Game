from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0,260)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"SCORE:{self.score}",move=False,align="center",font=("Arial",15,"normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 20, "bold"))