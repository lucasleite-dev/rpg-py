#Importações
from random import randint
from random import uniform

class Inimigo:

    def __init__(self, name, vida=150, vida_max = 150,ataque=25, defesa=100, exp=35, status="Vivo"):
        self.name = name
        self.vida = vida
        self.vida_max = vida_max
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
        print(f"| HP    : {self.vida}" + f"/{self.vida_max}" + " "*(24-len(str(self.vida))-len(str(self.vida_max))) + "|")
        print(f"| Exp   : {self.exp}" + " "*(25-len(str(self.exp))) + "|")
        print(f"| Estado: {self.status}" + " "*(25-len(str(self.status))) + "|")
        print("^----------------//----------------^")

class Rato(Inimigo):

    def __init__(self):
        super().__init__("Rato")

class Urso(Inimigo):

    def __init__(self):
        super().__init__("Urso", vida=225, vida_max=225, ataque=50, defesa=150, exp=75)
