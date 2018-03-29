# coding=utf-8
# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ ESCOLA POLITÉCNICA
# RACIOCÍNIO ALGORÍTMICO
# PROF. HENRI FREDERICO EBERSPÄCHER
# Estudante: Ricardo Varjão

#PROBLEMAS 4: Selecao Composta

def alg1():
#A partir da idade informada de uma pessoa, elabore um algoritmo que informe a sua classe eleitoral,
# sabendo que menores de 16 não votam (não votante),
#  que o voto é obrigatório para adultos entre 18 e 65 anos (eleitor obrigatório)
# e que o voto é opcional para eleitores entre 16 e 18,
# ou maiores de 65 anos (eleitor facultativo).
    print('Eleicoes')
    a = input('idade: ')
    if a < 16 : print('Pessoa nao esta apta a votar')
    elif a >= 18 and a <= 65 : print('Voto obrigatório')
    else: print('Voto facultativo')


def alg2():
# O IMC, índice de massa corporal, é calculado através da seguinte fórmula: IMC = massa / altura2
# Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário
# e mostre o valor do IMC e qual sua condição segundo o critério apresentado na tabela da OMS
#  (Organização Mundial de Saúde):

# Condição            #IMC em adultos
#abaixo do peso         abaixo de 18,5
# no peso normal        entre 18,5 e 25
# acima do peso         entre 25 e 30
# Obeso                 acima de 30

    print('IMC')
    altura = input('Altura (m): ')
    massa = input ('Massa (kg):  ')

    imc = massa / altura**2
    print('IMC: {:.2f}'.format(imc))
    if imc < 18.5 : print('Abaixo do peso')
    elif imc >= 18.5 and imc < 25: print('peso normal')
    elif imc >= 25 and imc < 30 : print('acima do peso')
    else: print('obeso')


def alg3():
    #Elabore um algoritmo que, dada a idade de um nadador, mostre sua classificação segundo uma das seguintes categorias:
# 5 até 7 anos: Infantil A;
# 8 até 10 anos: Infantil B;
# 11 até 13 anos: Juvenil A;
# 14 até 17 anos: Juvenil B;
# Maiores de 18 anos: Adulto.

    print('Faixa etária')
    idade = input("Idade: ")
    if idade < 5 : print('Nao classificado')
    elif idade >= 5 and idade <= 7: print('Infantil A')
    elif idade >= 8 and idade <= 10: print('Infantil B')
    elif idade >= 11 and idade <= 13: print('Juvenil A')
    elif idade >= 14 and idade <= 17: print('Juvenil B')
    elif idade >= 18 : print('Adulto')



def alg4():
    import math
    # Desenvolva um algoritmo que calcule as raízes de uma equação do 2o. grau na forma Ax2 + Bx + C (A ≠ 0),
    # levando em consideração a existência de raízes reais e empregando a fórmula de Bhaskara.

    print('Equacao de segundo grau')
    a = input('a: ')
    if a == 0 :
        print('Erro! a deve ser diferente de zero')
        return
    b = input('b: ')
    c = input('c: ')
    delta = b**2 - 4 * a * c
    if delta < 0 :
        print('Não existe raízes reais')
        return
    else:
        raiz1 = (-b + math.sqrt(delta))/(2*a)
        print('raiz1: {:.2f}'.format(raiz1))
        if delta != 0:
            raiz2 = (-b - math.sqrt(delta))/(2*a)
            print('raiz2: {:.2f}'.format(raiz2))

def alg5():
    # Dados três valores A, B, C, verificar se eles podem ser os comprimentos dos lados de um triângulo,
    # cada um é menor que a soma das medidas dos outros dois e maior que o valor
    # absoluto da diferença entre essas medidas (ou seja, | B − C | < A < B + C).
    # Caso as medidas fornecidas formem um triângulo, verificar se compõem um triângulo equilátero,
    # isósceles ou escaleno. Informar se não compuserem um triângulo.

    print('Triangulo')
    # lados = [0,0,0]
    # i = 0
    # somaTotal = 0
    # for i in range(0, 3, 1):
    #     lados[i] = input('lado {} do triangulo: '.format(i))
    #     somaTotal += lados[i]
    #
    # for i in range(0, 3, 1):
    #     a = lados[i]
    #     ladosRestantes = lados[:]
    #     ladosRestantes.remove(a)
    #
    #     b = ladosRestantes[0]
    #     c = ladosRestantes[1]
    #
    #     if a < abs(b - c) or a > (b + c):
    #         print('Não forma triângulo')
    #         return
    #
    # combinacaoDeLadosIguais = 0
    # for i in range(0,2,1):
    #     for j in range(i+1,3,1):
    #         if lados[i] == lados[j] : combinacaoDeLadosIguais += 1
    #
    # if combinacaoDeLadosIguais == 0 : print('Triangulo escaleno')
    # elif combinacaoDeLadosIguais == 1: print('Triangulo isosceles')
    # elif combinacaoDeLadosIguais == 3 : print ('Triangulo equilatero')

    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))

    #| B − C | < A < B + C)
    if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < (a + b)):
        #e triangulo, verificar agora qual triangulo
        if a == b == c : print("Triangulo equilatero")
        elif (a == b or a == c or b == c) : print("Triangulo Isosceles")
        else : print("Triangulo escaleno")
    else : print("Nao e triangulo")








def alg6():
#Escreva um algoritmo que leia três números inteiros e mostre o valor do maior deles
    print("alg6")



def alg7():
    #Escreva um algoritmo que leia três números inteiros e mostre-os em ordem crescente.
    print("alg7")





def alg8():

    #A tabela progressiva mensal do IRRF (Imposto de Renda Retido na Fonte) estabelece as seguintes alíquotas
    # (para o ano-calendário de 2018):
    #Base de cálculo mensal em R$          Alíquota %
    #Até 1.903,98                          -
    #De 1.903,99 até 2.826,65              7,5
    #De 2.826,66 até 3.751,05              15,0
    #De 3.751,06 até 4.664,68              22,5
    #Acima de 4.664,68                     27,5
    #Considerando que o valor da dedução mensal por dependente é de R$ 189,59; escreva um algoritmo que leia o salário de
    #  um funcionário (rendimento tributável mensal) e calcule o valor do imposto devido. Para verificar a estratégia de
    # cálculo e comparar seus resultados use o simulador disponível no site da Receita Federal em:
    # http://www.receita.fazenda.gov.br/Aplicacoes/ATRJO/Simulador/simulador.asp

    rendimentos = float(input("Remdimentos tributaveis: R$ "))
    dependentes = int(input("Dependentes: ")) # O valor da dedução é R$ 189,59 mensais, por dependente.

    previdencia = float(input("Previdencia: R$ "))
    outrasDeducoes = float(input("Outras deducoes: R$ "))

    descontoPorDependente = dependentes * 189.59
    baseDeCalculo = rendimentos - descontoPorDependente - outrasDeducoes - previdencia

    impostoDevido = 0

    faixas = [1903.98, 2826.65, 3751.05, 4664.68]
    aliquotas = [0, 7.5, 15, 22.5, 27.5]

    faixasAPagar = []
    impostoTotal = 0


    tempR = baseDeCalculo

    #verifica quais faixas o contribuinte vai entrar
    for i in range(0, len(faixas)):
        current = 0
        if i == 0:
            current = faixas[i]
        else:
            current = faixas[i] - faixas[i - 1]
        faixasAPagar.append (min (current, tempR))
        tempR -= current
        if tempR <= 0: break

    if tempR > 0: faixasAPagar.append(tempR)

    impostos = []
    print("\n\nFAIXA DA BASE DE CALCULO         ALIQUOTA           VALOR DO IMPOSTO")

    #calcula o imposto devido em cada uma das faixas
    for (i, faixa) in enumerate(faixasAPagar):
        imposto = faixa * aliquotas[i]/100
        impostos.append(imposto)
        impostoTotal += imposto
        print("{:.2f}                       {:.2f}%                         {:.2f}".format(faixa, aliquotas[i], imposto))

    efetiva = impostoTotal / rendimentos * 100
    print("\n\nAlíquota efetiva: {:.2f}%  Percentual do imposto sobre os rendimentos tributáveis.\n\n\n".format(efetiva))
    print("Senhor contribuinte, apesar do seu rendimento estar na faixa de {}%, sua alíquota efetiva é de {:.2f} %".format(aliquotas[len(faixasAPagar) -1], efetiva))



def sum(valores):
    total = 0
    for valor in valores:
        total += valor
    return  total



def fimAlg8(impostoDevido):
    print("Imposto devido : R$ {}".format(impostoDevido))

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
