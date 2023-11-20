from turtle import Turtle
from constants import *


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=SCREEN_HEIGHT/2-SCORE_TOP_GAP)
        self.color(FONT_COLOR)

        self.score = [0, 0]
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f'{self.score[0]}  {self.score[1]}', align='center', font=BIG_FONT)

    def player_point(self, player):
        idx = 0
        if player.side == 'right':
            idx = 1
        self.score[idx] += 1
        self.show_score()

    def check_winner(self):
        if WIN in self.score:
            if self.score[1] == WIN:
                self.goto(x=150, y=0)
            else:
                self.goto(x=-150, y=0)
            self.write(arg='You Win!', align='center', font=FONT)
            return True

        return False
