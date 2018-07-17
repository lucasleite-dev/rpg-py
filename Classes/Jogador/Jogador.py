#Importações
from random import randint
from random import uniform

class Jogador:

    def __init__(self, vida_max=100, vida=100, mana=100, ataque=15,defesa=50, status="Vivo", name=""):
        self.vida_max = vida_max
        self.vida = vida
        self.mana = mana 
        self.ataque = ataque
        self.defesa = defesa
        self.status = status
        self.inventario = {}
        self.name = name

    def levaDano(self, dano):
        self.vida -= int(dano / (1+self.defesa/100))
        if self.vida <= 0:
            self.vida = 0
            self.status = "Morto"
        return int(dano / (1+self.defesa/100))
