#Importações
from random import randint
from random import uniform

class Jogador:

    def __init__(self, level=1, vida=300, vida_max=300, mana=150, mana_max=150,ataque=55,defesa=110, status="Vivo", name=""):
        self.level = level
        self.exp = 0
        self.exp_max = round(75)
        self.vida_max = vida_max
        self.vida = vida
        self.mana = mana
        self.mana_max = mana_max
        self.ataque = ataque
        self.defesa = defesa
        self.status = status
        self.inventario = {"Poção de Mana": 2, "Poção de Vida": 3}
        self.name = name

    def levaDano(self, dano):
        self.vida -= int(dano / (1+self.defesa/100))
        if self.vida <= 0:
            self.vida = 0
            self.status = "Morto"
        return int(dano / (1+self.defesa/100))

    def getInventario(self): # Função para retornar os itens do inventário
        print("+----------------------------------+")
        print("|            Inventário            |")
        print("V----------------------------------V")
        if self.inventario == {}:
            print("| [Vazio]                          |")
        else:
            for key in self.inventario:
                resto = (30-len(key))-len(str(self.inventario[key]))
                print(f"| {key} : {self.inventario[key]}" + " "*resto + "|")
        print("+----------------------------------+")
        print("| Pressione enter para voltar      |")
        print("^----------------//----------------^")
        input("")

    # Mostra o status do jogador, nome;hp;mp;etc;
    def getStatus(self):
        print("+----------------------------------+")
        print("|              Status              |")
        print("V----------------------------------V")
        print(f"| Nome : {self.name}" + " "*(26-len(self.name)) + "|")
        print(f"| HP   : {self.vida}" + f"/{self.vida_max}" + " "*(22-len(str(self.vida))) + "|")
        print(f"| MP   : {self.mana}" + f"/{self.mana_max}" +  " "*(22-len(str(self.mana))) + "|")
        print(f"| Exp  : {self.exp}" + f"/{self.exp_max}" + " "*(23-len(str(self.exp))) + "|")
        print(f"| Level: {self.level}" + " "*(26-len(str(self.level))) + "|")
        print("^----------------//----------------^")
