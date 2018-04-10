#coding=utf-8
#Problema 01 da lista 10, porem, feitos utilizando sqlite3

import sqlite3
import random
import datetime


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
    nPessoas = 50

    perguntas = []
    perguntas.append ("Quantidade de torcedores com mais de 70 anos")
    perguntas.append ("Quantidade de mulheres torcedoras do Atletico com menos de 25 anos (inclusive)")
    perguntas.append ("Quantidade de homens torcedores do Coritiba ou Parana")
    perguntas.append ("Quantidade de homens torcedores do Coritiba ou Parana com idade entre 20 e 40 (inclusive)")
    perguntas.append ("Porcentagem de entrevistados que nao torcem por nenhum dos times relacionados")
    perguntas = ajustaPerguntas(perguntas)

    # conectando ao banco de dados
    global conn
    conn = sqlite3.connect ('clientes.db')

    # definindo um cursor
    global cursor
    cursor = conn.cursor ( )

    criaBancoDeDados()

    criar = raw_input("Popular banco de dados? (S/N): ").lower()
    if criar == "s":
        populaBancoDeDados()

    #fazer as pesquisas no banco de dados

    #salva os resultados das pesquisas
    resultados = [0,0,0,0,0]
    queries = []

    queryTotal = "SELECT COUNT(*) FROM tbEntrevistados"
    cursor.execute(queryTotal)
    nEntradas = cursor.fetchone()[0]
    print("nEntradas: {}".format(nEntradas))


    # 01 - Quantidade de torcedores com mais de 70 anos;
    nascimento = datetime.datetime.now().year - 70
    queries.append("SELECT COUNT(*) FROM tbEntrevistados WHERE anoNascimento < {}".format(nascimento))
    cursor.execute(queries[0])

    #salva o resultado da pesquisa
    resultados[0] = cursor.fetchone ()[0]
    # print("01:  {}".format(resultados[0]))
    #---

    # • Sexo (1 - Masculino, 2 - Feminino);
    # • Time de preferência (1- Atlético, 2 - Coritiba, 3 – Paraná, 4 – nenhum).

    # 02 - Quantidade de mulheres torcedoras do Atlético com menos de 25 anos (inclusive);
    nascimento = datetime.datetime.now().year - 25
    queries.append("SELECT COUNT(*) FROM tbEntrevistados WHERE anoNascimento <= {} AND sexo = 2".format(nascimento))
    cursor.execute(queries[1])
    resultados[1] = cursor.fetchone()[0]
    # print("02:  {}".format(resultados[1]))

    # 03 - Quantidade de homens torcedores do Coritiba ou Paraná;
    queries.append("SELECT COUNT(*) FROM tbEntrevistados WHERE sexo = 1 AND (time = 1 OR time = 2)")
    cursor.execute(queries[len(queries) - 1])
    resultados[2] = cursor.fetchone()[0]
    # print("03:  {}".format(resultados[2]))


    # 04 - Quantidade de homens torcedores do Coritiba ou Paraná com idade entre 20 e 40 (inclusive);
    nascInicio = datetime.datetime.now().year - 40
    nascFim = datetime.datetime.now().year - 20

    queries.append("SELECT COUNT(*) FROM tbEntrevistados WHERE sexo = 1 AND (time = 1 OR time = 2) AND "
                   "(anoNascimento > {} AND anoNascimento <= {})".format(nascInicio, nascFim))
    cursor.execute(queries[len(queries) - 1])
    resultados[3] = cursor.fetchone()[0]
    # print("04:  {}".format(resultados[3]))

    # 05 - Porcentagem de entrevistados que não torcem por nenhum dos times relacionados.
    queries.append("SELECT COUNT(*) FROM tbEntrevistados WHERE time = 4")
    cursor.execute(queries[len(queries) - 1])
    resultados[4] = 100 * float(cursor.fetchone()[0])/float(nEntradas)

    # print("05:  {}".format(resultados[4]))

    print("-"*100)
    for (i, pergunta) in enumerate(perguntas):
        print("{}: {}".format(pergunta, resultados[i]))

    print("-"*100)

    imprimirDados = raw_input("Imprimir todo o banco de dados? (S/N): ").lower()
    if imprimirDados == "s":
        queryTotal = "SELECT * FROM tbEntrevistados ORDER BY anoNascimento"
        for data in cursor.execute(queryTotal):
            print(data)




    #fecha o banco de dados
    conn.close ( )

def criaBancoDeDados():
    # criando a tabela (schema)
    cursor.execute ("CREATE TABLE IF NOT EXISTS tbEntrevistados (anoNascimento int, sexo int, time int)")


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


# ajusta as perguntas para ficar alinhada à direita
def ajustaPerguntas(perguntas):
    maxSize = 0
    #verifica a pergunta mais comprida
    for pergunta in perguntas:
        size = len(pergunta)
        if maxSize < size : maxSize = size

    #coloca o numero de espacos à esquerda necessarios
    for (i, pergunta) in enumerate(perguntas):
        size = len(pergunta)
        nEspacos = maxSize - size
        strEspacos = " "*nEspacos
        perguntas[i] = strEspacos + pergunta

    return perguntas


alg1()