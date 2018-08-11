# Importações
from Classes.Jogador.Jogador import Jogador
from Classes.Jogador.Jogador import Espadachim
from Classes.Jogador.Jogador import Mago
from Classes.Jogador.Jogador import Arqueiro
from Classes.Jogador.Jogador import Tanker
from Classes.Batalha.Batalha import batalha
# Importações de monstros
from Classes.Inimigos.Inimigos import Rato
from Classes.Inimigos.Inimigos import Urso

#  Bibliotecas padrão
from random import randint
from time import sleep
import os
import platform
import sqlite3
import json

# Variáveis SQL
conexão = sqlite3.connect('personages.db') # Conecta no Banco de dados
cursor = conexão.cursor() # comando cursor
# Váriaveis
jogador = Jogador()
fim_de_jogo = False
# Funções úteis
# Limpa a tela
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

def criar_tabela():# Cria uma tabela
    cursor.execute("CREATE TABLE IF NOT EXISTS personagens (nome text, level integer, inventario text, exp integer, exp_max integer, vida integer, vida_max integer, mana integer, mana_max integer, ataque integer, defesa integer, status text, classe text)")

# Insere o novo char no banco de dados
def inserir_na_tabela(jogador):
    jogador.inventario = json.dumps(jogador.inventario)
    cursor.execute("""
        INSERT INTO personagens (nome, level, inventario, exp, exp_max, vida, vida_max, mana, mana_max, ataque, defesa, status, classe)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (jogador.nome, jogador.level, jogador.inventario, jogador.exp, jogador.exp_max, jogador.vida, jogador.vida_max, jogador.mana, jogador.mana_max, jogador.ataque, jogador.defesa, jogador.status, jogador.classe))
    conexão.commit()
    #jogador.inventario = json.loads(jogador.inventario)

# Atualiza o jogador na tabela quando o jogador escolher Salvar no menu.
def atualizar_tabela(jogador):
    jogador.inventario = json.dumps(jogador.inventario)
    cursor.execute("""
        UPDATE personagens
        SET level = ?, inventario = ?, exp = ?, exp_max = ?, vida = ?, vida_max = ?, mana = ?, mana_max = ?, ataque = ?, defesa = ?, status = ?
        WHERE nome = ?
        """, (jogador.level, jogador.inventario, jogador.exp, jogador.exp_max, jogador.vida, jogador.vida_max, jogador.mana, jogador.mana_max, jogador.ataque, jogador.defesa, jogador.status, jogador.nome))
    conexão.commit()
# Tela inicial.
criar_tabela()
print("+----------------------------------+")
print("|             RPG-PY               |")
print("^----------------//----------------^")
print("+----------------------------------+")
print("|         Pressione Enter          |")
print("^----------------//----------------^")
input("")
limparTela()
# Menu Inicial
while True:
    print("+----------------------------------+")
    print("|               Menu               |")
    print("V----------------------------------V")
    print("| 1 - Criar personagem             |")
    print("| 2 - Selecionar personagem        |")
    print("| 3 - Sair                         |")
    print("^----------------//----------------^")
    escolhaMenu = input("| ?: ")
    limparTela()
    # Criação de Personagem
    if escolhaMenu == "1":
        print("+----------------------------------+")
        print("|       Criação de Personagem      |")
        print("V----------------------------------V")
        nome = input('Nome: ')
        print("Classes: \n1 - Espadachim\n2 - Mago\n3 - Arqueiro\n4 - Tanker")
        escolhaClasse = input('| ?:')
        if escolhaClasse == '1':
            jogador = Espadachim()
            jogador.nome = nome
            inserir_na_tabela(jogador)
            print("Personagem criado com sucesso.")
        elif escolhaClasse == '2':
            jogador = Mago()
            jogador.nome = nome
            inserir_na_tabela(jogador)
            print("Personagem criado com sucesso.")
        elif escolhaClasse == '3':
            jogador = Arqueiro()
            jogador.nome = nome
            inserir_na_tabela(jogador)
            print("Personagem criado com sucesso.")
        elif escolhaClasse == '4':
            jogador = Tanker()
            jogador.nome = nome
            inserir_na_tabela(jogador)
            print("Personagem criado com sucesso.")
        limparTela()
    # Escolhe o personagem "Ainda n ta pronto, apenas mostra todos os personagens salvos no banco"
    elif escolhaMenu == "2":
        cursor.execute("""
        SELECT nome, level FROM personagens;
        """)
        fetch = cursor.fetchall()
        linhas = len(fetch)
        if linhas > 0:
            seletor = {}
            c = 0
            for linha in fetch:
                c += 1
                seletor[c] = linha
            while True:
                print("+----------------------------------+")
                print("|     Seleção de personagens       |")
                print("V----------------------------------V")
                for key in seletor:
                    print(f"| {key} - {seletor[key][0]} ({seletor[key][1]})" + " "*(27-len(str(seletor[key][0]))-len(str(key))-len(str(seletor[key][1]))) + "|")
                if c < 5:
                    j = c+1
                    while j <= 5:
                        print(f"| {str(j)} - [Vazio]                      |")
                        j += 1
                    j = 0
                print("| 6 - Menu                         |")
                print("^----------------//----------------^")
                escolha = input("| ?: ")
                limparTela()
                if escolha.isnumeric():
                    if int(escolha) > 0 and int(escolha) <= c:
                        personagem_nome = seletor[int(escolha)][0]
                        cursor.execute(f"""
                        SELECT * FROM personagens WHERE nome = '{personagem_nome}';
                        """)
                        fetch = cursor.fetchall()
                        for item in fetch:
                            jogador.nome = item[0]
                            jogador.level = item[1]
                            jogador.inventario = item[2]
                            jogador.exp = item[3]
                            jogador.exp_max = item[4]
                            jogador.vida = item[5]
                            jogador.vida_max = item[6]
                            jogador.mana = item[7]
                            jogador.mana_max = item[8]
                            jogador.ataque = item[9]
                            jogador.defesa = item[10]
                            jogador.status = item[11]
                            jogador.classe = item[12]
                        jogador.inventario = json.loads(jogador.inventario)
                        explorar = ""
                        inimigo = ""
                        combate = False
                        while True:
                            jogador.getStatus()
                            print("+----------------------------------+")
                            print("|              Ações               |")
                            print("V----------------------------------V")
                            print("| 1 - Explorar                     |")
                            print("| 2 - Inventário                   |")
                            print("| 3 - Salvar                       |")
                            print("| 4 - Seleção de personagem        |")
                            print("^----------------//----------------^")
                            escolha = input("| ?: ")
                            limparTela()
                            if escolha == "1": # Carregamento de tela da Exploração
                                jogador.getStatus()
                                loading("Explorando...", 0.5)
                                explorar = randint(1, 5) # gera um número aleátorio, se for 1,2,3 = fight com rato
                                if explorar <= 3: # Declara que o inimigo é um Rato
                                    inimigo = Rato()
                                    combate = True
                                elif explorar == 4: # Declara que o inimigo é um Urso
                                    inimigo = Urso()
                                    combate = True
                                if combate == True: # Tela de Combate
                                    limparTela()
                                    jogador.getStatus()
                                    inimigo.getStatus()
                                    print(f"Entrou em combate com um {inimigo.nome}!")
                                    print(30*"-")
                                    while inimigo.status == "Vivo":
                                        print("1 - Lutar\n2 - Fugir.") # Menu de Ataques
                                        ataques = input("| ?: ")
                                        print(5*"=")
                                        # Ataque normal
                                        if ataques == "1":
                                            limparTela()
                                            batalha(jogador, inimigo)
                                        elif ataques == "2":
                                            limparTela()
                                            combate = False
                                            print("Você fugiu do combate.")
                                            break
                                        # Quando o jogador morre.
                                        if jogador.vida <= 0:
                                            print(f"{jogador.nome} morreu!\nGAMER OVER")
                                            fim_de_jogo = True
                                            break
                                    if inimigo.status == "Morto":
                                        """if drop_item == 2:
                                            if 'Poção de Vida' in jogador.inventario.keys():
                                                jogador.inventario['Poção de Vida'] += 1
                                            else:
                                                jogador.inventario['Poção de Vida'] = 1
                                        elif drop_item == 3:
                                            if 'Poção de Mana' in jogador.inventario.keys():
                                                jogador.inventario['Poção de Mana'] += 1
                                            else:
                                                jogador.inventario['Poção de Mana'] = 1"""
                                        combate = False
                                else:
                                    print("Nada foi encontrado.")
                                    sleep(1.5)
                                    limparTela()
                            elif escolha == "2": # Carregamento da tela de inventario
                                limparTela()
                                loading("\nCarregando inventário...", 0.5)
                                limparTela()
                                jogador.getInventario()
                                limparTela()
                            elif escolha == "3":
                                limparTela()
                                loading("\nSalvando...", 0.5)
                                limparTela()
                                atualizar_tabela(jogador)# Atualiza todos os dados do jogador no "Bando" de Dados
                                loading("\nJogo Salvo.", 1)
                                limparTela()
                                jogador.inventario = json.loads(jogador.inventario)
                            elif escolha == "4" or fim_de_jogo == True:
                                break
                            jogador.getLevel()
                    elif int(escolha) == 6:
                        break
                    else:
                        print("V----------------------------------V")
                        print("|          Opção inválida          |")
                        print("^----------------//----------------^")
                else:
                    print("V----------------------------------V")
                    print("|          Opção inválida          |")
                    print("^----------------//----------------^")
        else:
            print("Nenhum jogador encontrado!")
    elif escolhaMenu == "3":
        break
    else:
        print("V----------------------------------V")
        print("|          Opção inválida          |")
        print("^----------------//----------------^")

print("Você saiu do Jogo!")
sleep(2)
