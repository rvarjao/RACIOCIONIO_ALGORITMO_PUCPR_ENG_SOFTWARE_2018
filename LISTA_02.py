# coding=utf-8
# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ ESCOLA POLITÉCNICA
# RACIOCÍNIO ALGORÍTMICO
# PROF. HENRI FREDERICO EBERSPÄCHER
# Estudante: Ricardo Varjão

#Problemas Sequenciais II
#-------------------------------

def alg1():
    #Considerando que a conversao de grau Celsius para grau Fahrenheit e dada pela seguinte formula:
    # F = (9/5)*C + 32
    # Elabore um algoritmo que leia uma temperatura em Celsius e mostre seu valor em Fahrenheit
    c = float(input('Temperatura em Celsius: '))
    f = float((9/5)*c + 32)
    print('{0} oC = {1} oF'.format(c,f))

def alg2():
    #Elabore um algoritmo para calcular o consumo medio de um automovel (medido em km/l)
    #solicitando como dados de entrada a distancia total percorrida (em km)
    #e o volume de combustivel consumido para percorre-la (em litros)
    dist = input('distancia percorrida (km): ')
    vol = input('consumo de combustivel (L): ')
    print('consumo medio (km/l): {0}'.format(dist/vol))

def alg3():
    #Escreva um algoritmo para calcular o volume de uma esfera de raio r,
    #sendo r um valor fornecido pelo usuario
    r = float(input('raio da esfera: '))
    pi = 3.14159265359
    v = (4/3) * pi * pow(r,3)
    print('volume: {}'.format(v))


def alg4():
    # O IMC, indice de massa corporal, e calculado atraves da seguinte forma:
    # IMC = massa / altura^2
    # Elabore um algoritmo que leia a massa (em kg) e a altura (em m) do usuario e mostre o seu IMC
    print('Calculo de IMC')
    m = float(input('massa (kg): '))
    h = float(input('altura (m): '))
    imc = m / pow(h, 2)
    print('O seu IMC e : {}'.format(imc))

def alg5():
    import math
    # elabore um algoritmo que leia um numero inteiro e considerando que este possui tres casas decimais,
    # mostre o valor da centena, da dezena e da unidade
    print('Partes do numero')
    n = float(input('digite um numero entre 100 e 999'))
    if n < 100 or n > 999 : print('valor errado')
    else:
        c = math.floor(n / 100) * 100
        d = math.floor((n - c)/10) * 10
        u = n - c - d
        print('centena: {}'.format(c))
        print('dezena:  {}'.format(d))
        print('unidade: {}'.format(u))


def alg6():
    # no sistema de medidas imperiais (adotado no Reino Unido), um pe (medida de comprimento) corresponde a doze
    # polegadas, e tres pes sao uma jarda. Considerando que uma polegada corresponde a
    # 2.54 cm, elabore um algoritmo que leia o valor de uma medida em comprimento (em m), e mostre o valor
    # equivalente em pes, polegadas e jardas
    print('Conversao de unidade de medida de comprimento')
    l = input('comprimento em metros: ')
    pol = l / (2.54*pow(10,-2))
    pes = pol / 12
    jardas = pes / 3
    print('{} m e equivalente a:'.format(l))
    print('polegadas: {}'.format(pol))
    print('pes: {}'.format(pes))
    print('jardas: {}'.format(jardas))

def alg7():
    # construa um algoritmo que calcule o valor de uma conta de energia eletrica de uma cidade hipotetica considerando:
    # leitura do mes anterior (em kWh) e leitura do mes atual (em kWh). O valor do kWh e de R$0.38 e a taxa de ICMS
    # de 27 %
    print('Conta de luz')
    consumoAnterior = float(input('consumo anterior (kWh): '))
    consumoAtual = float (input ('consumo atual (kWh): '))
    valorAnterior = (0.38 * consumoAnterior) * (1 + 0.27)
    valorAtual = (0.38 * consumoAtual) * (1 + 0.27)
    print('Valor pago no mes anterior: {}'.format(valorAnterior))
    print('Valor paga no mes atual:    {}'.format(valorAtual))

def alg8():
    # Os fabricantes de discos rigidos usam potências de dez (definidas no Sistema Internacional)
# para expressar a capacidade dos discos. Assim quando é anunciado um disco rígido com 500 GB
#  (ou 500 Gbytes, em grafia correta), o disco tem aproximadamente 500 bilhões de bytes (500 x 10^9);
# que correspondem, entretanto, a aproximadamente 465,6 GiB (465,6 gibibytes = 465 x 2^30).
# Para maiores informações sobre esta ambiguidade ler o artigo da Wikipédia sobre “Prefixo binario”.
# Elabore um algoritmo que leia a capacidade de um disco rígido (em notação comercial) e mostre quantos gibibytes
# de fato ele tem.

    capComercial = float(input('capacidade do disco (Gbytes): '))
    k2e30 = float(1073741824) #2 elevado a trinta
    capReal = capComercial * 1000000000 / k2e30
    print('Capacidade comercial de {} GBytes = {} GiBytes'.format(capComercial, capReal))


def alg9():
    import math
    #um caixa automatico possui as seguintes cedulas disponiveis: 50, 20, 10, 5, 2 e 1. Faca um algoritmo
#que leia o valor de um saque e mostre a quantidade de bilhetes de cada nota necessarios para compor o valor
# solicitado pelo usuario
    notas = [50, 20, 10, 5, 2 , 1]
    valor = input('quanto deseja sacar? ')
    #comeca do maior para o menor
    n = len(notas)
    print('notas:{}'.format(n))
    valorAtual = valor
    for nota in notas:
        if valorAtual >= nota:
            #verifica quantas precisas dessa nota
            nNota = math.floor(valorAtual / nota)
            valorAtual -= nNota * nota  #desconta do valor atual
            print('{} notas de R${}'.format(nNota, nota))

def alg10():
    #Elabore um algoritmo que leia três valores inteiros a, b e c. Em seguida,
# encontre e mostre o maior dos três valores usando a fórmula: maiorAB = (a + b + abs (a - b) ) / 2
# Sendo o abs o valor absoluto.
    a = input('a : ')
    b = input('b : ')
    c = input('c : ')
    d = maior(a, b)
    e = maior(d, c)
    print('o maior numero e o : {}'.format(e))

def maior(a,b):
    return (a + b + abs(a - b))/2

sair = False
while (sair == False):
    print('------')
    a = input ('Qual algoritmo voce deseja: ')
    print('------')
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
    else : sair = True
