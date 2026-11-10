import sqlite3
con= sqlite3.connect('dadosUsuario.db')
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