# Criando conexão ao banco Sqlite

import sqlite3

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()
sql = """
    CREATE TABLE IF NOT EXISTS cadastro (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    CPF VARCHAR(11) NOT NULL,
    END VARCHAR(30) NOT NULL,
    balance FLOAT(2));
    """
cursor.execute(sql)
print("tabela criada com sucesso!")



conector.commit()
cursor.close()
conector.close()