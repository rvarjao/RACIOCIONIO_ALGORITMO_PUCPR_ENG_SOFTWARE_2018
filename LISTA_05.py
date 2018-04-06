# coding=utf-8
#PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ ESCOLA POLITÉCNICA
#RACIOCÍNIO ALGORÍTMICO
#PROF. HENRI FREDERICO EBERSPÄCHER
#Estudante: Ricardo Varjão

# PROBLEMAS LISTA 5: Selecao Composta

def alg1():
#[1] A partir das informações contidas na tabela abaixo, elabore um algoritmo que leia a massa em kg de um
# boxeador e mostre a qual categoria ele pertence.
# Caso ele não se encaixe, informe “Categoria inferior a Super-médio”.
# Lembrando que 1 quilograma = 2,20462262 libras.
# Massa                 Categoria
# 201 lb ou mais        Peso-pesado
# 176 até 200 lb       Cruzador
#169 até 175 lb        Meio-pesado
#161 até 168 lb        Super-médio
    massaKg = float(input("Massa do lutador (kg): "))
    massaLb = 2.20462262 * massaKg
    limites = [161, 169, 176, 201]
    categorias = ["Super-médio", "Meio Pesado", "Cruzador", "Peso-Pesado"]
    print("massa em lb: {}".format(massaLb))

    if massaLb < limites[0] :
        print("Categoria inferior a Super-médio")
        return

    categoria = categorias[3]

    for (i, limite) in enumerate(limites):
        if i == 0 : continue #ja foi feita essa verificacao
        else:
            #print("i:{}  limite:{}   categoria: {}".format(i, limites[i], categorias[i]))
            if massaLb <= limite :
                categoria = categorias[i-1]
                break

    print("-"*10)
    print("Peso (kg): {:.2f}    \nPeso (lb): {:.2f}".format(massaKg, massaLb))
    print("Categoria: {}".format(categoria))
    print("-" * 10)


def alg2():
# Uma determinada loja de varejo classifica seus produtos utilizando códigos conforme
# descrito na tabela abaixo. Elabore um algoritmo que leia o código de um produto e mostre sua classificação.
# Para qualquer código inexistente, mostre “Código inválido”.

# Código            Classificação
# 1                 Alimento não perecível
# 2, 3 ou 4         Alimento perecível
# 5 ou 6            Vestuário
# 7                 Higiene Pessoal
# 8 até 15          Limpeza e utensílios domésticos

    #cadastro das categorias
    categorias = []
    categorias.append({"codigoInicial" : 1, "codigoFinal" : 1, "descricao" : "Alimento não perecível"})
    categorias.append ({"codigoInicial": 2, "codigoFinal": 4, "descricao": "Alimento perecível"})
    categorias.append ({"codigoInicial": 5, "codigoFinal": 6, "descricao": "Vestuário"})
    categorias.append ({"codigoInicial": 7, "codigoFinal": 7, "descricao": "Alimento perecível"})
    categorias.append ({"codigoInicial": 8, "codigoFinal": 15, "descricao": "Limpeza e utensílios domésticos"})

    inputCodigo = int(input("Digite o codigo do produto: "))

    categoriaSelecionada = "Código inválido"

    for categoria in categorias:
        if categoria["codigoInicial"] <= inputCodigo <= categoria["codigoFinal"]:
            categoriaSelecionada = categoria["descricao"]
            break

    print("Categoria Selecionada: {}".format(categoriaSelecionada))


def alg3():
    #Em uma determinada loja de eletrodomésticos, os produtos podem ser adquiridos da seguinte forma:
    #Opção                Condição          Cálculo
# 1             à vista                 8% de desconto
# 2             em 2 parcelas           4% de desconto, dividido em duas vezes
# 3             em 3 parcelas           sem desconto, dividido em três vezes
# 4             em 4 parcelas           4% de acréscimo, dividido em quatro vezes

#Elabore um algoritmo que leia a opção do cliente e o preço de tabela do produto,
#mostrando então o valor calculado conforme a condição escolhida.

    valorDoProduto = float(100) #valor lido do sistema
    opcoes = []
    opcoes.append({"codigo" : 1, "nParcelas" : 1 , "fator" : -0.08})
    opcoes.append({"codigo" : 2, "nParcelas" : 2 , "fator" : -0.04})
    opcoes.append({"codigo" : 3, "nParcelas" : 3 , "fator" : 0.00})
    opcoes.append({"codigo" : 4, "nParcelas" : 4 , "fator" : 0.04})

    inputOpcao = int(input("Digite a opcao de pagamento: "))
    valorDasParcelas = valorDoProduto
    nParcelas = 0
    valorTotal = 0

    for opcao in opcoes:
        if inputOpcao == opcao["codigo"]:
            fator = opcao["fator"]
            nParcelas = opcao["nParcelas"]
            valorTotal = valorDoProduto *(1 + fator)
            valorDasParcelas = valorTotal / nParcelas
            break
    print("\n\n")
    print("   Valor do produto: R$ {:.2f}".format(valorDoProduto))
    print(" Número de parcelas:    {}".format(nParcelas))
    print(" Valor das parcelas: R$ {:.2f}".format(valorDasParcelas))
    print("Valor total a pagar: R$ {:.2f}".format(valorTotal))
    print("\n\n")




def alg4():
    import requests
    import json

    #Uma empresa de câmbio permite a compra de dólares, libras e euros.
    # Elabore um algoritmo que leia o código da moeda que o cliente quer comprar e qual o
#   montante que ele quer adquirir nessa moeda. Mostre então quanto ele deverá pagar em reais
#  para concretizar a operação.
# Além da cotação, a empresa cobra uma comissão de 5% (quando o valor for menor que R$ 1.000),
# ou de 3% (quando maior ou igual a R$1.000).

#fiz de uma forma diferente, o app faz uma requisicao utilizando a api: https://www.exchangerate-api.com/app/dashboard

#    inputMoeda = str(input("moeda\nUSD - Dolar\nGBP	United Kingdom Pound\nEUR	Euro Member Countries: "))

    # primeiro puxa a cotacao de todos e mostra numa tabela

    # Where USD is the base currency you want to use  (i'm using BRL)
    url = 'https://v3.exchangerate-api.com/bulk/4d52cef7ad4a863ae9e86e9e/BRL'

    # Making our request
    response = requests.get(url)
    data = response.json()

    # Your JSON object
    # print data

    # dumps the json object into an element
    json_str = json.dumps (data)
    # load the json to a string
    resp = json.loads (json_str)
    # print the resp
    # print (resp)


    rates = resp['rates']
    print("Cotacao: BRL 1,00")
    print("Data:")
    print("resp: {}".format(resp))

    for key in rates:
        print("BRL 1,00 = {} {} ".format(key, rates[key]))

    moeda = str(raw_input("moeda: ")).upper()
    valor = input("valor a comprar ({}): ".format(moeda))

    # extract an element in the response
    cotacao = resp['rates'][moeda]

    valorTransacao = valor / cotacao

    # Além da cotação, a empresa cobra uma comissão de 5% (quando o valor for menor que R$ 1.000),
    # ou de 3% (quando maior ou igual a R$1.000).

    comissao = 0
    if valorTransacao < 1000 : comissao = 0.05
    else: comissao = 0.03

    valorComissao = valorTransacao * comissao
    valorTotal = valorTransacao + valorComissao

    print("\n\n---------------------------------")
    print("Cotacao:            BRL 1,00  = {} {}".format(moeda, cotacao))
    print("Valor da transacao: BRL {:.2f}".format(valorTransacao))
    print("Valor da comissao:  BRL {:.2f}".format(valorComissao))
    print("Valor total:        BRL {:.2f}".format(valorTotal))
    print("---------------------------------\n\n")



def alg5():
    import random
#Escreva um algoritmo que jogue Joquempô (Pedra, Papel e Tesoura) com o usuário;
# ou seja ele escolhe randomicamente sua jogada, lê a opção do usuário e mostra o resultado:
# vitória do computador, vitória do usuário ou empate.
    jogador = "a"
    while jogador != "e":
        print("P - PEDRA")
        print("L - PAPEL")
        print("T - TESOURA")

        possiveis = []
        possiveis.append({"id" : 0, "codigo" : "p" , "descricao" : "PEDRA"})
        possiveis.append({"id" : 1, "codigo" : "l" , "descricao" : "PAPEL"})
        possiveis.append({"id" : 2, "codigo" : "t" , "descricao" : "TESOURA"})


        jogador = raw_input("JOGADA: ")
        jogador = jogador.lower() #garantir que nao tem letra maiscula

        computador = possiveis[random.randrange(0,2,1)]["id"]

        resultado = joquempoResultado(jogador, computador)
        ganhador = ""

        if resultado == 0 : ganhador = "Jogador ganhou"
        elif resultado == 1 : ganhador = "Computador ganhou"
        else : ganhador = "Empate"

        # mydict = {'george': 16, 'amber': 19}
        # print(list (mydict.keys ( ))[ list (mydict.values ( )).index (16) ])  # Prints george

        print(possiveis[0])

        print("{}    jogador:  {}  X {}  computador".format(ganhador, jogador, computador))



def joquempoResultado(a, b): #returna 0 -> a ganhou, 1 -> b ganhou, -1 -> empate
    if a == b : return  -1
    else:
        if a == 'p' and b == 't': return 0
        elif a == 'p' and b == 'l': return 1

        elif a == 'l' and b == 't': return 1
        elif a == 'l' and b == 'p': return 0

        elif a == 't' and b == 'l': return 0
        elif a == 't' and b == 'p': return 1


def alg6():
#     O plano cartesiano está divido em quatro partes pelos eixos X (eixo das abcissas)e Y (eixo das ordenadas)
# chamadas de quadrantes. O quadrante superior da direita é o primeiro,
# o superior esquerdo é o segundo, o inferior esquerdo é o terceiro e o inferior direito é o quarto.
# Elabore um algoritmo que leia uma coordenada (x, y) do plano cartesiano e informe em qual quadrante
# este ponto se encontra.

    ponto = raw_input("Digite o ponto (x, y): ")
    valores = stringSeparetedBy(ponto, ",")

    print("words: {}".format(valores))

    x = float(valores[0])
    y = float(valores[1])

    if x == 0 : print("Sobre o eixo x")
    elif y == 0 : print("Sobre o eixo y")
    if x > 0 and y > 0 : print("Primeiro quadrante")
    if x < 0 and y > 0 : print("Segundo quadrante")
    if x < 0 and y < 0 : print("Terceiro quadrante")
    if x > 0 and y < 0 : print("Quarto quadrante")



def stringSeparetedBy(text, separator):
    words = []
    cWord = ""
    for char in text:
        if char == separator:
            words.append(cWord)
            cWord = ""
        else:
            cWord += char
    if cWord != "" : words.append(cWord)
    return words


def alg7():
#Elabore um algoritmo que leia um número inteiro (n), e se este número atender a condição 1 ≤ n ≤ 99,
# mostre seu valor por extenso (exemplo: para n = 38, a saída será trinta e oito);
# caso contrário mostre “Entrada fora dos limites operacionais”.

    n = input("Digite um número entre 0 e 99: ")
    if n < 1 and n > 99 :
        print("Fora dos limites operacionais")
        return

    text = strNumero(n)
    print("{} = {}".format(n, text))


def strNumero(n):
    if n < 1 and n > 99 :
        print("Fora dos limites operacionais")
        return ""
    else:
        if n < 10: return strUnidade(n)
        elif n == 10 : return strDezena(n)
        elif n < 20 : return strDezVinte(n)
        else:
            text = ""
            d = round(n / 10)
            text = strDezena(d)
            u = n - d * 10
            if u != 0 : text += " e " + strUnidade(u)
            return text



def strUnidade(n):
    if n == 1 : return "um"
    elif n == 2 : return "dois"
    elif n == 3 : return "tres"
    elif n == 4 : return "quatro"
    elif n == 5 : return "cinco"
    elif n == 6 : return "seis"
    elif n == 7 : return "sete"
    elif n == 8 : return "oito"
    elif n == 9 : return "nove"

def strDezena(n):
    if n == 1 : return "dez"
    elif n == 2 : return "vinte"
    elif n == 3 : return "trinta"
    elif n == 4 : return "quarenta"
    elif n == 5 : return "cinquenta"
    elif n == 6 : return "sessenta"
    elif n == 7 : return "setenta"
    elif n == 8 : return "oitenta"
    elif n == 9 : return "noventa"

def strDezVinte(n):
    if n == 11 : return "onze"
    elif n == 12 : return "doze"
    elif n == 13 : return "treze"
    elif n == 14 : return "quatorze"
    elif n == 15 : return "quinze"
    elif n == 16 : return "dezesseis"
    elif n == 17 : return "dezessete"
    elif n == 18 : return "dezoito"
    elif n == 19 : return "dezenove"



a = 0
while 0 <= a <= 7:
    a = input ('Qual algoritmo voce deseja?: ')
    if (a == 1) : alg1()
    elif (a == 2) : alg2()
    elif (a == 3) : alg3()
    elif (a == 4) : alg4()
    elif (a == 5) : alg5()
    elif (a == 6) : alg6()
    elif (a == 7) : alg7()
