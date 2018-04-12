# coding=utf-8
def alg1():
    import random
    import datetime
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

    dados = []
    nPessoas = 50

    #gera do banco de dados
    anoAtual = datetime.datetime.now ( ).year

    for i in range(0, nPessoas):

        # • Ano de Nascimento;
        ano = random.randrange(anoAtual - 100, anoAtual - 5)

        # • Sexo (1 - Masculino, 2 - Feminino);
        sexo = random.randrange(1, 3)

        # • Time de preferência (1- Atlético, 2 - Coritiba, 3 – Paraná, 4 – nenhum).
        time = random.randrange(1, 5)

        dado = {"ano" : ano, "sexo" : sexo, "time" : time}
        dados.append(dado)



    perguntas = []
    perguntas.append("01 - Quantidade de torcedores com mais de 70 anos")
    perguntas.append("02 - Quantidade de mulheres torcedoras do Atlético com menos de 25 anos (inclusive)")
    perguntas.append("03 - Quantidade de homens torcedores do Coritiba ou Parana")
    perguntas.append("04 - Quantidade de homens torcedores do Coritiba ou Paraná com idade entre 20 e 40 (inclusive)")
    perguntas.append("05 - Porcentagem de entrevistados que não torcem por nenhum dos times relacionados")
    perguntas = ajustaPerguntas(perguntas)

    resultados = []

    for (i, _) in enumerate(perguntas):
        resultados.append(0)

    for dado in dados:
        ano = dado["ano"]
        sexo = dado["sexo"]
        time = dado["time"]
        idade = anoAtual - ano

        #PESQUISA 01
        if idade > 70 : resultados[0] += 1

        #PESQUISA 02
        if sexo == 2 and idade <= 25: resultados[1] += 1

        #PESQUISA 03
        if sexo == 1 and (time == 2 or time == 3):
            resultados[2] += 1

            #PESQUISA 04
            if 20 < idade <= 40: resultados[3] += 1

        #PESQUISA 05
        if time == 4 : resultados[4] += 1

        resultados[4] = 100 * float(resultados[4]) / float(len(dados))

    #RESULTADOS
    for (i, pergunta) in enumerate(perguntas):
        print("{}: {:.1f}".format(pergunta, resultados[i]))
    print("-"*50)

    imprimirDados = raw_input("Imprimir todo o banco de dados? (S/N) ").lower()
    if imprimirDados == "s":
        for dado in dados:
            print(dado)



#-------------------------------------------

def alg2():
    import random
    import datetime
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
    dados = [ ]

    # gera do banco de dados
    anoAtual = datetime.datetime.now ( ).year
    dados = []
    for i in range (0, 50):
        peso = random.randrange(30, 200)
        sexo = random.randrange(1, 3)
        idade = random.randrange(10, 100)
        dado = {"peso" : peso, "sexo": sexo, "idade" : idade}
        dados.append(dado)


    resultados = [0,0,0,0]
    #fazer as buscas
    # 01 - Quantidade de Pessoas Acima de 90 kg;
    # 02 - Quantidade de Mulheres entre 20 e 25 (inclusive) com peso abaixo de 60 kg;
    # 03 - Quantidade de Homens com peso acima de 100 kg.
    # 04 - Porcentagem de Pessoas com idade abaixo de 16 ou superior a 65 anos.

    for dado in dados:
        peso = dado["peso"]
        idade = dado["idade"]
        sexo = dado["sexo"]


        #PESQUISA 01
        if idade > 90 : resultados[0] += 1

        #PESQUISA 02
        if sexo == 2:
            if (20 < idade <= 25) and (peso < 60): resultados[1] += 1
        # PESQUISA 03
        else:
            if peso > 100: resultados[2] += 1

        # PESQUISA 04
        if (idade < 16) or (idade > 65) : resultados[3] += 1


    porcentagem4 = 100 * float(resultados[3]) / float(len(dados))

    print("-"*50)
    print("                                     Quantidade de Pessoas Acima de 90 kg: {}".format(resultados[0]))
    print("Quantidade de Mulheres entre 20 e 25 (inclusive) com peso abaixo de 60 kg: {}".format(resultados[1]))
    print("                            Quantidade de Homens com peso acima de 100 kg: {}".format(resultados[2]))
    print("      Porcentagem de Pessoas com idade abaixo de 16 ou superior a 65 anos: {:.1f} %".format(resultados[3]))

    print("-"*50)

    imprimirDados = raw_input("Imprimir todo o banco de dados? (S/N) ").lower()
    if imprimirDados == "s":
        for dado in dados:
            print(dado)


#-------------------------------------------
def alg3():
    import datetime
    import random

#Desenvolva um algoritmo que leia as informações solicitadas a seguir referentes a um conjunto de 20 pessoas.
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

    dados = [ ]
    nPessoas = 20

    # gera do banco de dados
    anoAtual = datetime.datetime.now().year

    for i in range (0, nPessoas):
        idade = random.randrange(16, 100)
        sexo = random.randrange(1,3)
        estadoCivil = random.randrange(1,4)

        dado = {"idade" : idade, "sexo" : sexo, "estadoCivil" : estadoCivil}
        dados.append(dado)


    # • Sexo (1 - Masculino, 2 - Feminino);
    # • Estado Civil (1 - Solteiro, 2 - Casado, 3 - Divorciado).

    resultados = [0,0,0,0,0]

    #fazer as buscas
    for dado in dados:
        idade = dado["idade"]
        sexo = dado["sexo"]
        estadoCivil = dado["estadoCivil"]

        # 01 - Quantidade de pessoas solteiras ou divorciadas;
        if estadoCivil == 1 or estadoCivil == 3: resultados[0] += 1

        # 02 - Quantidade de homens casados;
        if sexo == 1 and estadoCivil == 2:
            resultados[1] += 1
            # 03 - Quantidade de homens casados com menos de 25 anos;
            if idade < 25:
                resultados[2] += 1

        # 04 - Quantidade de pessoas divorciadas com 40 anos ou mais;
        if estadoCivil == 3 and idade >= 40: resultados[3] += 1

        # 05 - Quantidade de mulheres entre 40 e 50 (inclusive) solteiras.
        if sexo == 2 and (40 < idade <= 50) and (estadoCivil == 1):
            resultados[4] += 1

    #Apresentacao dos resultados
    print("-"*50)
    print("            Quantidade de pessoas solteiras ou divorciadas: {}".format(resultados[0]))
    print("                              Quantidade de homens casados: {}".format(resultados[1]))
    print("         Quantidade de homens casados com menos de 25 anos: {}".format(resultados[2]))
    print("     Quantidade de pessoas divorciadas com 40 anos ou mais: {}".format(resultados[3]))
    print("Quantidade de mulheres entre 40 e 50 (inclusive) solteiras: {}".format(resultados[4]))

    print("-"*50)

    imprimirDados = raw_input("Imprimir todo o banco de dados? (S/N) ").lower()
    if imprimirDados == "s":
        for dado in dados:
            print(dado)


def alg4():
    import datetime
    import random
    import operator  #usado para fazer buscar no dicionario

#Desenvolva um algoritmo que leia as informações solicitadas a seguir referentes a um conjunto de 30 pessoas. 
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
    
    nPessoas = 30
    dados = [ ]


    # gera do banco de dados
    anoAtual = datetime.datetime.now ( ).year

    for i in range (0, nPessoas):
        idade = random.randrange (6, 100)
        praticaEsportes = random.randrange(1,4)
        saude = random.randrange(1,5)

        dado = {"idade": idade, "praticaEsportes" : praticaEsportes, "saude" : saude}
        dados.append (dado)

    # • Quantas pessoas com menos de 20 anos nunca praticam esportes;
    #   dict = dict.Where(r=>r.Value > 0);


    resultados = []
    for i in range(0, 6): resultados.append(0)

    # analise dos dados
    # • Pratica esportes: 1 - sempre, 2 – raramente, 3 - nunca;
    # • Como qualifica sua saúde: 1 – ótima, 2 – boa, 3 – regular, 4 – ruim.

    #esse vai ser feito um loop para cada pesquisa
    # 01 - Quantas pessoas com menos de 20 anos nunca praticam esportes;
    for dado in dados:
        idade = dado["idade"]
        praticaEsportes = dado["praticaEsportes"]
        saude = dado["saude"]

        if (idade < 20) and (praticaEsportes == 3) :
            resultados[0] += 1
    #--------------------------------------


    # 02 - Qual a média das idades das pessoas que sempre praticam esporte;
    soma02 = 0.
    count02 = 0.
    for dado in dados:
        idade = dado["idade"]
        praticaEsportes = dado["praticaEsportes"]
        saude = dado["saude"]

        if (praticaEsportes == 1):
            soma02 += idade
            count02 += 1
    resultados[1] = soma02 / count02



    # 03 - Qual média das idades das pessoas que tem saúde regular ou ruim e que praticam esportes raramente ou nunca;
    soma03 = 0.
    count03 = 0.
    for dado in dados:
        idade = dado["idade"]
        praticaEsportes = dado["praticaEsportes"]
        saude = dado["saude"]

        if ((saude == 3) or (saude == 4)) and ((praticaEsportes == 2) or (praticaEsportes == 3)):
            soma03 += idade
            count03 += 1
    resultados[2] = soma03 / count03


    # 04 - Qual a idade da pessoa mais idosa que tem saúde ótima;
    # Primeiramente, ordena-se o dicionario baseado na idade
    #fonte: https://wiki.python.org/moin/SortingListsOfDictionaries
    campoASortear = "idade"
    decorated = [ (dict_[ campoASortear ], dict_) for dict_ in dados ]
    decorated.sort (reverse=True) #do mais velho ao mais novo
    dadosOrdenados = [ dict_ for (key, dict_) in decorated ]

    for dado in dadosOrdenados:
        #verifica se a pessoa tem saúde otima, essa já será a mais velha
        idade = dado["idade"]
        saude = dado["saude"]
        if saude == 1:
            resultados[3] = idade
            break

    # 05 - Qual a idade da pessoa mais idosa que tem saúde ótima e que pratica esportes raramente;
    for dado in dadosOrdenados:
        # verifica se a pessoa tem saúde otima, essa já será a mais velha e que pratica esportes raramente;
        idade = dado[ "idade" ]
        praticaEsportes = dado[ "praticaEsportes" ]
        saude = dado[ "saude" ]
        if saude == 1 and praticaEsportes == 2:
            resultados[4] = idade
            break

    # 06 - Qual a idade da pessoa mais nova que tem saúde ruim.
    for dado in reversed(dadosOrdenados): #vai de tras para frente, pegando o mais novo primeiro
        idade = dado[ "idade" ]
        saude = dado[ "saude" ]
        if saude == 4:
            resultados[5] = idade
            break


    perguntas = []
    perguntas.append("Quantas pessoas com menos de 20 anos nunca praticam esportes")
    perguntas.append("Qual a media das idades das pessoas que sempre praticam esporte")
    perguntas.append("Qual media das idades das pessoas que tem saude regular ou ruim e que praticam esportes raramente ou nunca")
    perguntas.append("Qual a idade da pessoa mais idosa que tem saude otima")
    perguntas.append("Qual a idade da pessoa mais idosa que tem saude otima e que pratica esportes raramente")
    perguntas.append("Qual a idade da pessoa mais nova que tem saude ruim")

    #ajusta as perguntas para ficar alinhada à direita
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



    for (i, pergunta) in enumerate(perguntas):
        print("{}: {:.2f}".format(pergunta, resultados[i]))




    imprimirDados = raw_input("Imprimir todo o banco de dados? (S/N) ").lower()
    if imprimirDados == "s":
        for dado in dados:
            print(dado)


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

a = 1
nProblemas = 4
while 0 < a <= nProblemas:
    print("-"*40)
    a = int(input ('Qual algoritmo voce deseja?: '))
    if (a == 1) : alg1()
    elif (a == 2) : alg2()
    elif (a == 3) : alg3()
    elif (a == 4) : alg4()
