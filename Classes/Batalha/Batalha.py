
def batalha(jogador, inimigo):
    while inimigo.status == "Vivo":
        inimigo.levaDano(jogador.ataque)
        #Quando o jogador recebe dano
        jogador.levaDano(inimigo.ataque)
        #Verifica a vida do jogador
        if jogador.vida > 0:
            jogador.getStatus()
        #Verifica se a vida do inimigo é maior que 0
        if rato.vida > 0:
            rato.getStatus()
        #Combate log
        combatLog()

def combatLog(jogador, inimigo, forca=1):
    print("+----------------------------------+")
    print("|            Combat Log            |")
    print("V----------------------------------V")
    print(f"| {jogador.name} atacou e causou {inimigo.levaDano(jogador.ataque)*forca} de dano.")
    print(f"| {jogador.name} recebeu {jogador.levaDano(inimigo.ataque)} de dano.")
    print("^----------------//----------------^")
