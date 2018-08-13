#Importações
from random import randint
from random import uniform
from time import sleep
import platform
import os
from Classes.Item import Item

#Limpa a tela
def limparTela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

class Jogador:

    def __init__(self, level=1, vida=0, vida_max=0, mana=0, mana_max=0,ataque=0, ataque_magico=0,defesa=0, status='Vivo', nome='', classe=''):
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
        self.inventario = {}
        self.nome = nome
        self.classe = classe

    def levaDano(self, dano):
        self.vida -= int(dano / (1+self.defesa/100))
        if self.vida <= 0:
            self.vida = 0
            self.status = 'Morto'
        return int(dano / (1+self.defesa/100))


    # Mostra o status do jogador, nome;hp;mp;etc;
    def getStatus(self):
        print("+----------------------------------+")
        print("|              Status              |")
        print("V----------------------------------V")
        print(f"| Nome  : {self.nome}" + " "*(25-len(self.nome)) + "|")
        print(f"| HP    : {self.vida}" + f"/{self.vida_max}" + " "*(24-len(str(self.vida))-len(str(self.vida_max))) + "|")
        print(f"| MP    : {self.mana}" + f"/{self.mana_max}" +  " "*(24-len(str(self.mana))-len(str(self.mana_max))) + "|")
        print(f"| Exp   : {self.exp}" + f"/{self.exp_max}" + " "*(24-len(str(self.exp))-len(str(self.exp_max))) + "|")
        print(f"| Level : {self.level}" + " "*(25-len(str(self.level))) + "|")
        print(f"| Classe: {self.classe}" + " "*(25-len(self.classe)) + "|")
        print("^----------------//----------------^")

    def getInventario(self): # Função para retornar os itens do inventário
        print("+----------------------------------+")
        print("|            Inventário            |")
        print("V----------------------------------V")
        if self.inventario == {}:
            print("| [Vazio]                          |")
            print("+----------------------------------+")
            print("| Pressione enter para voltar      |")
            print("^----------------//----------------^")
            input("")
        else:
            for key in self.inventario:
                resto = (30-len(key))-len(str(self.inventario[key]))
                print(f"| {key} : {self.inventario[key]}" + " "*resto + "|")
            print("+----------------------------------+")
            print("| 1 - Para usar algum item         |")
            print("| 2 - Para voltar                  |")
            print("^----------------//----------------^")
            escolha = input("| ?: ")
            while escolha != "1" and escolha != "2":
                print("Opção inválida")
                escolha = input("| ?: ")
            if escolha == "1":
                self.menuItens()
            else:
                pass

    # Poções
    def pocaoVida(self): # VIDA
        if self.vida == self.vida_max:
            print("V----------------------------------V")
            print("|     Sua vida já está no max.     |")
            print("^----------------//----------------^")
            sleep(1)
        elif self.vida < self.vida_max:
            if self.inventario["Poção de Vida"] != 0:
                self.vida += 50
                if self.vida > self.vida_max:
                    self.vida = self.vida_max
                self.inventario["Poção de Vida"] -= 1

    def pocaoMana(self): # MANA
        if self.mana == self.mana_max:
            print("V----------------------------------V")
            print("|     Sua mana já está no max.     |")
            print("^----------------//----------------^")
            sleep(1)
        elif self.mana < self.mana_max:
            if self.inventario["Poção de Mana"] != 0:
                self.mana += 50
                if self.mana > self.mana_max:
                    self.mana = self.mana_max
                self.inventario["Poção de Mana"] -= 1
                if self.inventario["Poção de Mana"] == 0:
                    del(self.inventario["Poção de Mana"])

    # Menu para usar itens
    def menuItens(self):
        menu = True
        while menu:
            limparTela()
            self.getStatus()
            print("+----------------------------------+")
            print("|            Usar Item             |")
            print("V----------------------------------V")
            if self.inventario == {}:
                print("| [Vazio]                          |")
                print("+----------------------------------+")
                print("| Pressione enter para voltar      |")
                print("^----------------//----------------^")
                input("")
                menu = False
            else:
                for key, item in enumerate(self.inventario):
                    resto = (26-len(item))-len(str(self.inventario[item]))
                    print(f"| {key} - {item} : {self.inventario[item]}" + " "*resto + "|")
                print("+----------------------------------+")
                print("| Selecione uma opção              |")
                print("^----------------//----------------^")
                escolha = int(input("| ?: "))
                if list(self.inventario.keys())[escolha] == 'Poção de Vida':
                    self.pocaoVida()
                    limparTela()
                elif list(self.inventario.keys())[escolha] == 'Poção de Mana':
                    self.pocaoMana()
                    limparTela()
                elif escolha == '666':
                    break
                else:
                    print("+----------------------------------+")
                    print("|             Inválido             |")
                    print("^----------------//----------------^")

    def getLevel(self):
        if self.exp >= self.exp_max and self.status == 'Vivo':
            self.level += 1
            self.exp -= self.exp_max
            self.exp_max = round(self.exp_max * 1.5)
            self.vida_max += 10
            self.mana_max += 5
            self.vida = self.vida_max
            self.mana = self.mana_max
            self.ataque += 5
            self.defesa += 5
            self.getStatus()
            print(12*"*"+"  LEVEL UP  "+"*"*12)
            sleep(1.5)
            print("+----------------------------------+")
            print("| Pressione enter para voltar      |")
            print("^----------------//----------------^")
            input("")
            limparTela()

class Espadachim(Jogador):

    def __init__(self):
        super().__init__(classe='Espadachim', vida=220, vida_max=220, mana=190, mana_max=190,ataque=75,defesa=100)

class Mago(Jogador):

    def __init__(self):
        super().__init__(classe='Mago', vida=150, vida_max=150, mana=300, mana_max=200,ataque=25, ataque_magico = 100,defesa=80)

class Arqueiro(Jogador):

    def __init__(self):
        super().__init__(classe='Arqueiro', vida=175, vida_max=175, mana=150, mana_max=150,ataque=85,defesa=90)

class Tanker(Jogador):

    def __init__(self):
        super().__init__(classe='Tanker', vida=300, vida_max=300, mana=125, mana_max=125,ataque=55,defesa=120)
