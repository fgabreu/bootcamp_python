import csv

caminho_arquivo: str = "/Volumes/SSD Felipe/CURSOS ENGENHARIA DE DADOS/BOOTCAMP PYTHON/04-aula_04/exemplo.csv"

arquivo_csv: list = []

with open(file=caminho_arquivo, mode="r", encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)