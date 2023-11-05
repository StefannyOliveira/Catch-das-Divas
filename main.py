from tupy import *
import level
import random


class Level(Image):
    def __init__(self):
        self.x = 450
        self.y = 252
        self.file = 'level.png'
            
tela = Level()

run(globals())
