#Exemplo que causa TypeError

"""nome = "Felipe"

try:
    resultado = len(nome)
    print(resultado)
except TypeError as e:
    print(e) # Imprime a mensagem de erro
else:
    print("Tudo ocorreu bem")
finally:
    print("Operação com sucesso")"""



numero = int(input("Insira um número :"))
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")