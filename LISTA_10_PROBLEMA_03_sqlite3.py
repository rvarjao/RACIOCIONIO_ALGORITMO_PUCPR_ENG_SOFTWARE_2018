# coding=utf-8
import sqlite3
import random
import datetime
import FuncoesComuns as common

def alg3():
    # Desenvolva um algoritmo que leia as informações solicitadas a seguir referentes a um conjunto de 20 pessoas.
    # Após a leitura e devidos cálculos exibir as respostas pedidas.
    # Dados de entrada:
    # • Idade;
    # • Sexo (1 - Masculino, 2 - Feminino);
    # • Estado Civil (1 - Solteiro, 2 - Casado, 3 - Divorciado).
    #
    # Informações de saída:
    # • Quantidade de pessoas solteiras ou divorciadas;
    # • Quantidade de homens casados;
    # • Quantidade de homens casados com menos de 25 anos;
    # • Quantidade de pessoas divorciadas com 40 anos ou mais;
    # • Quantidade de mulheres entre 40 e 50 (inclusive) solteiras.

    global nPessoas
    nPessoas = 20

    perguntas = []
    perguntas.append("Quantidade de pessoas solteiras ou divorciadas")
    perguntas.append("Quantidade de homens casados")
    perguntas.append("Quantidade de homens casados com menos de 25 anos")
    perguntas.append("Quantidade de pessoas divorciadas com 40 anos ou mais")
    perguntas.append("Quantidade de mulheres entre 40 e 50 (inclusive) solteiras")
    perguntas = common.ajustaPerguntas(perguntas)


    # conectando ao banco de dados
    global conn
    conn = sqlite3.connect ('lista10_problema03.db')

    # definindo um cursor
    global cursor
    cursor = conn.cursor ( )

    # cria o banco de dados
    criaBancoDeDados ( )


    # insere novos dados no banco se o usuario quiser
    criar = input ("Popular banco de dados? (S/N): ").lower ( )
    if criar == "s":
        populaBancoDeDados ( )


    # comeca a fazer as pesquisas
    # ----------------------
    resultados = []
    queries = []

    # • Idade;
    # • Sexo (1 - Masculino, 2 - Feminino);
    # • Estado Civil (1 - Solteiro, 2 - Casado, 3 - Divorciado).

    # 01 - Quantidade de pessoas solteiras ou divorciadas
    queries.append("SELECT COUNT(*) FROM {} WHERE estadoCivil = 1 or estadoCivil = 3".format(tabelaPrincipal))
    # 02 - Quantidade de homens casados
    queries.append("SELECT COUNT(*) FROM {} WHERE sexo = 1 and estadoCivil = 2".format(tabelaPrincipal))
    # 03 - Quantidade de homens casados com menos de 25 anos
    queries.append ("SELECT COUNT(*) FROM {} WHERE (sexo = 1) and (estadoCivil = 2) and (idade < 25)".format (tabelaPrincipal))
    # 04 - Quantidade de pessoas divorciadas com 40 anos ou mais
    queries.append ("SELECT COUNT(*) FROM {} WHERE (idade >= 40) and (estadoCivil = 3)".format (tabelaPrincipal))
    # 05 - Quantidade de mulheres entre 40 e 50 (inclusive) solteiras
    queries.append ("SELECT COUNT(*) FROM {} WHERE (sexo = 2) and (idade > 40 and idade <= 50) and (estadoCivil = 1)".format (tabelaPrincipal))

    for query in queries:
        cursor.execute(query)
        resultados.append(cursor.fetchone()[0])

    #---------------------------------------
    #apresenta os resultados
    print("-"*100)
    for (i, pergunta) in enumerate(perguntas):
        print("{}: {}".format(pergunta, resultados[i]))
    print("-"*100)
    # ---------------------------------------

    imprimirDados = input("Imprimir todo o banco de dados? (S/N): ").lower()
    if imprimirDados == "s": imprimirTodoBancoDeDados()

    #fecha o banco de dados
    conn.close ( )
    #fim
    #--------------------



def criaBancoDeDados():
    # • Idade;
    # • Sexo (1 - Masculino, 2 - Feminino);
    # • Estado Civil (1 - Solteiro, 2 - Casado, 3 - Divorciado).
    global tabelaPrincipal
    tabelaPrincipal = "tbEntrevistados"

    camposNomes = ["sexo", "idade", "estadoCivil"]
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

    cursor.execute ("DELETE FROM {}".format (tabelaPrincipal))  # apaga todos os dados que possam já existir

    # • Idade;
    # • Sexo (1 - Masculino, 2 - Feminino);
    # • Estado Civil (1 - Solteiro, 2 - Casado, 3 - Divorciado).
    for i in range (0, nPessoas):
        idade = random.randrange (10, 100)
        # • Sexo (1 - Masculino, 2 - Feminino);
        sexo = random.randrange (1, 3)
        estadoCivil = random.randrange(1,4)
        # Insert a row of data
        cursor.execute ("INSERT INTO {} VALUES ({},{},{})".format (tabelaPrincipal, sexo, idade, estadoCivil))
    conn.commit ()


def imprimirTodoBancoDeDados():
    queryTotal = "SELECT * FROM {} ORDER BY idade".format(tabelaPrincipal)
    for data in cursor.execute (queryTotal):
        print(data)





alg3()