# coding=utf-8
# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ ESCOLA POLITÉCNICA
# RACIOCÍNIO ALGORÍTMICO
# PROF. HENRI FREDERICO EBERSPÄCHER
# Estudante: Ricardo Varjão

#PROBLEMAS 3: Selecao simples
#-------------------------------


    #Elabore um algoritmo que leia um número inteiro e verifique se ele é par ou ímpar.
    print('Par ou impar?')
    a = int(input('digite um numero: '))
    r = a % 2
    if r  == 1 : print ('O número {} é impar'.format(a))
    else : print('O numero {} é par'.format(a))

def alg2():
    import datetime
# A partir do ano de nascimento informado pelo usuário,
# elabore um algoritmo que informe a idade que completará
# (ou já completou) em 2018. Verifique se ele já pode fazer
# a carteira de motorista ou não, informando sua situação.
    print('Carteira de motorista?')
    nascimento = input('Ano de nascimento: ')
    anoAtual = int(datetime.datetime.now().year)
    idade = anoAtual - nascimento
    if idade >= 18 : print('Apto a tirar carteira de motorista')
    else : print('Não está apto a tirar carteira de motorista')

def alg3():
    #Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada
    #(informe 'valor inválido para numeros negativos)

    print('Raiz quadrada')def alg1():

    a = input('Digite um valor')
    if a < 0 : print('Valor inválido!')
    else:
        print('sqrt({}) = {}'.format(a, pow(a, 0.5)))



def alg4():
    #Um produtor de abóboras deve verificar a classificação dos seus produtos para
    # posterior empacotamento e venda. Um de seus clientes compra apenas abóboras médias
    # (aquelas que possuem o diâmetro (d) no intervalo 15 cm ≤ d < 20 cm).
    # Elabore um algoritmo que leia o diâmetro de uma abóbora e mostre se ela é do tipo médio ou não.
    # Caso ela não se encaixe na classificação, informe “produto fora das medidas”.

    print('Aboboras')
    a = input('diametro da abóbora (cm): ')
    if a >= 15 and a < 20: print('abóbora média, ok para ser vendida')
    else: print('produto fora das medidas')


def alg5():
    # em uma determinada papelaria a fotocopia custa R$0.25, caso sejam tiradas menos de 100 copias.
    # A partir de 100 copias, o valor de cada fotocopia tirada cai para R$0.20.
    # Elabore um algoritmo que leia o numero de copias e mostre o valor a pagar pelo servico

    print('Fotocópia')
    copias = abs(input('número de cópias: '))
    valorCopias = 0.25
    if copias > 100:
        valorCopias = 0.20
    print('valor total: R$ {:.2f}'.format(copias * valorCopias))



def alg6():
    # Tendo como dados de entrada a altura (h) e o sexo de uma pessoa (use 1 - Masculino, 2 - Feminino)
    #elabore um algoritmo que calcule o peso ideal (p) do usuario utilizando as seguintes formulas:
    #homens: p = (72.7 * h) - 58
    #mulheres: p = (62.1 * h) - 44.7
    print('Peso ideal')
    sexo = input("Sexo: \n1 - Masculino 2 - Feminino: ")
    h = float(input('altura: '))
    p = 0
    if sexo == 1: p = (72.7 * h) - 58
    elif sexo == 2: p = (62.1 * h) - 44.7
    print('peso ideal: {:.2f}'.format(p))

def alg7():
    #O IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula: IMC = massa / altura^2
    # Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário
    # e mostre o valor do IMC e se ele está na faixa considerada “normal” segundo
    # o critério apresentado na tabela da OMS (Organização Mundial de Saúde):
    # 18,5 ≤ IMC< 25.
    # Caso não esteja, calcule sua massa máxima considerada normal (usando IMC igual a 24,9).

    print('IMC')
    h = input('altura: ')
    m = input('massa: ')
    imc = m / pow(h,2)
    if imc >= 18.5 and imc < 25: print('Valor de IMC ({:.2f}) considerado normal'.format(imc))
    elif imc < 18.5 :
        massaMinima = 18.5 * pow(h,2)
        print('Valor de IMC ({:.2f}) considerado abaixo do normal. Massa mínima deveria ser de {:.2f} kg'.format(imc, massaMinima))
    elif imc > 25 :
        massaMaxima = 25 * pow(h,2)
        print('Valor de IMC ({:.2f}) considerado acima do normal. Massa máxima deveria ser de {:.2f} kg'.format(imc, massaMaxima))


def alg8():
    import math
    # Em um determinado estacionamento a primeira hora custa R$8.00, que e o valor minimo praticado
    # Apos uma hora o valor é fracionado, R$1.50 a cada quinze minutos.
    #Elabore um algoritmo que leia um numero inteiro correspondente a quantidade de minutos usados no estacionamento
    # e mostre e mensagem "Valor minimo R$8.00" ou "Valor fracionado: "R$ x"
    # no qual 'x' será o valor a pagar calculado
    print('Estacionamento')
    valorMinimo = 8.00
    tempo = int(input('Minutos utilizados: '))
    if tempo <= 60 : print('Valor minimo: R$ {:.2f}'.format(valorMinimo))
    else:
        tempoExtra = tempo - 60
        print('tempo extra: {:.2f}'.format(tempoExtra))
        divisoes = math.ceil(1 + tempoExtra / 15) #fracoes de 15 min. Se entrar naquela fracao, ja sera cobrada
        print('divisoes: {:.2f}'.format(divisoes))
        valor = valorMinimo + divisoes * 1.5
        print('Valor fracionado: R${:.2f}'.format(valor))



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
    else : sair = True
