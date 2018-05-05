# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ ESCOLA POLITÉCNICA
# RACIOCÍNIO ALGORÍTMICO
# PROF. HENRI FREDERICO EBERSPÄCHER
# Estudante: Ricardo Varjão

#Problemas Sequenciais I
#-------------------------------


def alg1():
    #Faca um algoritmo que leia um numero inteiro e escreva seu sucessor e seu antecessor
    a = int(input('insira um numero: '))
    print(a)
    print(a + 1)
    print(a - 1)

def alg2():
    # Escreva um algoritmo que leia o ano de nascimento de uma pessoa,
    # calcule e mostre a idade que ele completara em 2018
    import datetime
    now = datetime.datetime.now()

    birthYear = int(input('ano de nascimento: '))
    idade = now.year - birthYear
    print("idade: {}".format(idade))
    return


def alg3():
    # Construa um algoritmo que leia o valor do salario de um determinado funcionario,
    # calcule quantos salarios minimos este funcionario recebe
    salMin = 900
#    salMin = float(input("valor do salario minimo: ")) #pode-se colocar como input
    salTrab = float(input("salario do trabalhador: "))
    print("o trabalhador recebe {:.2f} salarios minimos ".format(salTrab / salMin))

def alg4():
    # faca um algoritmo que leia o diametro de um circulo e calcule a sua area
    diametro = float(input("diametro: "))
    pi = 3.14159265359
    raio = diametro / 2
    print("area do triangulo: {:.2f}".format(pi * raio * raio))


def alg5():
    # elabore um algoritmo que leia o preco de catalogo de um produto e entao,
    # mostre queia os valores com:
    # 5% de acrescimento em 3 parcelas,
    # preco de tabela em 2 parcelas
    # preco a vista com 5% de desconto
    preco = float(input("preco do produto: R$ "))
    aVista = preco * ( 1 - 0.05)
    emTresParcelas = preco * (1 + 0.05)
    emDuasParcelas = preco
    print("a vista: R$", aVista)
    print("em duas parcelas: R$ {:.2f}".format(emDuasParcelas))
    print("em tres parcelas: R$ {:.2f}".format(emTresParcelas))

def alg6():
#Escreva um algoritmo que leia o valor dos dois catetos de um triangulo
#retangulo e calcule a sua hipotenusa
    cat1 = float(input("cateto 1: "))
    cat2 = float(input("cateto 2: "))
    hip = pow(pow(cat1, 2) + pow(cat2, 2), 0.5)
    print("hipotenusa : {:.2f}".format(hip))

def alg7():
#faca um algoritmo que dado um horario fornecido pelo usuario (hora, minuto e segundo)
#calcule o total de minutos e o total de segundos que transcorreram
#desde o inicio do dia
    hora =    float (input ("   hora: "))
    minuto =  float (input (" minuto: "))
    segundo = float (input ("segundo: "))
    minutos = hora * 60 + minuto + segundo / 60
    segundos = minutos * 60
    print("minutos: {:.2f}".format(minutos))
    print("segundos: {:.2f}".format(segundos))


def alg8():
    # elabore um algoritmo que leia a razao (r) de uma PA e seu primeiro termo,
    # calcular o 15o termo
    # lembrete: a_n = a_1 + (n-1) . r

    # pode ser feito como input
    # #n = input("termo: ")
    n = 15
    a1 = int(input ('a1 = '))
    r = int(input ('razao: '))
    print("15o termo: {}".format(termoPA (a1, r, n)))
    return


def alg9():
    # elabore um algoritmo que leia a razao (q) de uma PG e seu primeiro termo,
    # calcular o 25o termo
    # lembrete: a_n = a_1 * q^(n-1)

    # pode ser feito como input
    # #n = input("termo: ")

    n = 25
    a1 = int(input('a1 = '))
    q = int(input("razao = "))
    print("25o termo :{}".format(termoPG(a1, q, n)))

def termoPA(a1, r, n):
    return a1 + (n - 1) * r

def termoPG(a1, q, n):
    return a1 * pow(q, n - 1)


def alg10():
    import  math
# construa um algoritmo que calcule a quantidade de latas de tinta necessarias
#    e o custo para pintar tanques cilindricos de combustivel, em que sao
#fornecidos a altura e o raio desse cilindro
#sabendo que:
#a lata de tinta custa R$ 50.00
#cada lata contem 5 litros
#cada litro pinta 3 metros quadrados
#dados de entrada: altura e raio
#dados de saida: custo em R$ e quantidade de latas

    #inputs
    h = float(input ("altura: "))
    r = float(input ("raio: "))

    #calculos da area do cilindro
    pi = 3.14159265359
    areaBase = float(pi * pow(r , 2))
    l = float(2 * pi * r)
    areaLados = float(l * h)
    areaTotal = areaBase + areaLados

    #calculos do volume de tinta
    volumeLataDeTinta = float(5)    #volume de cada lata de tinta
    areaLitroDeTinta = float(3)     #valor que cada litro de tinta pinta

    litrosNecessarios = areaTotal / areaLitroDeTinta

    #latas de tinta
    # arredonda para cima o numero de latas necessarias
    nLatas = math.ceil(litrosNecessarios / volumeLataDeTinta)
    #custo
    valorLata = 50
    valorTotal = float(nLatas * valorLata)

    #resultado final
    print ("Tanque  altura: {} m  raio: {} m ".format(h, r))
    print ('Quantidade de latas necessarias: {:.0f}'.format(nLatas))
    print ('Area total: {:.2f} m2'.format(areaTotal))
    print ('Custo total: {:.2f}'.format(valorTotal))


a = 1
nProblemas = 10

while 0 < a <= nProblemas:
    print ("-" * 40)
    a = int (input ('Qual algoritmo voce deseja?: '))
    if (a == 1):   alg1 ( )
    elif (a == 2): alg2 ( )
    elif (a == 3): alg3 ( )
    elif (a == 4): alg4 ( )
    elif (a == 5): alg5 ( )
    elif (a == 6): alg6 ( )
    elif (a == 7): alg7 ( )
    elif (a == 8): alg8 ( )
    elif (a == 9): alg9 ( )
    elif (a == 10): alg10 ( )
