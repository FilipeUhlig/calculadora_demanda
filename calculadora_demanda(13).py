"""
Programa: Calculadora de demanda
Descrição: Este programa calcula a demanda de um certo bem.
Autor: Filipe
Data: 06/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis

#Entrada de dados
b = float(input("Qual é a renda do consumidor? "))
p = float(input("Qual é o preço deste bem? "))

#Processamento de dados
q = (b/p)

#Saida de dados
print(f"A quantidade demandada é de {q}.")
