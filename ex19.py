# Crie um programa que solicite uma frase ao usuário e realize as seguintes operações:

# Quantidade total de caracteres
# Quantidade de vogais
# Quantidade de espaços
# Quantidade de palavras
# Exibir a frase em letras maiúsculas
# Exibir a frase invertida
# Exemplo:

# texto[::-1]

print('===== ANALISADOR DE FRASES =====')

# Entrada de dados
texto = input('Digite uma frase: ')

# Quantidade de caracteres
quantidade_caracteres = len(texto)

# Contadores
vogais = 0
espacos = 0

# Verificando caracteres
for letra in texto.lower():

    # Contando vogais
    if letra in 'aeiou':
        vogais += 1

    # Contando espaços
    if letra == ' ':
        espacos += 1

# Quantidade de palavras
palavras = len(texto.split())

# Frase maiúscula
maiuscula = texto.upper()

# Frase invertida
invertida = texto[::-1]

# Resultados
print('\n===== RESULTADOS =====')

print('Quantidade de caracteres:', quantidade_caracteres)

print('Quantidade de vogais:', vogais)

print('Quantidade de espaços:', espacos)

print('Quantidade de palavras:', palavras)

print('Frase em maiúsculas:', maiuscula)

print('Frase invertida:', invertida)