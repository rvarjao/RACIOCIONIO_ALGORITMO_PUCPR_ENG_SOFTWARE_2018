# coding=utf-8
def alg1():
#Escreva um algoritmo que imprima todas as possibilidades de que no lançamento de dois dados
# tenhamos o valor 7 como resultado da soma dos valores de cada dado.
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 7:
                count += 1
                print("{}: dado 1: {}  dado 2: {}".format(count, i, j))

def alg2():
#Um número na forma n3 é igual a soma de n ímpares consecutivos.
# Exemplo: 13= 1, 23= 3+5, 33= 7+9+11, 43= 13+15+17+19 etc.
# Dado um limite superior li fornecido pelo usuário, mostre os ímpares consecutivos cuja soma é igual a
#  n3 para n variando de 1 a li.

#comentario do problema:
# n	n^3
# 1	1	    1				        -inicio                             foi necessario 1 impar
# 2	8	    3	5			        - o 3 é sequencia do 1 anterior     foram necessarios 2 impares
# 3	27	    7	9	11		        - o 7 é sequencia do 5 anterior     foram necessarios 3 impares
# 4	64	    13	15	17	19	        - o 13 é sequencia do 11 anterior   foram necessarios 4 impares
# 5	125	    21	23	25	27	29      - o 21 é sequencia do 19 anterior   foram necessarios 5 impares
#...
#n n^3                              -                                   serao necessarios n impares
#e assim por diante
#outra coisa, a diferenca entre n^3 e n é sempre igual a (n-1)^2
#entao, para determinar o primeiro impar da sequencia, deve-se fazer:
# p = (n-1)^2 + n
#exemplo, para n = 5:  p = (5 - 1)ˆ2 + 5 = (4)^2 + 5 = 16 + 5 = 21.
#entao, como sao 5 impares necessario, 5^3 = 21 + 23 + 25 + 27 + 29

    li = int(input("Digite o limite superior: ")) #deve-se pedir do usuario
    for n in range(1, li + 1):

        pImpar = (n - 1)**2 + n #primeiro impar da sequencia
        uImpar = pImpar + (n-1) * 2 #ultimo impar da sequencia é uma PA com a1 = pImpar p = 2, e pegando o elemento (n-1)

        impares = []

        for i in range(pImpar, uImpar + 1, 2):
            impares.append(i)

        print("{}^3 = {} = {}".format(n, impares, sum(impares)))
        impares = []



def alg3():
    #Elabore um algoritmo que imprima:
#1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
    text = ""
    for x in range(1, 10):
        text += "{} ".format(x)
    text += "\n"
    print(text*10)

def alg4():
    #Elabore um algoritmo que imprima:
    # 1
    # 12
    # 123
    # 1234
    # 12345
    # 123456
    # 1234567
    # 12345678
    # 123456789
    for i in range(1, 11):
        text = ""
        for j in range(1, i):
            text += "{}".format(j)
        # text += "\n"
        print(text)

def alg5():
    #Elabore um algoritmo que imprima:
    # 123456789
    # 12345678
    # 1234567
    # 123456
    # 12345
    # 1234
    # 123
    # 12
    # 1
    for i in range(10, 0, -1):
        text = ""
        for j in range(1, i):
            text += "{}".format(j)
        # text += "\n"
        print(text)

def alg6():
#     Elabore um algoritmo que imprima:
# 0 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 0
# 2 3 4 5 6 7 8 9 0 1
# 3 4 5 6 7 8 9 0 1 2
# 4 5 6 7 8 9 0 1 2 3
# 5 6 7 8 9 0 1 2 3 4
# 6 7 8 9 0 1 2 3 4 5
# 7 8 9 0 1 2 3 4 5 6
# 8 9 0 1 2 3 4 5 6 7
# 9 0 1 2 3 4 5 6 7 8
    n = []
    for i in range(0, 10):
        n.append(i)

    text = ""
    for i in range(0, 10):
        for v in n:
            text += "{} ".format(v)
        print(text)
        text = ""
        first = n[0]     #guarda o primeiro
        n.pop(0)         #tira
        n.append(first)  #coloca no final

def alg7():
#     Elabore um algoritmo que imprima:
# x23456
# 2x3456
# 33x456
# 444x56
# 5555x6
# 66666x
    for i in range(1, 7):
        text = ""
        for j in range(1, 7):
            v = ""
            if j == i : v = "x"
            elif j < i : v = "{}".format(i)
            else: v = "{}".format(j)
            text += v
        print(text)

def alg8():
    #Elabore um algoritmo que imprima:
# 1     6
#  2   5
#   3 4
#   3 4
#  2   5
# 1     6
    for i in range(1, 7):
        text = ""
        for j in range(1, 7):
            v = " "
            if (j == i) or (j + i == 7) : v = "{} ".format(j)
            text += v
        print(text)


def alg9():
    for i in range(1, 8):
        verificacao = i % 2
        text = ""
        for j in range(1, 8):
            v = "- "
            if j % 2 == verificacao: v = "{} ".format(j)
            text += v
        print(text)

def alg10():
    text = ""
    for i in range(1, 11):
        text = ""                       #zera o texto

        for j in range(1, i):           #comeca um novo triangulo
            text += "\n"
            for k in range(1, j + 1):
                text += "{}".format(k)  #preenche uma linha
        print(text)


a = 1

nProblemas = 10
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
