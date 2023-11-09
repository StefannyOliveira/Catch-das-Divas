from tupy import *
import random
import os

class TelaInicial(BaseImage):

    def __init__(self) -> None:
        super().__init__(file = 'telainicial.png', x = 450, y= 250)
        self._facil = False
        self._medio = False
        self._dificil = False
        self._fim = False

class Personagem(Image):
    def __init__(self, x: float, y: float, file = str) -> None:
        self.x = x
        self.y = y
        self.angle = 0
        self.pulando = 0
        self.pulo = False
        self.file = 'humandown.png'

    def update(self) -> None:
        if keyboard.is_key_down('Left'):
            self.file = 'humanleft.png'
            self.x -= 15
        elif keyboard.is_key_down('Right'):
            self.file = 'humanright.png'
            self.x += 15
        elif keyboard.is_key_just_down('space'):
            self.pulo = True
            self.pulando += 1
        elif self.pulo:
            if self.pulando <= 3:
               self.pulando += 1
               self.y -= 15
            elif self.pulando < 8:
                self.pulando += 1
            elif self.pulando == 8:
                self.pulando += 1
                self.y += 15
            elif self.pulando == 9:
                self.pulando += 1
                self.y += 15
            elif self.pulando == 10:
                self.pulando = 0
                self.pulo = False
                self.y += 15           
        else:
            self.file = 'humandown.png' 

class Monstro(Image):
    def __init__(self) -> None:
        self.x = 10
        self.y = 20
        self._file = 'monstro.png'
        self.__velocidade = 40

    @property
    def velocidade(self) -> float:
        return self.__velocidade
    #Método de leitura da velocidade.

    @velocidade.setter
    def velocidade(self, valor: float) -> None:
        self.__velocidade = valor
    #Método de definição da velocidade.

    def update(self) -> None:
        if self.x > 820:
            return False
        self.x += self.velocidade
    #Método que atualiza a taxa de pixels dos itens.

    def _collides_with(self, other: TupyObject) -> bool:
        return super()._collides_with(other)
    
    def collides_with(self, other: TupyObject) -> bool:
        return super()._collides_with(other)
    

class Item(Image):
    def __init__(self, x: float, y: float, file: str, velocidade: float, angle: int) -> None:
        self.x = x
        self.y = y
        self._file = str
        self.__velocidade = velocidade
        self._angle = angle
        self._hide()
    #Método inicial que armazena a posição e velocidade dos itens que caem no jogo.

    @property
    def velocidade(self) -> float:
        return self.__velocidade
    #Método de leitura da velocidade.
    
    @velocidade.setter
    def velocidade(self, valor: float) -> None:
        self.__velocidade = valor
    #Método de definição da velocidade.

    def update(self) -> None:
        if self.y > 520:
            return False
        self.y += self.velocidade
    #Método que atualiza a taxa de pixels dos itens.

class Recorde(Label):

    def __init__(self) -> None:
        super().__init__('Recorde: 0', 500, 9, font='Times New Roman 30', color='yellow')
        self.__recorde = 0
        self.__maiorrecorde = 0

        #Método inicial, herdando funções da classe Label do Tupy, que imprime a pontuação atualizada na tela
    
    def aumenta(self, pontos: int) -> None:
        self.__recorde += pontos
        self.text = f'Pontuação: {self.__score}'

        if self.__recorde > self.__maiorrecorde:
            self.__maiorrecorde = self.__recorde
        
        #Método que atualiza a pontuação aumentando.

    def diminui(self, pontos: int) -> None:
        self.__recorde -= pontos
        self.text = f'Pontuação: {self.__score}'

        #Método que atualiza a pontuação diminuindo.

menu1 = TelaInicial()
if keyboard.is_key_just_down('space'):
    menu1.file = 'level.png'

if (keyboard.is_key_just_down(1) or
   keyboard.is_key_just_down(2) or 
   keyboard.is_key_just_down(3)):
    pass
     


# personagem = Personagem(180, 410)


run(globals())