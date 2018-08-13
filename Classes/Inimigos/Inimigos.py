#Importações
from random import randint
from random import uniform
class Inimigo:

    def __init__(self, nome, vida=150, vida_max = 150,ataque=25, defesa=100, exp=35, status="Vivo", drop={}):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida_max
        self.ataque = ataque
        self.defesa = defesa
        self.status = status
        self.exp = exp
        self.drop = drop

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
        print(f"| Nome  : {self.nome}" + " "*(25-len(self.nome)) + "|")
        print(f"| HP    : {self.vida}" + f"/{self.vida_max}" + " "*(24-len(str(self.vida))-len(str(self.vida_max))) + "|")
        print(f"| Exp   : {self.exp}" + " "*(25-len(str(self.exp))) + "|")
        print(f"| Estado: {self.status}" + " "*(25-len(str(self.status))) + "|")
        print("^----------------//----------------^")

class Skelet(Inimigo):

    def __init__(self):
        super().__init__("Skelet", drop={'Poção de Vida':1})

class Bear_Zombie(Inimigo):

    def __init__(self):
        super().__init__("Bear Zombie", vida=225, vida_max=225, ataque=50, defesa=150, exp=75, drop={'Poção de Vida':1, 'Poção de Mana':1})

class Demon(Inimigo):

    def __init__(self):
        super().__init__("Demon", vida=400, vida_max=400, ataque=100, defesa=190, exp=150, drop={'Poção de Vida':1, 'Poção de Mana':1, 'Sword of Demon':1})
