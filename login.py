import re;
def mostrarMenu():
    menu ={
        "1": "Login",
        "2": "Validação de senha",
        "3": "Pesquisa de senha",
        "4": "Sair",
    }

    print(f"Bem-vindo ao sistema de login!")
    for key, value in menu.items():
        print(f"{key}: {value}")

    escolha = input("Escolha uma opção: ")
    if escolha not in menu:
        print("Opção inválida. Tente novamente.")
    else:
        return menu[escolha]


def cadastroEmail():
    texto = input("Digite seu email: ")
    return texto

def verificaEmail(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(padrao,email)

def cadastroSenha():
    senha = input("Digite sua senha:(Ela deve conter pelos menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial) ")
    return senha

def verificarSenha(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(padrao, senha):
        return True
    else:
        return False

