#Importações
from random import randint
from random import uniform

class Rato:

    def __init__(self, name="Rato", vida_max=50, vida=50, ataque=10, defesa=25, exp=15, status="Vivo"):
        self.name = name
        self.vida_max = vida_max
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.status = status
        self.exp = exp

    def levaDano(self, dano):
        self.vida -= int(dano / (1+self.defesa/100))
        if self.vida <= 0:
            self.status = "Morto"
            self.vida = 0
        return int(dano / (1+self.defesa/100))
