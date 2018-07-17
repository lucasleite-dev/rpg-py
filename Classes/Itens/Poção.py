#Importações
from Classes.Jogador.Jogador import Jogador

#Variáveis
jogador = Jogador()

class Poção:

    def __init__(self, potion = 20):
        self.potion = potion
        if jogador.vida < 100:
            jogador.vida += potion
            if jogador.vida > 100:
                jogador.vida = 100
