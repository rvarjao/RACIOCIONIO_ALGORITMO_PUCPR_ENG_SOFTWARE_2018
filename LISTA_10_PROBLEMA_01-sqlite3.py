#coding=utf-8
#Problema 01 da lista 10, porem, feitos utilizando sqlite3

import sqlite3
import random
import datetime
import numbers
import FuncoesComuns as common



def alg1():

#Desenvolva um algoritmo que leia as informações referentes a um conjunto de 50 pessoas.
# Após a leitura e devidos cálculos exibir as respostas pedidas.
# Dados de entrada:
# • Ano de Nascimento;
# • Sexo (1 - Masculino, 2 - Feminino);
# • Time de preferência (1- Atlético, 2 - Coritiba, 3 – Paraná, 4 – nenhum).
#
# Informações de saída:
# • Quantidade de torcedores com mais de 70 anos;
# • Quantidade de mulheres torcedoras do Atlético com menos de 25 anos (inclusive);
# • Quantidade de homens torcedores do Coritiba ou Paraná;
# • Quantidade de homens torcedores do Coritiba ou Paraná com idade entre 20 e 40 (inclusive);
# • Porcentagem de entrevistados que não torcem por nenhum dos times relacionados.

    global nPessoas
    nPessoas = 51

    perguntas = []
    perguntas.append("Quantidade de torcedores com mais de 70 anos")
    perguntas.append("Quantidade de mulheres torcedoras do Atletico com menos de 25 anos (inclusive)")
    perguntas.append("Quantidade de homens torcedores do Coritiba ou Parana")
    perguntas.append("Quantidade de homens torcedores do Coritiba ou Parana com idade entre 20 e 40 (inclusive)")
    perguntas.append("Porcentagem de entrevistados que nao torcem por nenhum dos times relacionados (%)")
    # perguntas =  common.ajustaPerguntas(perguntas)

    for pergunta in perguntas:
        pergunta = pergunta.ljust(20, "x")

    # conectando ao banco de dados
    global conn
    conn = sqlite3.connect ('clientes.db')

    # definindo um cursor
    global cursor
    cursor = conn.cursor ( )

    criaBancoDeDados()

    criar = input("Popular banco de dados? (S/N): ").lower()
    if criar == "s":
        populaBancoDeDados()

    #salva os resultados das pesquisas
    resultados = []
    queries = []

    # 01 - Quantidade de torcedores com mais de 70 anos;
    nascimento = datetime.datetime.now().year - 70
    queries.append("SELECT COUNT(*) FROM tbEntrevistados WHERE anoNascimento < {}".format(nascimento))

    # 02 - Quantidade de mulheres torcedoras do Atlético com menos de 25 anos (inclusive);
    nascimento = datetime.datetime.now ( ).year - 25
    queries.append ("SELECT COUNT(*) FROM tbEntrevistados WHERE anoNascimento <= {} AND sexo = 2".format (nascimento))

    # 03 - Quantidade de homens torcedores do Coritiba ou Paraná;
    queries.append ("SELECT COUNT(*) FROM tbEntrevistados WHERE sexo = 1 AND (time = 1 OR time = 2)")

    # 04 - Quantidade de homens torcedores do Coritiba ou Paraná com idade entre 20 e 40 (inclusive);
    nascInicio = datetime.datetime.now ( ).year - 40
    nascFim = datetime.datetime.now ( ).year - 20

    queries.append ("SELECT COUNT(*) FROM tbEntrevistados WHERE sexo = 1 AND (time = 1 OR time = 2) AND "
                    "(anoNascimento > {} AND anoNascimento <= {})".format (nascInicio, nascFim))

    # 05 - Porcentagem de entrevistados que não torcem por nenhum dos times relacionados.
    query = "SELECT 100*CAST(COUNT(time) AS DOUBLE)/ CAST((SELECT COUNT(time) FROM tbEntrevistados) AS DOUBLE) FROM tbEntrevistados WHERE (time = 4)"
    queries.append(query)

    #salva os resultados da pesquisa
    for query in queries:
        cursor.execute(query)
        resultado = cursor.fetchone()[0]
        resultados.append(resultado)

    print("-"*100)
    for (i, pergunta) in enumerate(perguntas):
        resultado = resultados[i]
        if float(resultado).is_integer(): print("{}: {}".format(pergunta, resultados[i]))
        else: print("{}: {:.2f}".format(pergunta, resultados[i]))

    print("-"*100)

    imprimirDados = input("Imprimir todo o banco de dados? (S/N): ").lower()
    if imprimirDados == "s":
        queryTotal = "SELECT * FROM tbEntrevistados ORDER BY anoNascimento"
        for data in cursor.execute(queryTotal):
            print(data)




    #fecha o banco de dados
    conn.close ( )

def criaBancoDeDados():
    # criando a tabela (schema)
    global tabelaPrincipal
    tabelaPrincipal = "tbEntrevistados"

    camposNomes = ["anoNascimento", "sexo", "time"]
    camposTipos = ["int", "int", "int"]

    # criando a tabela (schema)
    sqlCreateTable = "CREATE TABLE IF NOT EXISTS {} ".format(tabelaPrincipal)
    for (i, _) in enumerate(camposNomes):
        if i == 0: sqlCreateTable += "("

        sqlCreateTable += camposNomes[i] + " " + camposTipos[i]

        if i < len(camposNomes) - 1: sqlCreateTable += ","
        else: sqlCreateTable += ")"

    print("sqlCreateTable: {}".format(sqlCreateTable))
    cursor.execute (sqlCreateTable)


def populaBancoDeDados():
    # gera do banco de dados
    anoAtual = datetime.datetime.now ( ).year

    cursor.execute ("DELETE FROM tbEntrevistados")  # apaga todos os dados que possam já existir

    for i in range (0, nPessoas):
        # • Ano de Nascimento;
        ano = random.randrange (anoAtual - 100, anoAtual - 5)
        # • Sexo (1 - Masculino, 2 - Feminino);
        sexo = random.randrange (1, 3)
        # • Time de preferência (1- Atlético, 2 - Coritiba, 3 – Paraná, 4 – nenhum).
        time = random.randrange (1, 5)
        # Insert a row of data
        cursor.execute ("INSERT INTO tbEntrevistados VALUES ({},{},{})".format (ano, sexo, time))
    conn.commit ( )


alg1()