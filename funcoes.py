"""
Funções genéricas utilizadas nas aulas
"""
def gera_lista(n):
    """
    Gera uma lista aleatória de tamanho 'n'
    """
    from random import shuffle

    lista = list(range(1,n))
    shuffle(lista)

    return lista

def parouimpar(n):
    """
    Retorna se o valor é par ou ímpar.
    """
    if divmod(n,2)[1]:
        return "Ímpar"
    return "Par"
