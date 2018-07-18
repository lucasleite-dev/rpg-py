#Importações
from random import randint
from random import uniform
from time import sleep
import platform
import os

#Limpa a tela
def limparTela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

class Jogador:

    def __init__(self, level=1, vida=300, vida_max=300, mana=150, mana_max=150,ataque=55,defesa=110, status="Vivo", name="", classe=""):
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
        self.classe = classe

    def levaDano(self, dano):
        self.vida -= int(dano / (1+self.defesa/100))
        if self.vida <= 0:
            self.vida = 0
            self.status = "Morto"
        return int(dano / (1+self.defesa/100))


    # Mostra o status do jogador, nome;hp;mp;etc;
    def getStatus(self):
        print("+----------------------------------+")
        print("|              Status              |")
        print("V----------------------------------V")
        print(f"| Nome  : {self.name}" + " "*(25-len(self.name)) + "|")
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
        else:
            for key in self.inventario:
                resto = (30-len(key))-len(str(self.inventario[key]))
                print(f"| {key} : {self.inventario[key]}" + " "*resto + "|")
            print("+----------------------------------+")
            print("| 1 - Para voltar                  |")
            print("| 2 - Para usar algum item         |")
            print("^----------------//----------------^")
            escolha = input("| ?: ")
            while escolha != "1" and escolha != "2":
                print("Opção inválida")
                escolha = input("| ?: ")
            if escolha == "1":
                pass
            else:
                self.menuItens()

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
            else:
                print("V----------------------------------V")
                print("|          Sem unidades.           |")
                print("^----------------//----------------^")
                sleep(1)


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
            else:
                print("V----------------------------------V")
                print("|          Sem unidades.           |")
                print("^----------------//----------------^")
                sleep(1)

    # Menu para usar itens
    def menuItens(self):
        menu = True
        while menu:
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
                key = "Poção de Vida"
                resto = (26-len(key))-len(str(self.inventario[key]))
                print(f"| 1 - {key} : {self.inventario[key]}" + " "*resto + "|")
                key2 = "Poção de Mana"
                resto = (26-len(key2))-len(str(self.inventario[key2]))
                print(f"| 2 - {key2} : {self.inventario[key2]}" + " "*resto + "|")
                print("+----------------------------------+")
                print("| Selecione uma opção              |")
                print("^----------------//----------------^")
                escolha = input("| ?: ")
                if escolha == '1':
                    self.pocaoVida()
                    break
                elif escolha == '2':
                    self.pocaoMana()
                    break
                else:
                    print("+----------------------------------+")
                    print("|             Inválido             |")
                    print("^----------------//----------------^")

    def getLevel(self):
        if self.exp >= self.exp_max:
            self.level += 1
            self.exp -= self.exp_max
            self.exp_max = round(self.exp_max * 1.5)
            self.vida_max += 10
            self.mana_max += 5
            self.vida = self.vida_max
            self.mana = self.mana_max
            self.getStatus()
            print(12*"*"+"  LEVEL UP  "+"*"*12)
            sleep(1.5)
            print("+----------------------------------+")
            print("| Pressione enter para voltar      |")
            print("^----------------//----------------^")
            input("")
            limparTela()