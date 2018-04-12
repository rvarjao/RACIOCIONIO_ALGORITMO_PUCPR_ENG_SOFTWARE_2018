# coding=utf-8
#algumas funcoes comuns utilizadas em varios dos algoritmos

# ajusta as perguntas para ficar alinhada à direita
def ajustaPerguntas(perguntas):
    maxSize = 0
    #verifica a pergunta mais comprida
    for pergunta in perguntas:
        size = len(pergunta)
        if maxSize < size : maxSize = size

    #coloca o numero de espacos à esquerda necessarios
    for (i, pergunta) in enumerate(perguntas):
        size = len(pergunta)
        nEspacos = maxSize - size
        strEspacos = " "*nEspacos
        perguntas[i] = strEspacos + pergunta

    return perguntas