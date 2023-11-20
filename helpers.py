import pygame
from constants import *


def is_close(a, b, precision=5):
    return b - precision <= a <= b + precision


class Audio:
    def __init__(self):
        self.mixer = pygame.mixer
        self.mixer.init()

    def play(self, file):
        if SOUND_ON:
            self.mixer.music.load(f'./audio/{file}.wav')
            self.mixer.music.play(loops=0)


audio = Audio()
