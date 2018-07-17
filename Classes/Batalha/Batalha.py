#Importações
import os
import platform

def limparTela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def combatLog(jogador, inimigo, forca=1):
    print("+----------------------------------+")
    print("|            Combat Log            |")
    print("V----------------------------------V")
    print(f"| {jogador.name} atacou e causou {inimigo.levaDano(jogador.ataque)*forca} de dano.")
    print(f"| {jogador.name} recebeu {jogador.levaDano(inimigo.ataque)} de dano.")
    print("^----------------//----------------^")

def verificaStatus(jogador, inimigo):
        jogador.getStatus()
        inimigo.getStatus()

def batalha(jogador, inimigo):
    while inimigo.status == "Vivo":
        verificaStatus(jogador,inimigo)
        print("+----------------------------------+")
        print("|               Menu               |")
        print("V----------------------------------V")
        print(f"1 - Ataque Normal : 0 MP\n2 - Ataque Forte : 30 MP")
        escolha_ataque = input("| ?: ")
        print(5*"=")
        limparTela()
        if escolha_ataque == "1":
            inimigo.levaDano(jogador.ataque)#Quando o inimigo recebe dano
            jogador.levaDano(inimigo.ataque)#Quando o jogador recebe dano
            verificaStatus(jogador, inimigo)
            combatLog(jogador, inimigo)
        elif escolha_ataque == "2":
            inimigo.levaDano(jogador.ataque * 2)#Quando o inimigo recebe dano
            jogador.levaDano(inimigo.ataque)#Quando o jogador recebe dano
            jogador.mana -= 30
            verificaStatus(jogador, inimigo)
            combatLog(jogador, inimigo)        
    if inimigo.status == "Morto":
        verificaStatus(jogador,inimigo)
        combatLog(jogador, inimigo)
        print("+----------------------------------+")
        print("| Pressione enter para voltar      |")
        print("^----------------//----------------^")
        e = input("")
        limparTela()
