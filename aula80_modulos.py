"""
Aula 80 - Módulos

Declaração: import <arquivo.py>
Importa todo o módulo (funções, atributos, classes e propriedades)

Declaração: from <módulo> import <function>
Importa apenas o que se deseja
"""
# Importando apenas a função que se deseja
def gera_uniform(n):
    """
    Imprime um número aleatório com a função random.uniform
    :param = tamanho do intervalo
    """
    from random import uniform
    print("from random import uniform\n")
    print(f"\tNúmero aleatório entre 1 e {n} (uniform): {uniform(1,n)}\n")

gera_uniform(10)

# Importando outro módulo

def gera_random(n):
    """
    Gera uma lista com n números aleatórios com a função random.random
    :param = tamanho da lista
    """
    import random
    print("import random\n")

    lista = [] # Necessário declara devido ao escopo de variável

    for i in range(n):
        lista.append(round(random.random(),4))

    print(f"\tLista gerada com random.random(): \n\t {lista}")
    print(f"\tInverso da lista anterior: \n\t {lista[::-1]}\n")

gera_random(10)

# Importando módulo como alias

def alias_random():
    """
    Utlizando alias para módulos:

    import <modulo> as <alias>
    """
    import random as rdm

    print(f"Módulo como alias:")
    print("import random as rdm\n")
    print(f"\tNúmero aleatório com modulo rdm (alias): {rdm.random()}\n")

alias_random()

def func_alias():
    """
    Utilizando alias para funcoes:

    from <modulo> import <funcao> as <alias>
    """

    from random import randint as rdi

    print("Uma função com alias:")
    print("from random import randint as rdi\n")
    print(f"\tNúmero aleatório com funcao rdi (alias): {rdi(10,100)}\n")

func_alias()

def import_varias(n):
    """
    Costumamos utilizar tuplas para colocar múltiplos imports de um mesmo módulo.
    """

    from random import (
        random as rdm,
        randint as rdi,
        shuffle as shf,
        choice as ch
    )
    print("Varias funcoes com alias:\n")
    print(f"\tRandom (rdm): {rdm()}") # Gera um numero aleatório entre 0 e 1
    print(f"\tRandint (rdi): {rdi(1,n)}") # Gera um número aleatório em um intervalo definido
    lista = list(range(1,n))
    shf(lista)
    print(f"\tShuffle (shf): {lista}") # Embaralha um iterável
    print(f"\tChoice (ch): {ch(lista)}") # Escolhe um elemento não-vazio de um iterável

import_varias(10)
