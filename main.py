from tkinter import TclError
from turtle import Screen
import time

from helpers import *
from model.board import Board
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
        self.board = Board()
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
        self.screen.onkey(self.players[0].up, 'w')
        self.screen.onkey(self.players[0].down, 's')
        self.screen.onkey(self.players[1].up, 'Up')
        self.screen.onkey(self.players[1].down, 'Down')

    def play(self):
        on = True
        while on:
            self.screen.update()
            time.sleep(REFRESH_PERIOD)

            # Move ball
            self.ball.move()

            # Bounce wall
            if self.board.check_bounce(self.ball):
                self.ball.bounce('h')

            for player in self.players:
                # Bounce paddle
                if player.paddle.check_bounce(self.ball):
                    self.ball.bounce('v')

                # Check life
                if player.check_life(self.ball):
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
