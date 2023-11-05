from tupy import *

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