#Importações
from Classes.Jogador.Jogador import Jogador
from Classes.Inimigos.Rato import Rato
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

#Mostra o status do jogador, nome;hp;mp;etc;
def statusJogador():
    print(7*"-")
    print("STATUS")
    print(7*"-")
    print(f"Nome: {jogador.name}")
    print(f"HP: {jogador.vida}")
    print(f"MP: {jogador.mana}")
    print(7*"-")

#Mostra o status do inimigo, nome;hp;mp;etc;
def statusInimigo():
    print(f"STATUS INIMIGO")
    print(7*"-")
    print(f"Nome: {rato.name}")
    print(f"HP: {rato.vida}")
    print(f"Estado: {rato.status}")
    print(7*"-")
    
#Mostra o combat log do ataque fraco
def combatLog():
    print("COMBAT LOG:")
    print(f"{jogador.name} atacou e causou {rato.levaDano(jogador.ataque)} de dano.")
    print(f"{jogador.name} recebeu {jogador.levaDano(rato.ataque)} de dano.")
    print(30*"-")

#Mostra o combat log do ataque forte
def combatLog2():
    print("COMBAT LOG:")
    print(f"{jogador.name} atacou e causou {rato.levaDano(jogador.ataque)* 2} de dano.")
    print(f"{jogador.name} recebeu {jogador.levaDano(rato.ataque)} de dano.")
    print(30*"-")

#Váriaveis
jogador = Jogador()
rato = Rato()
fim_de_jogo = False
jogador.name = input("Nome: ")
limparTela()

while True:
    statusJogador()
    print("MENU")
    print(7*"-")
    print("1 - Explorar 2 - Inventário 3 - Sair do Jogo")
    print("")
    #Menu
    escolha = input()
    limparTela()
    if escolha == "1": #Carregamento de tela da Exploração
        statusJogador()
        print("Explorando", end="", flush=True)
        sleep(1)
        print(".", end="", flush=True)
        sleep(1)
        print(".", end="", flush=True)
        sleep(1)
        print(".")
        explorar = randint(1, 5) #gera um número aleátorio, se for 1,2,3 = fight com rato
    """if escolha == "2":
        print("Carregando inventário", end="", flush=True)
        sleep(1)
        print(".", end="", flush=True)
        sleep(1)
        print(".", end="", flush=True)
        sleep(1)
        print(".")
        print(jogador.inventario)
        menuInventario = input("1 - Usar poção: ")
        if menuInventario == "1":
            jogador.inventario"""
    if escolha == "3" or fim_de_jogo == True:
        break
    if explorar == 1 or explorar == 2 or explorar == 3: #Tela de combate
        limparTela()
        statusJogador()
        statusInimigo()
        print(f"Entrou em combate com um {rato.name}!")
        print(30*"-")
        while rato.status == "Vivo":
            print("1 - Ataque Normal, Custo: 0 MP\n2 - Ataque Forte, Custo: 30 MP\n3 - Para fugir.") #Menu de Ataques
            ataques = input()
            print(5*"=")
            #Ataque normal
            if ataques == "1": #Ataques
                limparTela()
                #Quando o inimigo recebe dano
                rato.levaDano(jogador.ataque)
                #Quando o jogador recebe dano
                jogador.levaDano(rato.ataque)
                #Verifica a vida do jogador
                if jogador.vida > 0:
                    statusJogador()
                #Verifica se a vida do inimigo é maior que 0
                if rato.vida > 0:
                    statusInimigo()
                #Combate log
                combatLog()
            #Quando jogador usa ataque forte
            if ataques == "2":
                limparTela()
                rato.levaDano(jogador.ataque) * 2
                jogador.levaDano(rato.ataque)
                jogador.mana -= 30
                #Verifica a vida do jogador
                if jogador.vida > 0:
                    statusJogador()
                #Verifica se a vida do inimigo é maior que 0
                if rato.vida > 0:
                    statusInimigo()
                combatLog2()
            #Quando o jogador foge
            if ataques == "3":
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
                statusInimigo()
                #print("O rato dropou 1 Poção")
                #jogador.inventario += rato.drop
                jogador.vida = 100
                jogador.mana = 100
                limparTela()
    else:
        print("Nada foi encontrado.")
        sleep(1.5)
        limparTela()
    if rato.vida <= 0 and rato.status == "Morto":
        rato.vida = 50
        rato.status = "Vivo"
    
print("Você saiu do Jogo!")
sleep(2)
