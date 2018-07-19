#Importações
from Classes.Jogador.Jogador import Jogador
from Classes.Batalha.Batalha import batalha
#Importações de monstros
from Classes.Inimigos.Inimigos import Rato
from Classes.Inimigos.Inimigos import Urso

# Bibliotecas padrão
from random import randint
from time import sleep
import os
import platform
import sqlite3

#Variáveis SQL
conexão = sqlite3.connect('personages.db') #Conecta no Banco de dados
cursor = conexão.cursor() #comando cursor
#Váriaveis
jogador = Jogador()
fim_de_jogo = False
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

def criar_tabela():#Cria uma tabela
    cursor.execute("CREATE TABLE IF NOT EXISTS personagens (nome text, level integer, exp integer, exp_max integer, vida integer, vida_max integer, mana integer, mana_max integer, ataque integer, defesa integer, status text, classe text)")

#Insere o novo char no banco de dados
def inserir_na_tabela(jogador):
    cursor.execute("""
        INSERT INTO personagens (nome, level, exp, exp_max, vida, vida_max, mana, mana_max, ataque, defesa, status, classe)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """, (jogador.name, jogador.level, jogador.exp, jogador.exp_max, jogador.vida, jogador.vida_max, jogador.mana, jogador.mana_max, jogador.ataque, jogador.defesa, jogador.status, jogador.classe))
    conexão.commit()

#Atualiza o jogador na tabela quando o jogador escolher Salvar no menu.
def atualizar_tabela(jogador):
    cursor.execute("""
        UPDATE personagens
        SET level = ?, exp = ?, exp_max = ?, vida = ?, vida_max = ?, mana = ?, mana_max = ?, ataque = ?, defesa = ?, status = ?
        WHERE nome = ?
        """, (jogador.level, jogador.exp, jogador.exp_max, jogador.vida, jogador.vida_max, jogador.mana, jogador.mana_max, jogador.ataque, jogador.defesa, jogador.status, jogador.name))
    conexão.commit()
#Tela inicial.
print("+----------------------------------+")
print("|             RPG-PY               |")
print("^----------------//----------------^")
print("+----------------------------------+")
print("|         Pressione Enter          |")
print("^----------------//----------------^")
input("")
limparTela()
#Menu Inicial
print("+----------------------------------+")
print("|               Menu               |")
print("V----------------------------------V")
print("| 1 - Criar personagem             |")
print("| 2 - Selecionar personagem        |")
print("^----------------//----------------^")
escolhaMenu = input("| ?: ")
limparTela()
#Criação de Personagem
if escolhaMenu == "1":
    print("+----------------------------------+")
    print("|       Criação de Personagem      |")
    print("V----------------------------------V")
    jogador.name = input('Nome: ')
    print("Classes: \n1 - Guerreiro")
    escolhaClasse = input('| ?:')
    if escolhaClasse == '1':
        jogador.classe = 'Guerreiro'
        criar_tabela()
        inserir_na_tabela(jogador)
        print("Personagem criado com sucesso.")
#Escolhe o personagem "Ainda n ta pronto, apenas mostra todos os personagens salvos no banco"
elif escolhaMenu == "2":
    cursor.execute("""
    SELECT nome FROM personagens;
    """)
    for linha in cursor.fetchall():
        print(linha)
    input("")
limparTela()
explorar = ""
inimigo = ""
combate = False

while True:
    jogador.getStatus()
    print("+----------------------------------+")
    print("|               Menu               |")
    print("V----------------------------------V")
    print("| 1 - Explorar                     |")
    print("| 2 - Inventário                   |")
    print("| 3 - Salvar                       |")
    print("| 4 - Sair do Jogo                 |")
    print("^----------------//----------------^")
    escolha = input("| ?: ")
    limparTela()
    if escolha == "1": #Carregamento de tela da Exploração
        jogador.getStatus()
        loading("Explorando...", 0.5)
        explorar = randint(1, 5) #gera um número aleátorio, se for 1,2,3 = fight com rato
        if explorar <= 3: #Declara que o inimigo é um Rato
            inimigo = Rato()
            combate = True
        elif explorar == 4: #Declara que o inimigo é um Urso
            inimigo = Urso()
            combate = True
        if combate == True: #Tela de Combate
            limparTela()
            jogador.getStatus()
            inimigo.getStatus()
            print(f"Entrou em combate com um {inimigo.name}!")
            print(30*"-")
            while inimigo.status == "Vivo":
                print("1 - Lutar\n2 - Fugir.") #Menu de Ataques
                ataques = input("| ?: ")
                print(5*"=")
                #Ataque normal
                if ataques == "1":
                    limparTela()
                    batalha(jogador, inimigo)
                elif ataques == "2":
                    limparTela()
                    combate = False
                    print("Você fugiu do combate.")
                    break
                #Quando o jogador morre.
                if jogador.vida <= 0:
                    print(f"{jogador.name} morreu!\nGAMER OVER")
                    fim_de_jogo = True
                    break
            if inimigo.status == "Morto":
                combate = False
        else:
            print("Nada foi encontrado.")
            sleep(1.5)
            limparTela()
    elif escolha == "2": #Carregamento da tela de inventario
        limparTela()
        loading("\nCarregando inventário...", 0.5)
        limparTela()
        jogador.getInventario()
        limparTela()
    elif escolha == "3":
        limparTela()
        loading("\nSalvando...", 0.5)
        limparTela()
        atualizar_tabela(jogador)#Atualiza todos os dados do jogador no "Bando" de Dados
        loading("\nJogo Salvo.", 1)
        limparTela()
    elif escolha == "4" or fim_de_jogo == True:
        break
    jogador.getLevel()
print("Você saiu do Jogo!")
sleep(2)
