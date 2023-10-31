from tupy import *

class Prova(Image):
    def __init__(self, x: int, y: int) -> None:
        self.file = "prova.png"
        self.x = x
        self.y = y
        self.vel = 10
    def update(self):
        if self.vel:
            self.y += self.vel
    def change_dif(self, dif):
        match dif:
            case "easy":
                self.vel = 10
            case "medium":
                self.vel = 15
            case "hard":
                self.vel = 20
class Player(Image):
    def __init__(self, x: int, y: int) -> None:
        self.file = "humandown.png"
        self.x = x
        self.y = y
        self.direction = ""
    def update(self):
        match self.direction:
            case "left":
                self.file = "humanleft.png"
            case "right":
                self.file = "humanright.png"
                
        if keyboard.is_key_down('Left'):
            self.direction = "left"
            self.x -= 15
        if keyboard.is_key_down('Right'):
            self.direction = "right"
            self.x += 15
            
Player = Player(450, 450)
Prova = Prova(450, 30)

run(globals())