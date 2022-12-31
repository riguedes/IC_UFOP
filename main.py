import MySQLdb

# Conecte-se ao banco de dados
db = MySQLdb.connect(host="localhost", user="root", passwd="littlemix38500588", db="ufop")

# Crie um cursor para executar consultas
cursor = db.cursor()

# Execute uma consulta
cursor.execute("SELECT count(*) FROM information_schema.columns  WHERE table_name='Bolsistas_ic' AND table_schema='ufop'")

# Obtenha os resultados da consulta
resultado = cursor.fetchone()

# O número de colunas está armazenado na primeira posição do resultado
num_colunas = resultado[0]

print("Número de colunas:", num_colunas)

# Feche a conexão com o banco de dados
db.close()