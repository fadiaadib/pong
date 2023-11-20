from tkinter import TclError
from turtle import Screen
import time

from helpers import *
from model.field import Field
from model.ball import Ball
from model.player import Player
from model.score_board import ScoreBoard


class Pong:
    def __init__(self):
        # Set up the screen
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor(BG_COLOR)
        self.screen.title(TITLE)

        # Create objects
        self.field = Field()
        self.ball = Ball()
        self.score_board = ScoreBoard()
        self.players = []
        self.players.append(Player('left'))
        self.players.append(Player('right'))

        # Create listeners
        self.key_bindings()

        # Start game
        try:
            self.play()
            self.screen.exitonclick()
        except TclError:
            pass

    def key_bindings(self):
        self.screen.listen()
        self.screen.onkey(self.players[1].up, 'Up')
        self.screen.onkey(self.players[1].down, 'Down')
        self.screen.onkey(self.players[0].up, 'w')
        self.screen.onkey(self.players[0].down, 's')

    def play(self):
        on = True
        while on:
            self.screen.update()
            time.sleep(REFRESH_PERIOD)

            # Move ball
            self.ball.move()

            # Bounce wall
            self.ball.bounce_wall()
            for player in self.players:
                # Bounce paddle
                self.ball.bounce_paddle(player)

                # Check point
                if is_close(self.ball.xcor(), player.point_bound):
                    self.score_board.player_point(player)
                    self.ball.restart()
                    self.screen.update()
                    if self.score_board.check_winner():
                        on = False
                        break
                    else:
                        time.sleep(RESTART_PERIOD)


if __name__ == '__main__':
    Pong()
