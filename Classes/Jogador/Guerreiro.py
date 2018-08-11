class Guerreiro:

    def __init__(self, level=1, vida=300, vida_max=300, mana=150, mana_max=150,ataque=55,defesa=110, status='Vivo', nome='', classe='Guerreiro'):
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
        self.nome = nome
        self.classe = classe