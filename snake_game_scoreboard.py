from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.write(f"score: {self.score}", align='center', font=('Ubuntu', 24, 'normal'))
    
