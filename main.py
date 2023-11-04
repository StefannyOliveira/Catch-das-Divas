from tupy import *
import random

class Jogo(Image):
    def __init__(self):
        self.tela = 'telainicial.png'
    def telas(self):

class Item(Image):
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
    def __init__(self, x: int, velocidade: int) -> None:
        super().__init__('monster.png')
        self.x = x
        self.y = 0
        self.velocidade = velocidade
    
    def update(self):
    self.x = self.x - self.velocidade
    if self.x < -20:
      self.x = 820
    elif self.x > 820:
      self.x = -20
    if self._collides_with(bolha):
            


    def bateu(self):
    bolhas_a_remover = []
    for bolha in bolhas:
        if self._collides_with(bolha):
            bolha.x = 1000
            bolha.y = 1000
            bolha.velocidade = 0
            bolhas.remove(bolha)


  
class Fase:
  pass

#Lembrar de Arsenário e Trilha Sonora em, respectivamente, Jogo e Fase

            
Player = Player(450, 450)
Provas = [Prova(450, 0), 
          Prova(300, -200), 
          Prova(600, -400), 
          Prova(300, -600)]

run(globals())
