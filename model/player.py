from helpers import *
from model.paddle import Paddle


class Player:
    def __init__(self, side):
        self.side = side
        if side == 'right':
            self.xcor = SCREEN_WIDTH/2 - PADDLE_GAP
            self.point_bound = -SCREEN_WIDTH/2
        else:
            self.xcor = PADDLE_GAP - SCREEN_WIDTH / 2
            self.point_bound = SCREEN_WIDTH / 2
        self.paddle = Paddle(self.xcor)
        self.sound = 'life'

    def up(self):
        if self.paddle.ycor() + PADDLE_HEIGHT/2 < SCREEN_HEIGHT/2:
            self.paddle.forward(PADDLE_SPEED)

    def down(self):
        if self.paddle.ycor() - PADDLE_HEIGHT / 2 > -SCREEN_HEIGHT / 2:
            self.paddle.backward(PADDLE_SPEED)

    def check_life(self, ball):
        result = is_close(ball.xcor(), self.point_bound)
        if result:
            audio.play(self.sound)
        return result
