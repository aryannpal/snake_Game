from turtle import Turtle
ALIGNMENT="center"
FONT=('Courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.highscore=0
        with open("data.txt",mode="r") as file:
            self.highscore=int(file.read())
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=268)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(align=ALIGNMENT, arg=f"Score : {self.score} Highscore : {self.highscore}", font=FONT)


    def change_score(self):
        self.score+=1

        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode='w') as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()








