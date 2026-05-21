# Desenvolva um programa que solicite ao usuário 10 números inteiros e armazene-os em uma lista.

# Ao final, o sistema deverá:

# Exibir todos os números digitados
# Informar:
# Quantos números são pares
# Quantos números são ímpares
# O maior número
# O menor número
# A média geral
# Exibir a lista em ordem crescente

print('===== SISTEMA DE NÚMEROS =====')

# Lista para armazenar os números
numeros = []

# Repetição para pedir os 10 números
for contador in range(1, 11):

    numero = int(input(f'Digite o {contador}º número: '))
    numeros.append(numero)

# Contadores
pares = 0
impares = 0

# Verificando pares e ímpares
for numero in numeros:

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Maior e menor número
maior = max(numeros)
menor = min(numeros)

# Média
media = sum(numeros) / len(numeros)

# Ordenando a lista
numeros.sort()

# Resultados
print('\n===== RESULTADOS =====')

print('Números digitados:', numeros)

print('Quantidade de pares:', pares)
print('Quantidade de ímpares:', impares)

print('Maior número:', maior)
print('Menor número:', menor)

print(f'Média geral: {media:.2f}')

print('Lista em ordem crescente:', numeros)