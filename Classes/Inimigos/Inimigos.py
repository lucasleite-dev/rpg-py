#Importações
from random import randint
from random import uniform

class Inimigo:

    def __init__(self, name, vida_max=50, vida=50, ataque=10, defesa=25, exp=15, status="Vivo"):
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

    def getStatus(self):
        print("+----------------------------------+")
        print("|           Status Inimigo         |")
        print("V----------------------------------V")
        print(f"| Nome  : {self.name}" + " "*(25-len(self.name)) + "|")
        print(f"| HP    : {self.vida}" + " "*(25-len(str(self.vida))) + "|")
        print(f"| Estado: {self.status}" + " "*(25-len(self.status)) + "|")
        print("^----------------//----------------^")

class Rato(Inimigo):

    def __init__(self):
        super().__init__("Rato")

class Urso(Inimigo):

    def __init__(self):
        super().__init__("Urso")
