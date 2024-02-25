#Desafio do dia: Cálculo de bônus com entrada do usuário
"""
Escreva um progra em Python que solicita ao usuário para digitar seu nome, o valoar do seu salário mensal
e o valor do bônus que recebeu. O programa deve então, imprimir uma mensagem saudando o usuário pelo nome
e informando o valor do salário em comparacao com o bônus recebido.
"""

#Valor do bonus para 2024:
CONST_BONUS = 1000

# Pedindo para entrar com o nome:
nome_usuario = input("Digite o seu nome: ")

# Pedindo para entrar com o salário:
salario_usuario = float(input("Digite o valor mensal do seu salário: "))

# Pedindo para entrar com o bonus:
bonus_usuario = float(input("Digite o valor do bônus recebido: "))

#calculo do valor do bônus: 
valor_bonus = CONST_BONUS + salario_usuario * bonus_usuario

#Imprima a mensagem incluindo nome do usuário e o valor do bônus:
print(f"O usuário {nome_usuario} possui o bonus de: {valor_bonus}")

