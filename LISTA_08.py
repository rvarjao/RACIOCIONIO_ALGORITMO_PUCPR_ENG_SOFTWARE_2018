# coding=utf-8

def alg1():
    #Escreva um algoritmo que leia um conjunto de números até que o usuário forneça o valor 0 (zero).
# Para cada número par, some-o com a soma dos anteriores, para cada número impar,
# subtraia-o da soma dos anteriores (exemplo: para a entrada: 2 + 4 - 3 + 2 -1 0, o resultado é 4).
#  Mostre então o resultado desta soma, a quantidade total de números fornecidos assim como a porcentagem de números
#  ímpares e de números pares.

    impares = []
    pares = []

    n = float("-inf")
    while n != 0:
        n = int(input("Digite um número: "))
        if n % 2 == 0 : pares.append(n)
        else: impares.append(n)


    nPares = len(pares)
    nImpares = len(impares)
    nTotal = float(nPares + nImpares)

    sumPares = sum(pares)
    sumImpares = sum(impares)
    resultado = sumPares - sumImpares

    print(nPares, nImpares, nTotal)

    print("-"*30)
    print("Resultado")
    print("Quantidade de números fornecidos: {}".format(nTotal))
    print("Pares:  {}  {:.2f} % do total".format(nPares, float(nPares/nTotal)*100))
    print("Impares:{}  {:.2f} % do total".format(nImpares, float(nImpares/nTotal)*100))
    print("\n({}) - ({}) = {}".format(sumPares, sumImpares, resultado))

    print("-"*30)


def alg2():
    #Escreva um algoritmo que leia um conjunto de números inteiros e que somente termine a
    # leitura quando atingir um total de 5 números lidos válidos.
    # Serão considerados inválidos os números múltiplos de 3. Informe então qual é a média do conjunto.
    numeros = []
    while True:
        n = int(input("Digite um numero: "))
        if n % 3 == 0:
            numeros.append(n)
            if len(numeros) == 5 : break

    print("media: {:.2f}".format(media(numeros)))

def alg3():
#Elabore um algoritmo que leia um conjunto de números inteiros e somente termine a leitura quando for
# fornecida uma sequência de dois números iguais.
# Mostre então qual a média do conjunto desconsiderando os últimos dois números (os finalizadores).
    numeros = []
    while True:
        n = input("Digite um numero: ")
        numeros.append(n)
        count = len(numeros)

        print("count: ", count)

        if count > 3 : #maior que tres para sobrar pelo menos um numero apos remover do array
            if n == numeros[count - 2] : break

    print("numeros antes: {}".format(numeros))
    for i in range(0, 2):
        numeros.pop()
    print("numeros depois: {}".format(numeros))

    print("Media: {:.2f}".format(media(numeros)))



def alg4():
#Escreva um algoritmo que leia um conjunto de números inteiros e que somente termine a leitura quando for
#fornecido como finalizador o mesmo valor fornecido no início da sequência.
#Informe então qual é a soma do conjunto, excluindo o primeiro e o último.
    numeros = []
    while True:
        n = int(input("Digite um numero: "))
        numeros.append(n)
        count = len(numeros)
        if count > 3 : #maior que tres para sobrar pelo menos um numero apos remover do array
            if numeros[count - 1] == numeros[0] : break

    numeros.pop(0)
    numeros.pop()

    print("Soma: {}".format(sum(numeros)))

def alg5():
    # Escreva um algoritmo que leia um conjunto de números inteiros e que somente termine a leitura quando
    # for fornecido um valor 0 (zero) imediatamente após um número impar.
    # Informe então qual foi o menor número impar fornecido.
    numeros = []
    i = 0
    while True:
        n = int(input("Digite um numero: "))
        numeros.append(n)
        count = len(numeros)
        if count > 2 : #maior que dois para ter com o que comparar
            if n == 0 and numeros[count - 2] % 3 == 0: break

    #verificar qual o menor impar
    menor = float("inf")
    for n in numeros:
        if n % 2 == 1 :
            if menor > n : menor = n

    print("Menor numero impar: {}".format(menor))


def verificaIntervalo(valor, intervalos):  # verifica em que intervalo esta o numero e retorna o index
    for (i, intervalo) in enumerate (intervalos):
        # print("{}  {}  {}".format(valor, i, intervalo))
        if valor <= intervalo:
            return i

def alg6():
    import random
#Elabore um algoritmo que sorteie 100 números entre 1 e 100.
# Ao final mostre quantos estão dentro dos seguintes intervalos:
# 1 ≤ d ≤ 25; 25 < d ≤ 50; 50 < d ≤ 75; 75 < d ≤ 100.

    intervalos = [25, 50, 75, 100]
    countIntervalos = [0, 0, 0, 0]

    for i in range(0, 100):
        valor = random.randrange(1,101) #tem que ser 101 para incluir o 100 no intervalo
        print(valor)
        index = verificaIntervalo(valor, intervalos)
        countIntervalos[index] = countIntervalos[index] + 1

    print("-"*40)
    print("Resultado")
    print("intervalos: {}".format(intervalos))
    print("contagem:   {}".format(countIntervalos))
    print("-"*40)



def media(numArray):
    return float (sum (numArray)) / float (len (numArray))



def alg7():
#Em uma determinada competição esportiva cada participante recebe as notas de seis juízes.
# A melhor e a pior nota são eliminadas, sendo a nota do participante a média das outras quatro notas.
# Elabore um algoritmo que leia as seis notas de um atleta e depois informe qual foi seu resultado final.

    notas = []

    for i in range(0, 6):
        nota = int(input("Digite a nota: "))
        notas.append(nota)

    menor = float("inf")
    maior = float("-inf")
    for nota in notas:
        if menor > nota : menor = nota
        if maior < nota : maior = nota

    print("\n")
    print("-"*50)
    print("        notas: {}".format(notas))
    notas.remove(maior)
    notas.remove(menor)

    print("notas válidas: {}".format (notas))
    print("        media: {}\n".format(media(notas)))

def alg8():
    #Escreva um algoritmo que mostre as tabuadas de multiplicar dos números 1 até 10
    #o resultado sera apresentado em forma de matriz, onde cada cruzamento sera a multiplicacao realizada
    #entre a primeira linha e a primeira coluna
    #     1 2 3 4 5 6 7 8 9 10
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10
    print("\n")
    strLinhas = "       "
    for i in range(1,11):
        strLinhas += "{:03d}   ".format(i)

    strLinhas += "\n"
    strLinhas += "-"*(len(strLinhas)-4)
    strLinhas += "\n"


    for y in range(1, 11):
        strLinhas += "{:03d} |  ".format(y)
        for x in range(1,11):
            strLinhas += "{:03d}   ".format (x*y)

        strLinhas += "\n"

    strLinhas += "-" * 64
    strLinhas += "\n"

    print(strLinhas)

def alg9():
#Crie um algoritmo que leia 10 números inteiros. Quando o número fornecido for positivo,
# mostre uma contagem regressiva até 0; quando ele for negativo, uma contagem normal até 0;
# quando for nulo mostre “não atendido pelo programa”.
    for i in range(0, 10):
        n = input("Digite um número: ")
        if n < 0 : s = 1
        elif n > 0: s = -1
        else:
            print("Não atendido pelo programa")
            continue
        for c in range(n, 0 + s, s):
            print(c)

def alg10():
    #Elabore um algoritmo que simule um relógio regressivo de 10 minutos, ou seja, que mostre 10:00, 9:59, 9:58 até 0:0.

    print("10 : 00")
    for minutos in range(9, -1, -1):
        for segundos in range(59, 0, -1):
            print("{:02d} : {:02d}".format(minutos, segundos))
        print("{:02d} : 00".format (minutos))

def alg11():
#Um número natural é um número primo quando ele tem exatamente dois divisores: o número um e ele mesmo.
# Em outras palavras, é um número maior que um que não é divisível por nenhum outro número
# maior que um e menor que ele mesmo.
# Exemplos: 2, 3, 5, 7, 11, 13, 17, 19 etc.
# Elabore um algoritmo que mostre os números primos existentes no intervalo de 1 a 500.
#Mais informações sobre número primos em: http://pt.wikipedia.org/wiki/Números_primos
    print("1\n2")
    for i in range(3, 500, 2): #sabe-se que o unico primo par é o 2, entao nao ha pq verificar os pares
        for j in range(3, i + 1, 2):
            if i % j == 0 and i != j: #nao e primo
                break
            if j == i : print(i)

def alg12():
#Um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos
# (excluindo ele mesmo) é igual ao próprio número;
# por exemplo, 6 = 1+2+3 e 28= 1+2+4+7+14.
# Escreva um algoritmo que mostre os números perfeitos existentes no intervalo de 1 a 10000.
#Mais informações sobre número perfeitos em: http://pt.wikipedia.org/wiki/Números_perfeitos

    print("-"*30)
    for i in range(1, 10000):
        divs = divisores(i)
        if sum(divs) == i : print("Numero perfeito encontrado: {}".format(i))

def divisores(n): #retorna os divisores de um numero
    toReturn = []
    for i in range(1, n):
        if n % i == 0 : toReturn.append(i)
    return toReturn

a = 1
nProblemas = 12
while 0 < a <= nProblemas:
    print("-"*40)
    a = int(input ('Qual algoritmo voce deseja?: '))
    if (a == 1) : alg1()
    elif (a == 2) : alg2()
    elif (a == 3) : alg3()
    elif (a == 4) : alg4()
    elif (a == 5) : alg5()
    elif (a == 6) : alg6()
    elif (a == 7) : alg7()
    elif (a == 8) : alg8()
    elif (a == 9) : alg9()
    elif (a == 10) : alg10()
    elif (a == 11) : alg11()
    elif (a == 12) : alg12()
