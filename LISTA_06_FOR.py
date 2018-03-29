# coding=utf-8
#PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ ESCOLA POLITÉCNICA
#RACIOCÍNIO ALGORÍTMICO
#PROF. HENRI FREDERICO EBERSPÄCHER
#estudante: Ricardo Varjão

#Problemas usando Repetição


def alg1():
# [1] Imprima os números de 1 até 99, com incremento de 2. Exemplo: 1, 3, 5.....97, 99
    for a in range(1, 99):
        print(a)

def alg2():
    #[2] Imprima os números de 50 até 0 com decremento de 5. Exemplo: 50, 45, 40.....5, 0
    for a in range(50, 0, -5):
        print(a)

def alg3():
    #[3] Imprima os números de -100 até 100, com incremento de 10. Exemplo: -100, -90, -80.....90, 100
    for a in range(-100, 100, 10):
        print(a)

def alg4():
    #[4] Imprima os números múltiplos de 4 existentes no intervalo aberto ]1, 100[
    for a in range(4, 100, 4):
        print(a)

def alg5():
    #[5] Imprima os números ímpares de 1 até n, sendo n fornecido pelo usuário. Intervalo fechado [1, n]
    n = input("Digite um numero (a > 0) : ")

    for a in range(1, n, 2):
        print(a)

def alg6():
    #[6] Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de 1 a 20 polegadas.
    # A conversão entre estas duas unidades é dada por: polegada = centímetro × 2,54
    for pol in range(1, 20, 1):
        cm = pol / 2.54
        print("{} pol = {:.2f} cm".format(pol, cm))


def alg7():
    #Faça um algoritmo que mostre o resultado da função de Babbage f(x) = x2 + x + 41
    # (polinômio que gera apenas números primos), variando x de 0 até 20.
    for x in range(0, 20):
        f = pow(x,2) + x + 41
        print("f({}) = {}".format(x, f))

def alg8():
    #Considerando que 1 milha vale exatamente 1.609,344 metros,
#  imprima uma tabela de conversão de metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10 kilômetros.
    for km in range(20, 160, 10):
        mi = km * 1609.344
        print("{:.3f} km = {:.3f} mi".format(km, mi))

def alg9():
    #Elabore um algoritmo que leia um conjunto de 10 números inteiros.
# Mostre então qual o valor da soma e da média aritmética do conjunto.
    soma = 0
    for n in range(1, 10):
        a = input ("Digite um numero: ")
        soma += a
        n += 1
    print("Soma:  {}".format (soma))
    print("Media: {}".format (float (soma) / 10))


def alg10():
    #[10] Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final).
# Os valores inteiros de li e lf devem ser informados pelo usuário e não pertencem ao intervalo, ou seja, intervalo aberto: ]li, lf[
    li = input("Limite inicial:")
    lf = input("Limite final:")
    li += 1

    for n in range(1, 3):
        if li % 3 != 0 : li += 1
        else : break

    for a in range(li, lf, 3):
        print("{}".format(a))
        a += 3


def alg11():
    #Imprima uma PA na qual são fornecidos o primeiro termo (a1), a razão (r) e a quantidade de termos (n) desejada.
    # Lembrete:an =a1 +(n-1).r
    a1 = input("a1: ")
    r = input("r: ")
    n = input("n: ")
    an = a1
    for cn in range(1, n):
        an += r
        print(an)

def alg12():
    #Considerando que a conversão de graus Celsius (° C) para graus Farenheit (°F)
    # é dada pela seguinte fórmula: °F = °C × 1,8 + 32
    #Elabore um algoritmo que leia uma temperatura (T) em graus Celsius e mostre as conversões da
    # temperatura dada para graus Farenheit em uma escala que vai de T-10 até T+10

    celsius = input("Temperatura em Celsius: ")
    infCelsius = celsius - 10
    supCelsius = celsius + 10

    for cCelsius in range(infCelsius, supCelsius):
        fahrenheit = cCelsius * 1.8 + 32
        print("{} ˚C = {} ˚F".format(cCelsius, fahrenheit))
        cCelsius += 1



def alg13():
    #[13] O n-ésimo número harmônico é dado pelo seguinte somatório:
#Hn = sum(1/k) (k = 1 -> k <= n)
#Escreva um algoritmo para calcular o valor do número harmônico H dado que o número n será fornecido pelo usuário.
# Exemplo, se o usuário digitar 5, calcular H = 1 + 1/2 + 1/3 + 1/4 + 1/5
#(Para maiores informações sobre o número harmônico http://en.wikipedia.org/wiki/Harmonic_number)
    n = input("Digite o harmonico: ")
    hn = 0
    a = 1
    for a in range(1, n):
        hn += 1/float(a)
    print("Hn: {:.3f}".format(hn))

def alg14():
    #[14] Elabore um algoritmo que calcule o valor da série S abaixo,
    # sendo que o valor inteiro de n é fornecido pelo usuário.
    #s = 1/sqrt(3) + 2/sqrt(4) + 3/sqrt(5) + ... + n/sqrt(n+2)
    n = input("digite o numero de termos (n > = 1) : ")
    sum = 0
    formula = ""

    for a in range(1, n):
        sum = a / (a + 2)**0.5
        formula += "{}/sqrt({})".format(a, a + 2)
        if a != n:
            formula += " + "

    print("s = {}".format(formula))
    print("soma: {}".format(sum))


a = 0
while 0 <= a <= 14:
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
    elif (a == 14) : alg14()
