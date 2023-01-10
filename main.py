import MySQLdb
import matplotlib.pyplot as plt

# Conecte-se ao banco de dados
db = MySQLdb.connect(host="localhost", user="root", passwd="littlemix38500588", db="ufop")

# Crie um cursor para executar consultas
cursor = db.cursor()

# Execute uma consulta para obter o número de linhas na tabela
cursor.execute("SELECT count(*) FROM Bolsistas_ic")

# Obtenha o resultado da consulta
resultado_linha = cursor.fetchone()

# O número de linhas está armazenado na primeira posição do resultado
num_linhas = resultado_linha[0]

# Execute uma consulta para obter o número de colunas na tabela
cursor.execute("SELECT count(*) FROM information_schema.columns WHERE table_name='Bolsistas_ic' AND table_schema='ufop'")

# Obtenha o resultado da consulta
resultado_coluna = cursor.fetchone()

# O número de colunas está armazenado na primeira posição do resultado
num_colunas = resultado_coluna[0]

print("Número de linhas:", num_linhas)
print("Número de colunas:", num_colunas)

# Selecione os dados do banco de dados e armazene-os em duas listas: 'categorias' e 'valores'
categorias = []
valores = []
for linha in 'Tipo_bolsa':
    categoria = linha
    valor = linha
    categorias.append(categoria)
    valores.append(valor)

# Crie o gráfico de barras
plt.bar(categorias, valores)

# Adicione um título e rótulos de eixo
plt.title('Quantidade de alunos por tipo')
plt.xlabel('tipo de aluno')
plt.ylabel('qntd. de alunos')

# Exiba o gráfico
plt.show()

# Feche a conexão com o banco de dados
db.close()
