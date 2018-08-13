#Importações
from time import sleep
import os
import platform

#Variáveis

def limparTela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def combatLog(jogador, inimigo, forca=1):
    danoJogador = 0
    danoInimigo = 0
    print("+----------------------------------+")
    print("|            Combat Log            |")
    print("V----------------------------------V")
    print(f"| {jogador.name} atacou e causou {danoJogador*forca} de dano.")
    print(f"| {jogador.name} recebeu {danoInimigo} de dano.")
    print("^----------------//----------------^")

def verificaStatus(jogador, inimigo):
        jogador.getStatus()
        inimigo.getStatus()

def batalha(jogador, inimigo):
    while inimigo.status == "Vivo":
        limparTela()
        verificaStatus(jogador,inimigo)
        print("+----------------------------------+")
        print("|               Menu               |")
        print("V----------------------------------V")
        print("| 1 - Ataque Normal (00 MP)        |")
        print("| 2 - Ataque Forte  (30 MP)        |")
        print("| 3 - Usar item                    |")
        print("^----------------//----------------^")
        escolha_ataque = input("| ?: ")
        print(20*"=")
        if escolha_ataque == "1":
            inimigo.levaDano(jogador.ataque)#Quando o inimigo recebe dano
            jogador.levaDano(inimigo.ataque)#Quando o jogador recebe dano
        elif escolha_ataque == "2":
            if jogador.mana < 30: # Mana insuficiente para o ataque
                print("Mana insuficiente")
                sleep(0.5)
            else:
                inimigo.levaDano(jogador.ataque*2)#Quando o inimigo recebe dano
                jogador.levaDano(inimigo.ataque)#Quando o jogador recebe dano
                jogador.mana -= 30
        elif escolha_ataque == "3":
            limparTela()
            jogador.menuItens()

    if inimigo.status == "Morto":
        limparTela()
        jogador.exp += inimigo.exp
        verificaStatus(jogador,inimigo)
        limparTela()
        print("Inimigo dropou:")
        for item in inimigo.drop:
            print(item)
            print("1 - para pegar")
            print("2 - para largar")
            decisao = input("|? : ")
            if decisao == '1':
                if len(jogador.inventario) < 20:
                    if item in jogador.inventario:
                        jogador.inventario[item] += 1
                    else:
                        jogador.inventario[item] = 1
                else:
                    print("Inventário cheio.")
                    pass
            elif decisao == '2': 
                pass
            limparTela()
        #combatLog(jogador, inimigo)
        print("+----------------------------------+")
        print("| Pressione enter para voltar      |")
        print("^----------------//----------------^")
        input("")
        limparTela()
