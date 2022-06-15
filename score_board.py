from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto((0, 260))
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}",align="center",font=("Ariel", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.color("Red")
        self.goto((0, 210))
        self.write(f"Game over!" , align="center", font=("Ariel", 30, "bold"))



