# Aula 15 - Tipo String

# Aspas duplas:
aplicativo = "Hiren's boot"
print(aplicativo)

# Aspas simples:
aplicativo = 'Kali Linux'
print(aplicativo)

# Verificando o tipo de variável:
print(f"Tipo = {type(aplicativo)}")

# Verificando o tamanho da string:
print(f"Comprimento da string = {len(aplicativo)}")

print(f"Comprimento da string: {aplicativo.__len__()}")

# Acessando as letras da string:
print(aplicativo[0:5])

# Criando uma lista - elementos separados pelor 'espaço'
print(aplicativo.split())

# Cada palavra do split
print(aplicativo.split()[0])
print(aplicativo.split()[1])

# Invertendo a string:
print(aplicativo[::-1])

# Invertendo as palavras:
def invert_palavras(aplicativo):
    """ Inverte a sequência de palavras da string
        string.split()[::-1]
        param: string
    """
    print(aplicativo.split()[::-1])

invert_palavras(aplicativo)

# Substituindo caracteres:
def substituindo(aplicativo, caracter, substituto):
    """ Substitui os caracteres na string
        string.replace(caracter, substituto)
        param: string, caracter, substituto
    """
    print(aplicativo.replace(caracter, substituto))

substituindo(aplicativo, 'l', 'xx')
