import sqlite3
import hashlib


def validar_senha():

    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

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

    conexao.close()