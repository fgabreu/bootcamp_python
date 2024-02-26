# Armazenar informações de um livro, incluindo título, autor e ano de publicacão. Imprima cada informação.

from typing import Dict, Any


livro:  Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "Alguem",
    "Ano": 2005
}

lista_elementos = livro.items()
for elemento in lista_elementos:
    print(elemento)
