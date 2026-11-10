import sqlite3
import hashlib
import re

# Banco de Dados
con = sqlite3.connect("dadodUsuarios.db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS usuarios 
                (email TEXT PRIMARY KEY,
                hash_senha TEXT)''')

con.commit()

# Menu
def mostrarMenu():
    opcoes = {
        "1": "Cadastro Senha",
        "2": "Validação de Senha",
        "3": "Pesquisar Hash da Senha",
        "4": "Sair"
    }

    print("\nSistema de Senhas\n")
    for chave, valor in opcoes.items():
        print(f"{chave}. {valor}")

    escolha = input("Digite o número da opção: ").strip()

    if escolha not in opcoes:
            print("Opção inválida. Tente novamente.")
            return None

    return escolha

# Cadastro email e validação
def cadastroEmail():
    pedirEmail = input("Digite o e-mail a ser cadastrado:").strip().lower()
    return pedirEmail

def verificarEmail(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(padrao, email) is not None

# Cadastro senha e validação
def cadastroSenha():
    print("Sobre a senha: ela deve conter pelos menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial")
    senha = input("Digite sua senha: ").strip()
    return senha

def verificarSenha(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(padrao, senha) is not None

# Opção 1: Cadastro
def cadastrar():
    print("Cadastro de Usuário")
    email = cadastroEmail()
    while not verificarEmail(email):
        print("E-mail inválido. Tente novamente.")
        email = cadastroEmail()

    senha = cadastroSenha()
    while not verificarSenha(senha):
        print("Senha inválida. Tente novamente.")
        senha = cadastroSenha()

    hash_senha = hashlib.sha256(senha.encode()).hexdigest()    

    try:
        cur.execute(
            "INSERT INTO usuarios (email, hash_senha) VALUES (?,?)",
            (email, hash_senha)
        )
        con.commit()
        print("Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("E-mail já cadastrado. Tente novamente.")

 # Opção 2: Validação de Senha

def validar_senha():
    email = input("Digite seu e-mail: ").strip().lower()
    senha = input("Digite sua senha: ").strip()

    hash_senha = hashlib.sha256(senha.encode()).hexdigest()

    cur.execute(
        "SELECT hash_senha FROM usuarios WHERE email = ?",
        (email,)
    )

    resultado = cur.fetchone()

    if resultado is None:
        print("E-mail inexistente")
    else:
        hash_banco = resultado[0]
        if hash_senha == hash_banco:
            print("Senha correta")
        else:
            print("Senha incorreta")  

# Opção 3: Pesquisar Hash da Senha
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

# Opções
def executarOpcao(escolha):
    if escolha == "1":
        cadastrar()
    elif escolha == "2":
        validar_senha()
    elif escolha == "3":
        pesquisar_hash_senha()
    elif escolha == "4":
        print("Saindo...")
        return False 
 
    return True 

def main():
    rodando = True
    while rodando:
        escolha = mostrarMenu()
        if escolha is not None:
            rodando = executarOpcao(escolha)
 
    con.close()
    print("Sistema encerrado.")
 
 
if __name__ == "__main__":
    main()