"""
Aula 12 - Recebendo dados do usuário
"""

import getpass

# Entrada de dados
""" Formato 1 - print + input
print("Qual o seu nome?")
nome = input().strip().title()
"""

'''Formato 2 - input'''
nome = input("Qual o seu nome? ").strip().title()

# Processamento

def centralizado(arg):
    print ("Seja bem vindo(a) {0}".format(arg).center(50))

centralizado(nome)

# Saída de dados

# print('Seja bem vindo(a) %s' % nome) # Python 2.x

print("Seja bem vindo(a) {0}".format(nome)) # Python 3.x

# print (f'Seja bem vindo(a) {nome}') # Python 3.7
