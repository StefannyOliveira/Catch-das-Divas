from tupy import *


'''Cria um plano de fundo preto'''
class Background(Image):
    def __init__(self, x: int, y: int) -> None:
        self.file = "black-background.png"
        self.x = x
        self.y = y


Background = Background(450, 250)

run(globals())