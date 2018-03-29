# coding=utf-8
# PROBLEMAS 4: Selecao Composta
# #Ricardo Varjao

# A tabela progressiva mensal do IRRF (Imposto de Renda Retido na Fonte) estabelece as seguintes alíquotas
# (para o ano-calendário de 2018):
# Base de cálculo mensal em R$          Alíquota %
# Até 1.903,98                          -
# De 1.903,99 até 2.826,65              7,5
# De 2.826,66 até 3.751,05              15,0
# De 3.751,06 até 4.664,68              22,5
# Acima de 4.664,68                     27,5
# Considerando que o valor da dedução mensal por dependente é de R$ 189,59; escreva um algoritmo que leia o salário de
#  um funcionário (rendimento tributável mensal) e calcule o valor do imposto devido. Para verificar a estratégia de
# cálculo e comparar seus resultados use o simulador disponível no site da Receita Federal em:
# http://www.receita.fazenda.gov.br/Aplicacoes/ATRJO/Simulador/simulador.asp

rendimentos = float (input ("Remdimentos tributaveis: R$ "))
dependentes = int (input ("Dependentes: "))  # O valor da dedução é R$ 189,59 mensais, por dependente.

previdencia = float (input ("Previdencia: R$ "))
outrasDeducoes = float (input ("Outras deducoes: R$ "))

descontoPorDependente = dependentes * 189.59
baseDeCalculo = rendimentos - descontoPorDependente - outrasDeducoes - previdencia

impostoDevido = 0

faixas = [ 1903.98, 2826.65, 3751.05, 4664.68 ]
aliquotas = [ 0, 7.5, 15, 22.5, 27.5 ]

faixasAPagar = [ ]
impostoTotal = 0

tempR = baseDeCalculo

# verifica quais faixas o contribuinte vai entrar
for i in range (0, len (faixas)):
    current = 0
    if i == 0:
        current = faixas[ i ]
    else:
        current = faixas[ i ] - faixas[ i - 1 ]
    faixasAPagar.append (min (current, tempR))
    tempR -= current
    if tempR <= 0: break

if tempR > 0: faixasAPagar.append (tempR)

impostos = [ ]
print("\n\nFAIXA DA BASE DE CALCULO         ALIQUOTA           VALOR DO IMPOSTO")

# calcula o imposto devido em cada uma das faixas
for (i, faixa) in enumerate (faixasAPagar):
    imposto = faixa * aliquotas[ i ] / 100
    impostos.append (imposto)
    impostoTotal += imposto
    print("{:.2f}                       {:.2f}%                         {:.2f}".format (faixa, aliquotas[ i ], imposto))

efetiva = impostoTotal / rendimentos * 100
print("\n\nAlíquota efetiva: {:.2f}%  Percentual do imposto sobre os rendimentos tributáveis.\n\n\n".format (efetiva))
print("Senhor contribuinte, apesar do seu rendimento estar na faixa de {}%, sua alíquota efetiva é de {:.2f} %".format (
    aliquotas[ len (faixasAPagar) - 1 ], efetiva))

