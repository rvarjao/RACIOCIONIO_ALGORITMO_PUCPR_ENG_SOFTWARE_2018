# coding=utf-8
# encoding=utf8
import sys
# from aetypes import end



#[1] No sistema de numeração romana as cifras escrevem-se com as letras I, V, X, L, C, D e M.
# Exemplo: 125 é representado por CXXV. Implemente um programa que leia um número inteiro,
# caso ele esteja dentro do intervalo de 1 a 999, mostre o número romano equivalente,
# caso contrário mostre “valor fornecido fora dos limites operacionais”.
# DICA: Utilize um vetor de strings para representar as unidades em números romanos,
#  outro para as dezenas e outro para as centenas.
# Separe, usando mod e div, o valor da unidade, da dezena e da centena do número fornecido e use estes valores como i
# ́ndices de consulta aos vetores em romanos.
# Observação: tabela com as referências da numeração romana disponível em
# http://pt.wikipedia.org/wiki/Números_romanos

def UnidadeEmRomanos(uni):
    if uni == 1: return "I"
    elif uni == 2: return "II"
    elif uni == 3: return "III"
    elif uni == 4: return "IV"
    elif uni == 5: return "V"
    elif uni == 6: return "VI"
    elif uni == 7: return "VII"
    elif uni == 8: return "VIII"
    elif uni == 9: return "IX"
    else: return ""

def DezenaEmRomanos(dez):
    if dez == 10: return "X"
    elif dez == 20: return "XX"
    elif dez == 30: return "XXX"
    elif dez == 40: return "XL"
    elif dez == 50: return "L"
    elif dez == 60: return "LX"
    elif dez == 70: return "LXX"
    elif dez == 80: return "LXXX"
    elif dez == 90: return "XC"
    else: return ""


def CentenaEmRomanos(cen):
    if cen == 100 : return "C"
    elif cen == 200 : return "CC"
    elif cen == 300 : return "CCC"
    elif cen == 400 : return "CD"
    elif cen == 500 : return "D"
    elif cen == 600 : return "DC"
    elif cen == 700 : return "DCC"
    elif cen == 800 : return "DCCC"
    elif cen == 900 : return "CM"
    else: return ""


def alg1():
    n = int(input("Digite um número entre 1 e 999: "))
    if n > 999:
        print("Fora dos limites operacionais")
    else:
        temp = n
        centena = divmod(temp, 100)[0]*100
        temp -= centena
        dezena = divmod(temp, 10)[0]*10
        temp -= dezena

        unidade = n - centena - dezena

        romCentena = CentenaEmRomanos(centena)
        romDezena = DezenaEmRomanos(dezena)
        romUnidade = UnidadeEmRomanos(unidade)

        romN = romCentena + romDezena + romUnidade

        print("{} = {}".format(n, romN))


def alg2():
    import json

#Escreva um “Mini-conjugador de verbos regulares”, ou seja, um programa que receba como entrada um verbo regular
# no infinitivo e mostre a sua conjugação. Como limitações: (i) considerar apenas verbos regulares da primeira
# conjugação (terminação “ar”), segunda conjugação (terminação “er”) e terceira conjugação (terminação “ir”);
# (ii) mostrar apenas os tempos Presente do Indicativo, Pretérito Perfeito e Futuro do Presente.
# DICA: Utilize um vetor de strings para representar os pronomes pessoais,
# e um vetor de desinências verbais para cada tempo/conjugação. A base deste exercício será resolvida em sala e
# estará disponível no BlackBoard, consulte-o com inspiração para sua implementação e como conceito para a
#  solução dos demais problemas.
# Observação: modelo de conjugação em http://pt.wikipedia.org/wiki/Modelos_de_conjugação_dos_verbos

    file_obj = open("LISTA_11_CONJUGACOES_VERBAIS.txt","r")
    text = file_obj.read()
    database = json.loads(text,encoding="utf-8")

    #1
    # primeira = info["1"]
    # primPP = primeira["Preterito Perfeito"]
    # nos = primPP[("nós")]


    verbo = input("Digite um verbo: ")

    termino = verbo[-2]
    conjugacao = ""
    if termino == "a" : conjugacao = "1"
    elif termino == "e" : conjugacao = "2"
    elif termino == "i" : conjugacao = "3"
    else:
        print("Erro ao ler verbo")
        return
    print("")

    radical = verbo[:len(verbo) -2]
    print("radical: {}".format(radical))

    pronomes = ["eu", "tu", "ele", "nós", "vós", "eles"]
    tempos = ["presente" , "preterito perfeito", "futuro do presente"]


    for tempo in tempos:
        print("--{}--".format(tempo))
        for pronome in pronomes:
            # pronomeUtf = pronome
            terminacao = database[conjugacao][tempo][pronome]
            print("{} {}{} ".format(pronome, radical, terminacao))
        print("\n")


def alg3():
    import json

# Leet (ou l33t) é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras,
# como números ou caracteres similares graficamente.
# O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e da Internet;
# veja explicação em: http://pt.wikipedia.org/wiki/Leet
# Usando vetores de strings e a tabela do alfabeto leet disponível no link acima,
# desenvolva um pequeno tradutor de leet, cuja função é ler uma frase do usuário e depois mostrá-la
#  em seu formato original e 3m $3μ f0rm4t0 l33t.
# Como são várias as possibilidades de tradução para cada caracter, mostre três formatos,
# fácil (deixando algumas letras normais),
# médio (trocando a maior parte das letras, mas com equivalentes mais conhecidos) e
# difícil (trocando todas as letras por equivalentes elaborados).
# DICA: Utilize um vetor de strings para armazenar cada uma das versões dos caracteres em leet
# (fácil, médio e difícil), use o valor de cada caracter fornecido na frase original como indice de acesso
# ao vetor (a função ord devolve o código do caracter).
    file_obj = open ("LISTA_11_DICIONARIO_NORMAL_PARA_LEET.txt", "r")
    text = file_obj.read ( )
    database = json.loads (text, encoding="utf-8")
    facilDict = database["facil"]

    print(facilDict)
    text = (input("Digite um texto: "))
    textLength = len(text)
    leetText = ""

    for c in text:
        upC = c.upper()
        exist = upC in facilDict
        if (upC in facilDict) and (facilDict[upC] != ""): leetText += facilDict[upC]
        else: leetText += upC

    print(leetText)


def alg4():
    # Elabore um algoritmo que leia um número inteiro (n), e se este número atender a condição 1 ≤ n ≤ 999,
    # mostre seu valor por extenso (exemplo: para n = 38, a saída será trinta e oito);
    # caso contrário mostre “Entrada fora dos limites operacionais”.
    
    #fazer com string fica mais fácil de pegar os valores

    # Elabore um algoritmo que leia um número inteiro (n), e se este número atender a condição 1 ≤ n ≤ 99,
    # mostre seu valor por extenso (exemplo: para n = 38, a saída será trinta e oito);
    # caso contrário mostre “Entrada fora dos limites operacionais”.

    n = int(input ("Digite um número entre 0 e 99: "))
    if n < 1 and n > 999:
        print ("Fora dos limites operacionais")
        return

    text = strNumero (n)
    print ("{} = {}".format (n, text))


def strNumero(n):
    import math

    if n < 1 and n > 999:
        print ("Fora dos limites operacionais")
        return ""
    else:
        if n < 10:
            return strUnidade (n)
        elif n == 10:
            return strDezena (n/10)
        elif n < 20:
            return strDezVinte (n)
        elif n == 100:
            return  "cem"
        else:


            #424   n/100 = 4,24  = 4
            c = math.floor(n / 100)
            txtCentena = strCentena(c)
            print("c: {}".format(c))

            #424 ->  424 - 400 = 24 -> 24/10 = 2,4 -> 2
            d = n - c * 100
            txtDezena = ""
            if d > 10 and d < 20:
                txtDezena = strDezVinte(d)
            else:
                d = math.floor((n - c * 100)/10)
                txtDezena = strDezena(d)

            print ("d: {}".format (d))

            u = n - d * 10 - c * 100
            txtUnidade = strUnidade(u)
            print ("u: {}".format (u))

            e1 = ""
            e2 = ""
            if (txtCentena != "" and (txtDezena != ""))  : e1 = " e "
            if txtUnidade != "" : e2 = " e "
            return "{}{}{}{}{}".format(txtCentena, e1, txtDezena, e2, txtUnidade)



def strUnidade(n):
    if n == 1: return "um"
    elif n == 2: return "dois"
    elif n == 3: return "tres"
    elif n == 4: return "quatro"
    elif n == 5: return "cinco"
    elif n == 6: return "seis"
    elif n == 7: return "sete"
    elif n == 8: return "oito"
    elif n == 9: return "nove"
    else: return ""


def strDezena(n):
    if n == 1: return "dez"
    elif n == 2: return "vinte"
    elif n == 3: return "trinta"
    elif n == 4: return "quarenta"
    elif n == 5: return "cinquenta"
    elif n == 6: return "sessenta"
    elif n == 7: return "setenta"
    elif n == 8: return "oitenta"
    elif n == 9: return "noventa"
    else: return ""


def strDezVinte(n):
    if n == 11: return "onze"
    elif n == 12: return "doze"
    elif n == 13: return "treze"
    elif n == 14: return "quatorze"
    elif n == 15: return "quinze"
    elif n == 16: return "dezesseis"
    elif n == 17: return "dezessete"
    elif n == 18: return "dezoito"
    elif n == 19: return "dezenove"
    else: return ""


def strCentena(n): 
    #deve-se passar o numero total e a funcao vai retornar a centena
    if   n == 1 : return "cento"
    elif n == 2 : return "duzentos"
    elif n == 3 : return "trezentos"
    elif n == 4 : return "quatrocentos"
    elif n == 5 : return "quinhentos"
    elif n == 6 : return "seiscentos"
    elif n == 7 : return "setecentos"
    elif n == 8 : return "oitocentos"
    elif n == 9 : return "novecentos"
    else: return ""


def alg5():
    import os

# Use the next line every time you wish to 'clear' the screen. Works with Windows and Linux.
    os.system ('cls' if os.name == 'nt' else 'clear')

#     Desenvolva um programa para o “Jogo da Forca”.
# Para tal, crie um vetor de strings inicializado com um conjunto de palavras-chave
# (por exemplo: nomes de capitais do Brasil, ou times de futebol da Serie A ou Países da América do Sul, etc).
# Sorteie uma das palavras para ser o segredo e forneça seis vidas para o usuário acertar o segredo.
# A cada rodada informe o número de vidas disponíveis e a disposição das letras acertadas e ausentes
# na palavra segredo (lembre de quando brincava com este jogo em caderno na infância),
# mostre também quais as letras que já foram usadas
# (e não compute acerto ou erro no caso do usuário repetir uma letra já fornecida).

    selecionado = EscolhaUmaPalavra()
    palavra = selecionado[ "valor" ].upper()

    # print("selecionado: {}".format(selecionado))
    titulo = "---FORCA---\n"
    titulo += "Categoria: {}".format(selecionado["categoria"]) + "\n"
    titulo += "Dica: {}\nnúmero de letras: {}".format(selecionado["dica"], len(palavra))
    print(titulo)

    vidas = 5
    charOculto = "*"

    palpite = ""
    for (i,char) in enumerate(palavra):
        if char == " " : palpite += char
        else: palpite += charOculto
    # tira os espacos em branco do palpite


    #COLOCAR UM ARRAY COM AS LETRAS QUE JA FORAM USADAS
    letras = []
    mensagem = ""

    fimDeJogo = False
    continuaLoop = True


    while (continuaLoop):

        os.system('cls' if os.name == 'nt' else 'clear')

        strLetras = "Letras já palpitadas:["

        for (i, letra) in enumerate(letras):
            strLetras += letra
            if i < len(letras) - 1:
                strLetras += ","
        strLetras += "]"

        print(titulo)
        print(strLetras)
        print("PALAVRA: {}".format (palpite))
        print(mensagem)
        printForca(vidas)

        if fimDeJogo :
            continuaLoop = False
            continue

        c = input("Digite uma letra: ").upper()



        if letras.__contains__(c):
            mensagem = "Você já tentou essa letra."
        else:
            letras.append(c)
            letras.sort()
            if palavra.find(c) == -1 :
                mensagem = "Palavra secreta não possui a letra: {}".format(c)
                vidas -= 1
                if vidas == 0 :
                    mensagem = "Você perdeu.\nPalavra secreta é: {}".format(palavra)
                    fimDeJogo = True
            else:
                temp = ""
                for (i, char) in enumerate(palavra):
                    if char == c : temp += char
                    else: temp += palpite[i]
                palpite = temp
                print("-"*30)
                if palpite.find(charOculto) == -1:
                    mensagem = "Você venceu"
                    fimDeJogo = True



def printForca(vidasRestantes):
    # strForca = "Vidas restantes: {}\n".format(vidasRestantes)
    strForca = "_____\n"
    if vidasRestantes == 5:
        strForca += "|\n"*3
    if vidasRestantes == 4:
        strForca += "|   O\n"
        strForca += "|\n" * 2
    if vidasRestantes == 3:
        strForca += "|   O\n"
        strForca += "|   |\n"
        strForca += "|\n"
    if vidasRestantes == 2:
        strForca += "|   O\n"
        strForca += "|  -|\n"
        strForca += "|\n"
    if vidasRestantes == 1:
        strForca += "|   O\n"
        strForca += "|  -|-\n"
        strForca += "|\n"
    if vidasRestantes == 0:
        strForca += "|   O\n"
        strForca += "|  -|-\n"
        strForca += "|  / \\\n"
    print(strForca)

def EscolhaUmaPalavra():
    import json
    import random

    file_obj = open ("LISTA_11_FORCA.txt", "r")
    text = file_obj.read()
    database = json.loads(text, encoding="utf-8")


    categorias = ["filmes", "estados e capitais", "paises e capitais", "times", "nomes dos alunos"]

    #escolhe uma categoria
    categoria = categorias[random.randrange(0,len(categorias))]

    #pega todos os itens daquela categoria
    itens = database[categoria]

    #escolhe um item daquela categoria
    item = itens[random.randrange(0,len(itens))]

    textoDica = ""
    chave = ""
    #como o banco de dados nao esta padronizado, dependendo da categoria escolhida tem que
    #ser feita a busca em chaves diferentes
    if categoria == "filmes":
        chave = "titulo"
        textoDica = "Ganhador da {}a edicao do Oscar".format(item["edicao"])
    elif categoria == "times":
        chave = "nome"
        textoDica = "Time da 1a divisão do Campeonato Brasileiro de 2018"
    elif categoria == "estados e capitais":
        chave = "capital"
        estado = item["estado"]
        textoDica = "Capital de {}".format(estado)
    elif categoria == "paises e capitais":
        chave = "pais"
        continente = item["continente"]
        textoDica = "Continente: {}".format(continente)
    elif categoria == "nomes dos alunos":
        chave = "nome"
        textoDica = "Nome de um aluno(a)"

    valor = item[chave]
    retornar = {"categoria" : categoria, "valor" : valor, "dica" : textoDica}

    return retornar



a = 1
nProblemas = 5

while 0 < a <= nProblemas:
    print("-"*40)
    a = int(input ('Qual algoritmo voce deseja?: '))
    if (a == 1) : alg1()
    elif (a == 2) : alg2()
    elif (a == 3) : alg3()
    elif (a == 4) : alg4()
    elif (a == 5) : alg5()

