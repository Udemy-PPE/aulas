"""
Seção 9 - Comprehensions
    Aulas 53 e 54 - List Comprehensions
    Aula 55 - Listas aninhadas
    Aula 56 - Dictionary Comprehension
    Aula 57 - Set Comprehensions
"""

from funcoes import (gera_lista, parouimpar)

def compre1(n):
    """
    List comprehension simples - aplica uma operação aos elementos de uma lista:
    :exemplo: Multiplica cada elemento da lista por 10
    var = [n * 10 for n in lista]
    """
    lista = gera_lista(n)

    var = [valor * n for valor in lista]

    print("List comprehension simples:")
    print(f"\tLista orginal: {lista}")
    print(f"\tLista multiplicada por {n}: {var}\n")

def compre2(n):
    """
    Aplica uma função com list comprehension:
    """
    lista = gera_lista(n)

    res = [parouimpar(numero) for numero in lista]

    print("List comprehension com funcao:")
    print(f"\tLista original: {lista}")
    print(f"\tLista após aplicar a funcao: {res}\n")

compre1(10)
compre2(10)
