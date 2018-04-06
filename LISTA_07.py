# coding=utf-8

def alg1():
    #Anacleto tem 1,50 metro e cresce 2 centímetros por ano,
    # enquanto Felisberto tem 1,10 metro e cresce 3 centímetros por ano.
    # Construa um algoritmo que calcule e mostre quantos anos serão necessários
    #  para que Felisberto seja maior que Anacleto.
    # y = ax + b
    # x = (y - b) / a

    #Anacleto
    b1 = 150
    a1 = 2

    #Felisberto
    b2 = 110
    a2 = 3

    x = 0
    y1 = a1 * x + b1
    y2 = a2 * x + b2

    while y2 < y1:
        print("{},{},{}".format(x, y1, y2))
        y1 = a1 * x + b1
        y2 = a2 * x + b2
        x += 1

    print("anos necessários: {}".format(x))

def alg2():
    #Crie um algoritmo que calcule a divisão inteira de dois números fornecidos pelo usuário:
    # a por b, através de subtrações sucessivas.
    # Mostre o resultado do quociente (o div) e do resto (o mod).
    a = int(input("a: "))
    b = int(input("b: "))

    temp = a
    count = 0
    while temp >= 0:
        temp -= b
        count += 1

    temp += b
    count -= 1

    print("-"*10)
    print("{} / {}".format(a, b))
    print("div: {}   mod: {}".format(count, temp))
    print("-"*10)

def alg3():
    #Elabore um algoritmo que leia um conjunto de n números inteiros, sendo n fornecido pelo usuário.
    # Mostre então qual o maior e qual o menor número fornecido.
    n = int(input("n: "))
    maior = 0
    for c in range(0, n, 1):
        current = input("digite um numero: ")
        if c == 0 : maior = current
        elif current > maior : maior = current

        #print("Atual valor maior: {}".format(maior))

    print("Valor maior: {}".format(maior))

def alg4():
    #Elabore um algoritmo que leia um conjunto de 10 números inteiros.
    #Mostre então qual a média dos números impares fornecidos.

    count = float(0)
    soma = float(0)

    for i in range(0, 10, 1):
        current = float(input("digite um numero: "))
        if current % 2 == 1 :
            soma += current
            count += 1

    media = soma / count
    print("media: {}".format(media))

def alg5():
# Escreva um algoritmo que leia um conjunto de números inteiros e que somente termine a
# leitura quando atingir um total de 3 números pares positivos lidos.
# Informe então qual foi o maior número par fornecido.

    nPositivos = 0
    maior = 0

    while True:
        a = int(input("Digite um número: "))
        if a % 2 == 0 :
            if nPositivos == 0 : maior = a

            if a > maior : maior = a

            nPositivos += 1
            if nPositivos == 3 : break

    print("maior: {}".format(maior))


def alg6():
#Elabore um algoritmo que leia um conjunto de números inteiros e somente termine a leitura quando for
# fornecida uma seqüência de três números em ordem crescente.
# Mostre então qual a média deste conjunto de três números.
    n = [float("-inf"), float("-inf"), float("-inf")]
    i = 0

    shouldContinue = True

    while shouldContinue:
        print("----------")

        for i in range(0, 3):

            print("i:{}".format(i))
            n[i] = int(input("digite um número: "))
            print(n)

            if i == 0 : continue

            if n[i] < n[i - 1]:
                print("{} < {}  Nao esta na sequencia, reiniciando".format(n[i], n[i-1]))
                n = [ float ("-inf"), float ("-inf"), float ("-inf") ]
                break

            if (i == 2):
                if (n[0] < n[1] < n[2]) :
                    print("encontrado resultado")
                    shouldContinue = False
                    break
                else: print("Nao esta na sequencia, reiniciando")
        if shouldContinue == False : break


    soma = sum(n)
    media = float(soma) / float(len(n))
    print(n)
    print("media: {}".format(media))


def alg7():
    # A série de Fibonacci é formada pela seguinte seqüência: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55... etc.
    # Escreva um algoritmo que mostre os números da série de Fibonacci menores que 1000.

    a0 = 0
    a1 = 1
    a2 = 1

    while a2 < 1000:
        print(a2)
        a2 = a0 + a1
        a0 = a1
        a1 = a2

def alg8():
    #A série de Fibonacci é formada pela seguinte seqüência: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55... etc.
    # Escreva um algoritmo que mostre o n primeiros números da série de Fibonacci, sendo n fornecido pelo usuário.
    a0 = 0
    a1 = 1
    a2 = 1
    n = int(input("Quantidade de termos: "))
    count = 0
    while count < n:
        print(a2)
        a2 = a0 + a1
        a0 = a1
        a1 = a2
        count += 1

def alg9():
#A série de Ricci difere da série de Fibonacci (1, 1, 2, 3, 5, ...)
# porque os dois primeiros termos podem ser definidos pelo usuário.
#   Imprima os n primeiros termos da série de Ricci,
# sendo que n e o valor dos primeiros termos são fornecidos pelo usuário.

# a0 a1 a2
# 5  8  13  21  34
    a0 = int(input("a0: "))
    a1 = int(input("a1: "))
    a2 = a0 + a1

    n = int (input ("Quantidade de termos: "))
    count = 0

    print(a0)
    print(a1)

    while count < n - 2:
        print(a2)
        a0 = a1
        a1 = a2
        a2 = a0 + a1
        count += 1

def alg10():
# A série de Fetuccine difere da série de Ricci porque o termo de posição par é resultado da
#  subtração dos dois anteriores.
# Os termos ímpares continuam sendo resultado da soma dos dois elementos anteriores.
# Imprima os n primeiros termos da série de Fetuccine,
# sendo que n e o valor dos primeiros termos são fornecidos pelo usuário.

    a0 = int(input("a0: "))
    a1 = int(input("a1: "))
    a2 = a0 + a1

    n = int (input ("Quantidade de termos: "))
    count = 0

    print(a0)
    print(a1)

    while count < n - 2:
        print(a2)
        a0 = a1
        a1 = a2
        if count % 2 == 0: a2 = a1 - a0
        else : a2 = a0 + a1
        count += 1

def alg11():
#Elabore um algoritmo que calcule o valor de S, em que:
# S = 1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 + ... – 10/100
    s = float(1)
    strS = "{:.0f}".format(s)

    for i in range(2, 100):
        sign = float(0)
        if i % 2 == 0 : sign = -1
        else: sign = 1
        current = float(sign * i / (2*i))
        s += current
        strS += " {:.0f}".format(s) + "{:.0f}".format(sign*i) + "/ {:.0f}".format(2*i)

    print("{} = {}".format(strS, s))

def alg12():
    #Elabore um algoritmo que o valor da série S abaixo, sendo que o valor inteiro de n é fornecido pelo usuário.
    #S = 1/3 + 3/6 + 5/9 + ... + (2n - 1) / 3n
    count = int(input("n: "))
    s = float(0)
    strS = ""
    for n in range(1, count):
        s += float(2* n - 1)/float(3*n)
        strS += " + ({}/{})".format(2 * n - 1, 3*n)
#    print("{} = {:.2f}".format(strS, s))
    print("{} termos = {}".format(count, s))


def alg13():
    #O valor de π pode ser calculado usando como base a seguinte série:
    #s = 1 - 1/3^3 + 1/5^3 - 1/7^3 + 1/9^3 + ...
    #sendo π = (s*32)^1/3
    count = 100
    s = float(1)
    sign  = float(-1)
    # strS = "1"
    for n in range(3, count, 2):
        s += sign/pow(float(n), 3)
        # strS += " + ({}/{}^3)".format(sign, n)
        sign *= -1

    pi = (s * 32)**(1./3)
    #print("{} = {:.2f}".format(strS, s))
    print("π = {}".format(pi))

a = 1
nProblemas = 13
while 0 < a <= nProblemas:
    a = input ('Qual algoritmo voce deseja?: ')
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
    elif (a == 13) : alg13()
