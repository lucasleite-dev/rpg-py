#Importações
from random import randint
from random import uniform

class Jogador:

    def __init__(self, vida=300, vida_max = 300,mana=150, ataque=55,defesa=110, status="Vivo", name=""):
        self.vida_max = vida_max
        self.vida = vida
        self.mana = mana
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
        e = input("")

    # Mostra o status do jogador, nome;hp;mp;etc;
    def getStatus(self):
        teste = str(self.vida)
        print("+----------------------------------+")
        print("|              Status              |")
        print("V----------------------------------V")
        print(f"| Nome: {self.name}" + " "*(27-len(self.name)) + "|")
        print(f"| HP  : {self.vida}" + f"/{self.vida_max}" + " "*(23-len(str(self.vida))) + "|")
        print(f"| MP  : {self.mana}" + " "*(27-len(str(self.mana))) + "|")
        print("^----------------//----------------^")
