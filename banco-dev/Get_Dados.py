import sqlite3

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()
sql = "select * from cadastro "
cursor.execute(sql)
dados = cursor.fetchall()
cursor.close()
conector.close()

print('\nConsulta ao Banco de Dados conta.db \n')

print('Dados da tabela ‘cadastro’' )

print('-' * 75)
print('{:<10} {:10} {:11} {:<30} {:<5}'.format('Código', 'Nome', 'CPF', 'END', 'Saldo'))
print('-' * 75)

for d in dados:
    print('{:<10} {:10} {:11} {:<30} {:<5}'.format(d[0], d[1], d[2], d[3], d[4]))

print('-' * 75)
print(' Encontrados {} registros'.format(len(dados)))
print('\n\nFim do programa')
