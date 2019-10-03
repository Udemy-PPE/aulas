"""
Aula 12 - Recebendo dados do usuário
: parametro: Nome a ser processado.
"""

# Entrada de dados
''' Formato 1 - print + input
print("Qual o seu nome?")
nome = input().strip().title()
'''

'''Formato 2 - apenas input'''
nome = input("Qual o seu nome? ")

# Processamento

def capitalize(arg):
    """
    Funcao para colocar as letras iniciais em maiúsculas
    : param arg: String a ser processada
    : retorno: Retorna a string capitalizada
    """
    arg = arg.title()
    return arg

def centralizado(arg):
    """
    Funcao para imprimir a string centralizada
    : param arg: String a ser processada
    """
    print (f"Seja bem vindo(a) {arg}".center(50))


# Saída de dadoslp()

'''
# Python 2.x:
print('Seja bem vindo(a) %s' % nome)

# Python 3.x:
print("Seja bem vindo(a) {0}".format(nome))
'''

print (f'Seja bem vindo(a) {nome}') # Saída não formatada
print(f'Seja bem vindo(a) {capitalize(nome)}') # Saida formatada (letras maiúsculas)
centralizado(capitalize(nome)) # Saída formatada e centralizada
