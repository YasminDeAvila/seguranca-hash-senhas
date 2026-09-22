import sqlite3
import hashlib
import re

con= sqlite3.connect('dadosUsuario.db')

def mostrarMenu():
    menu ={
        "1": "Cadastro",
        "2": "Login",
        "3": "Validação de senha",
        "4": "Pesquisa de senha",
        "5": "Sair",
    }

    print(f"Bem-vindo ao sistema de login!")
    for key, value in menu.items():
        print(f"{key}: {value}")

    escolha = input("Digite o número da opção: ").strip()
    if escolha not in menu:
        print("Opção inválida. Tente novamente.")
    else:
        return menu[escolha]

def cadastroEmail():
    texto = input("Digite o e-mail a ser cadastrado: ").strip().lower()
    return texto

def verificaEmail(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if re.match(padrao,email):
        return True
    else: 
        return False


def cadastroSenha():
    print("Sobre a senha: ela deve conter pelos menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial")
    senha = input("Digite sua senha: ").strip()
    return senha

def verificarSenha(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(padrao, senha):
        return True
    else:
        return False

# Buscar Hash

cur = con.cursor()
# ---------------------------

def pesquisar_hash_senha():
    email = input("Digite o e-mail: ").strip().lower()

    cur.execute(
    "SELECT hash_senha FROM usuarios WHERE email = ?",
    (email,)
    )

    resultado = cur.fetchone()

    if resultado is None:
        print("E-mail inexistente")
    else:
        print("Hash:" + resultado[0])

# Validar Senha

def validar_senha():

    cursor = con.cursor()

    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    hash_senha = hashlib.sha256(
        senha.encode()
    ).hexdigest()

    cursor.execute(
        "SELECT hash_senha FROM usuarios WHERE email = ?",
        (email,)
    )

    resultado = cursor.fetchone()

    if resultado is None:

        print("E-mail inexistente")

    else:

        hash_banco = resultado[0]

        if hash_senha == hash_banco:

            print("Senha correta")

        else:

            print("Senha incorreta")


# Banco de Dados

cur.execute('''CREATE TABLE IF NOT EXISTS usuarios
               (email TEXT PRIMARY KEY,
                hash_senha TEXT)''')

# sql_create = 'create table usuarios ' \
# '(email varchar (300) primary key,' \
# 'senha_hash TEXT)' \
# cur = con.cursor()
# cur.execute(sql_create)
# sql_insert = 'insert into usuarios values(?,?)'
# cur.execute(sql_insert)
# sql_select = 'select * from usuarios'

# Menu
def menu(escolha):
    if escolha in ("1", "login"):
        print("Opção de login escolhida!")

        email = cadastroEmail()
        verificaEmail(email)

        while not verificaEmail(email):
            email = cadastroEmail()
            
        senha = cadastroSenha()
        senha = verificarSenha(senha)
        while not verificarSenha(senha):
            print("Senha inválida. Tente novamente.")
            senha = verificarSenha()

        hash_senha = hashlib.sha256(senha.encode()).hexdigest()

        # sql_insert = 'insert into usuarios values(?,?)',(email, hash_senha)
        cur.execute("INSERT INTO usuarios (email, hash_senha) VALUES (?, ?)", (email, hash_senha))
        con.commit()

    elif escolha in ("2", "validação de senha"):
        validar_senha()


def main():
    rodando = True
    while rodando:
        escolha = mostrarMenu()
        if escolha is not None:
            rodando = menu(escolha)
    con.close()
    print("Sistema encerrado.")

if __name__ == "__main__":
    main()        