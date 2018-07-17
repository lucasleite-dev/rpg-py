#Importações
from Classes.Jogador.Jogador import Jogador
from Classes.Inimigos.Inimigos import Rato
from Classes.Batalha.Batalha import batalha
from Classes.Itens.Poção import Poção
from random import randint
from time import sleep
import os
import platform

#Funções úteis
#Limpa a tela
def limparTela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def loading(mensagem, tempo):
    c = 0
    while c < len(mensagem):
        if mensagem[c] != '.':
            print(mensagem[c], end='', flush=True)
        else:
            sleep(tempo)
            print(mensagem[c], end='', flush=True)
        c += 1
    print("\n")

#Váriaveis
jogador = Jogador()
rato = Rato()
fim_de_jogo = False
jogador.name = input("Nome: ")
limparTela()
explorar = ""

while True:
    jogador.getStatus()
    print("+----------------------------------+")
    print("|               Menu               |")
    print("V----------------------------------V")
    print("| 1 - Explorar                     |")
    print("| 2 - Inventário                   |")
    print("| 3 - Sair do Jogo                 |")
    print("^----------------//----------------^")
    escolha = input("| ?: ")
    limparTela()
    if escolha == "1": #Carregamento de tela da Exploração
        jogador.getStatus()
        loading("Explorando...", 0.5)
        explorar = randint(1, 5) #gera um número aleátorio, se for 1,2,3 = fight com rato
        if explorar == 1 or explorar == 2 or explorar == 3: #Tela de combate
            limparTela()
            jogador.getStatus()
            rato.getStatus()
            print(f"Entrou em combate com um {rato.name}!")
            print(30*"-")
            while rato.status == "Vivo":
                print("1 - Lutar\n2 - Fugir.") #Menu de Ataques
                ataques = input()
                print(5*"=")
                #Ataque normal
                if ataques == "1":
                    limparTela()
                    batalha(jogador, rato)
                if ataques == "2":
                    limparTela()
                    print("Você fugiu do combate.")
                    jogador.vida = 100
                    jogador.mana = 100
                    break
                #Quando o jogador morre.
                if jogador.vida <=0:
                    print(f"{jogador.name} morreu!\nGAMER OVER")
                    fim_de_jogo = True
                    break
                #Quando inimigo morre.
                if rato.vida <=0:
                    rato.getStatus()
                    #print("O rato dropou 1 Poção")
                    #jogador.inventario += rato.drop
                    jogador.vida = 100
                    jogador.mana = 100
                    sleep(0.5)
                    limparTela()
        else:
            print("Nada foi encontrado.")
            sleep(1.5)
            limparTela()
        if rato.vida <= 0 and rato.status == "Morto":
            rato.vida = 50
            rato.status = "Vivo"
    if escolha == "2": #Carregamento da tela de inventario
        limparTela()
        loading("\nCarregando inventário...", 0.5)
        limparTela()
        jogador.getInventario()
        limparTela()
    if escolha == "3" or fim_de_jogo == True:
        break

print("Você saiu do Jogo!")
sleep(2)
