from tupy import *

class Prova(Image):
    def __init__(self, x: int, y: int) -> None:
        self.file = "prova.png"
        self.x = x
        self.y = y
        self.vel = 20
    def update(self):
        if self.vel:
            self.y += self.vel
class Player(Image):
    def __init__(self, x: int, y: int) -> None:
        self.file = "humandown.png"
        self.x = x
        self.y = y
        self.direction = ""
    def update(self):
        if self.direction == "left":
            self.file = "humanleft.png"
        if self.direction == "right":
            self.file = "humanright.png"
        if keyboard.is_key_down('Left'):
            self.direction = "left"
            self.x -= 20
        if keyboard.is_key_down('Right'):
            self.direction = "right"
            self.x += 20
Player = Player(450, 450)
Prova = Prova(450, 30)

run(globals())