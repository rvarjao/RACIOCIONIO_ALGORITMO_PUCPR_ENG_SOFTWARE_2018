#coding=utf-8
#Problema 02 da lista 10, porem, feitos utilizando sqlite3

import sqlite3
import random
import datetime
import FuncoesComuns as common


def alg2():

#Desenvolva um algoritmo que leia as informações referentes a um conjunto de 50 pessoas.
# Após a leitura e devidos cálculos exibir as respostas pedidas.
# Dados de entrada:
# • Peso;
# • Sexo (1 - Masculino, 2 - Feminino);
# • Idade.
#
# Informações de saída:
# • Quantidade de Pessoas Acima de 90 kg;
# • Quantidade de Mulheres entre 20 e 25 (inclusive) com peso abaixo de 60 kg;
# • Quantidade de Homens com peso acima de 100 kg.
# • Porcentagem de Pessoas com idade abaixo de 16 ou superior a 65 anos.

    global nPessoas
    nPessoas = 50

    perguntas = []
    perguntas.append("Quantidade de Pessoas Acima de 90 kg")
    perguntas.append("Quantidade de Mulheres entre 20 e 25 (inclusive) com peso abaixo de 60 kg")
    perguntas.append("Quantidade de Homens com peso acima de 100 kg")
    perguntas.append("Porcentagem de Pessoas com idade abaixo de 16 ou superior a 65 anos")
    perguntas = common.ajustaPerguntas(perguntas)

    # conectando ao banco de dados
    global conn
    conn = sqlite3.connect ('lista10_problema02.db')

    # definindo um cursor
    global cursor
    cursor = conn.cursor ( )

    #cria o banco de dados
    criaBancoDeDados()

    #insere novos dados no banco se o usuario quiser
    criar = raw_input ("Popular banco de dados? (S/N): ").lower ( )
    if criar == "s":
        populaBancoDeDados ( )

    #comeca a fazer as pesquisas
    #----------------------
    # 01 - Quantidade de Pessoas Acima de 90 kg;
    resultados = []
    queries = []

    queries.append("SELECT COUNT(*) FROM {} WHERE peso > 90".format(tabelaPrincipal))
    cursor.execute(queries[len(queries) - 1])
    resultados.append(cursor.fetchone()[0])
    #----------------------
    # 02 - Quantidade de Mulheres entre 20 e 25 (inclusive) com peso abaixo de 60 kg
    queries.append("SELECT COUNT(*) FROM {} WHERE (sexo = 2) and (idade > 20 and idade <= 25) and (peso < 60)".format(tabelaPrincipal))
    cursor.execute(queries[len(queries) - 1])
    resultados.append(cursor.fetchone()[0])
    #----------------------
    # 03 - Quantidade de Homens com peso acima de 100 kg
    queries.append ("SELECT COUNT(*) FROM {} WHERE (sexo = 1) and (peso > 100)".format(tabelaPrincipal))
    cursor.execute (queries[ len (queries) - 1 ])
    resultados.append (cursor.fetchone ( )[ 0 ])
    # ----------------------
    # 04 - Porcentagem de Pessoas com idade abaixo de 16 ou superior a 65 anos
    queries.append ("SELECT COUNT(*) FROM {} WHERE (idade < 16) or (idade > 65)".format(tabelaPrincipal))
    cursor.execute (queries[ len (queries) - 1 ])
    resultados.append (cursor.fetchone ( )[ 0 ])

    #---------------------------------------
    #apresenta os resultados
    print("-"*100)
    for (i, pergunta) in enumerate(perguntas):
        print("{}: {}".format(pergunta, resultados[i]))
    print("-"*100)
    # ---------------------------------------

    imprimirDados = raw_input("Imprimir todo o banco de dados? (S/N): ").lower()
    if imprimirDados == "s": imprimirTodoBancoDeDados()

    #fecha o banco de dados
    conn.close ( )
    #fim
    #--------------------

def imprimirTodoBancoDeDados():
    queryTotal = "SELECT * FROM {} ORDER BY peso".format(tabelaPrincipal)
    for data in cursor.execute (queryTotal):
        print(data)


def populaBancoDeDados():
    import datetime
    import sqlite3
    import random

    # gera do banco de dados
    anoAtual = datetime.datetime.now().year

    cursor.execute ("DELETE FROM {}".format(tabelaPrincipal))  # apaga todos os dados que possam já existir

    for i in range (0, nPessoas):
        idade = random.randrange(10, 100)
        # • Sexo (1 - Masculino, 2 - Feminino);
        sexo = random.randrange (1, 3)

        peso = random.randrange (1, 200)

        # Insert a row of data
        cursor.execute ("INSERT INTO {} VALUES ({},{},{})".format(tabelaPrincipal, peso, sexo, idade))
    conn.commit ( )



def criaBancoDeDados():
    global tabelaPrincipal
    tabelaPrincipal = "tbEntrevistados"

    camposNomes = ["peso", "sexo", "idade"]
    camposTipos = ["double", "int", "int"]


    # criando a tabela (schema)
    sqlCreateTable = "CREATE TABLE IF NOT EXISTS {}".format(tabelaPrincipal)
    for (i, _) in enumerate(camposNomes):
        if i == 0: sqlCreateTable += "("

        sqlCreateTable += camposNomes[i] + " " + camposTipos[i]

        if i < len(camposNomes) - 1: sqlCreateTable += ","
        else: sqlCreateTable += ")"

    print("sqlCreateTable: {}".format(sqlCreateTable))
    cursor.execute (sqlCreateTable)



alg2()