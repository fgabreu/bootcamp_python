""""
Verificacao da qualidade de dados.
Você está analisando um conjunto de dados de vendas e precisa garantir que todos os
registros tenham valores positivos para `quantidade`e `preço`. Escreva um programa
que verifique esses campos e imprima "Dados Válidos"se ambos forem positivos ou
"Dados Inválidos" caso contrário.
"""

quantidade = 40
preco = 20

if quantidade > 0 and preco > 0:
    print("Valores validos")
else:
    print("Valoes inválidos")
