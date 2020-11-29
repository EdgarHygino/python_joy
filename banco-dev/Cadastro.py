import sqlite3


def insertCadastroTable (name, CPF, END, balance):
    try:
        conector = sqlite3.connect('conta.db')
        cursor = conector.cursor()

        sql = """ INSERT INTO cadastro 
        (name, CPF, END, balance) 
        VALUES (?, ?, ?, ?);"""

        dados_cadastro = (name, CPF, END, balance)
        cursor.execute(sql, dados_cadastro)
        conector.commit()

        cursor.close()

    except sqlite3.Error as error:
        print('Erro ao inserir dados', error)
    finally:
        if (conector):
            conector.close()
            print('Conexão com Sqlite fechada')

name = input('Qual nome do Cliente ')
CPF = input('Qual o CPF ')
END = input('Qual o endereço ')
saldo = float(input('Qual o saldo para abertura do cliente '))
insertCadastroTable(name, CPF, END, saldo)



