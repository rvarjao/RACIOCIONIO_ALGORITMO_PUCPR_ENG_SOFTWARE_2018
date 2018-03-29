# coding=utf-8

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
