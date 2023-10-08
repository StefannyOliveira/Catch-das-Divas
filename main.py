from tupy import *


'''Cria um plano de fundo preto'''
class Background(Image):
    def __init__(self, x: int, y: int) -> None:
        self.file = "black-background.png"
        self.x = x
        self.y = y

class Child(Image):
    def __init__(self, x: int, y: int) -> None:
        self.file = "humandown.png"
        self.x = x
        self.y = y
        self.direction = "down"
        self.collide = False
    def update(self):
        if self.direction == 'left':
            self.file = 'humanleft.png'
        if self.direction == 'up':
            self.file = 'humanup.png'
        if self.direction == 'right':
            self.file = 'humanright.png'
        if self.direction == 'down':
            self.file = 'humandown.png'
        
        if keyboard.is_key_just_down('Left') and not self.collide:
            self.direction = "left"
            self.x -= 20
        if keyboard.is_key_just_down('Right') and not self.collide:
            self.direction = "right"
            self.x += 20
        if keyboard.is_key_just_down('Up') and not self.collide:
            self.direction = "up"
            self.y -= 20
        if keyboard.is_key_just_down('Down') and not self.collide:
            self.direction = "down"
            self.y += 20
    def collides_with(self):
        if super()._collides_with(Background) is True:
            self.collide = True
Child = Child(70, 150)
Background = Background(450, 250)

run(globals())