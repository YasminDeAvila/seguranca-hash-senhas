# importar o sqlite3 as sql
import sqlite3 as sql

# conectar ao banco de dados
con = sql.connect('banco.db')

# criar um banco de dados
sql_create = 'create table usuarios ' \
'(email varchar (300) primary key,' \
'senha_hash TEXT)' \

# criar um cursor para executar comandos SQL
cur = con.cursor()

# executar o comando SQL para criar a tabela
cur.execute(sql_create)



