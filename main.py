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

class Monster(Image):
    def __init__(self, x: int) -> None:
        super().__init__('monster.png')
        self.x = x
        self.y = 0
        self.velocidade = 100
    
    def update(self):
        
            
Player = Player(450, 450)
Provas = [Prova(450, 0), 
          Prova(300, -200), 
          Prova(600, -400), 
          Prova(300, -600)]

run(globals())
