# coding=utf-8
import sqlite3
import random
import datetime


def alg4():
# Desenvolva um algoritmo que leia as informações solicitadas a seguir referentes a um conjunto de 30 pessoas.
# Após a leitura e devidos cálculos exibir as respostas pedidas.

# Dados de entrada:
# • Idade;
# • Pratica esportes: 1 - sempre, 2 – raramente, 3 - nunca;
# • Como qualifica sua saúde: 1 – ótima, 2 – boa, 3 – regular, 4 – ruim.

# Informações de saída:
# • Quantas pessoas com menos de 20 anos nunca praticam esportes;
# • Qual a média das idades das pessoas que sempre praticam esporte;
# • Qual média das idades das pessoas que tem saúde regular ou ruim e que praticam esportes raramente ou
# nunca;
# • Qual a idade da pessoa mais idosa que tem saúde ótima;
# • Qual a idade da pessoa mais idosa que tem saúde ótima e que pratica esportes raramente;
# • Qual a idade da pessoa mais nova que tem saúde ruim.
    global nPessoas
    nPessoas = 30

    perguntas = []
    perguntas.append("Quantas pessoas com menos de 20 anos nunca praticam esportes")
    perguntas.append("Qual a media das idades das pessoas que sempre praticam esporte")
    perguntas.append("Qual media das idades das pessoas que tem saude regular ou ruim e que praticam esportes raramente ou nunca")
    perguntas.append("Qual a idade da pessoa mais idosa que tem saude otima")
    perguntas.append("Qual a idade da pessoa mais idosa que tem saude otima e que pratica esportes raramente")
    perguntas.append("Qual a idade da pessoa mais nova que tem saude ruim")
    perguntas = ajustaPerguntas(perguntas)


    # conectando ao banco de dados
    global conn
    conn = sqlite3.connect ('lista10_problema04.db')

    # definindo um cursor
    global cursor
    cursor = conn.cursor ( )

    # cria o banco de dados
    criaBancoDeDados ( )

    # insere novos dados no banco se o usuario quiser
    criar = raw_input ("Popular banco de dados? (S/N): ").lower ( )
    if criar == "s":
        populaBancoDeDados ( )


    # comeca a fazer as pesquisas
    # ----------------------
    resultados = []
    queries = []

    # • Pratica esportes: 1 - sempre, 2 – raramente, 3 - nunca;
    # • Como qualifica sua saúde: 1 – ótima, 2 – boa, 3 – regular, 4 – ruim.
    # 01 - Quantas pessoas com menos de 20 anos nunca praticam esportes
    queries.append("SELECT COUNT(*) FROM {} WHERE (idade < 20) and (praticaEsportes = 3)".format(tabelaPrincipal))
    cursor.execute(queries[len(queries) - 1])
    resultados.append(cursor.fetchone()[0])
    #----------------------
    # 02 - Qual a média das idades das pessoas que sempre praticam esporte
    queries.append("SELECT AVG(idade) FROM {} WHERE (praticaEsportes = 1)".format(tabelaPrincipal))
    cursor.execute(queries[len(queries) - 1])
    resultados.append(cursor.fetchone()[0])
    #----------------------
    # 03 - Qual media das idades das pessoas que tem saude regular ou ruim e que praticam esportes raramente ou nunca
    queries.append ("SELECT AVG(idade) FROM {} WHERE (saude = 3 or saude = 4) and (praticaEsportes = 2 or praticaEsportes = 3)".format (tabelaPrincipal))
    cursor.execute (queries[ len (queries) - 1 ])
    resultados.append (cursor.fetchone ( )[ 0 ])
    # ----------------------
    # 04 - Qual a idade da pessoa mais idosa que tem saude otima
    queries.append ("SELECT MAX(idade) FROM {} WHERE (saude = 1)".format (tabelaPrincipal))
    cursor.execute (queries[ len (queries) - 1 ])
    resultados.append (cursor.fetchone ( )[ 0 ])
    # ----------------------
    # 05 - Qual a idade da pessoa mais idosa que tem saude otima e que pratica esportes raramente
    queries.append ("SELECT MAX(idade) FROM {} WHERE (saude = 1) and (praticaEsportes = 2)".format (tabelaPrincipal))
    cursor.execute (queries[ len (queries) - 1 ])
    resultados.append (cursor.fetchone ( )[ 0 ])
    # ----------------------
    # 06 - Qual a idade da pessoa mais nova que tem saude ruim
    queries.append ("SELECT MIN(idade) FROM {} WHERE (saude = 4)".format (tabelaPrincipal))
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




def criaBancoDeDados():
    # • Idade;
    # • Pratica esportes: 1 - sempre, 2 – raramente, 3 - nunca;
    # • Como qualifica sua saúde: 1 – ótima, 2 – boa, 3 – regular, 4 – ruim.

    global tabelaPrincipal
    tabelaPrincipal = "tbEntrevistados"

    camposNomes = ["idade", "praticaEsportes", "saude"]
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
    # • Pratica esportes: 1 - sempre, 2 – raramente, 3 - nunca;
    # • Como qualifica sua saúde: 1 – ótima, 2 – boa, 3 – regular, 4 – ruim.
    for i in range (0, nPessoas):
        idade = random.randrange (10, 100)
        praticaEsportes = random.randrange (1, 4)
        saude = random.randrange(1,5)

        # Insert a row of data
        cursor.execute ("INSERT INTO {} VALUES ({},{},{})".format (tabelaPrincipal, idade, praticaEsportes, saude))
    conn.commit()


def imprimirTodoBancoDeDados():
    queryTotal = "SELECT * FROM {} ORDER BY idade".format(tabelaPrincipal)
    for data in cursor.execute (queryTotal):
        print(data)


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


alg4()