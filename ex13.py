# Desenvolva um programa que leia 10 números inteiros informados pelo usuário.

# Ao final, o sistema deverá exibir:

# Quantidade de números pares
# Quantidade de números ímpares
# Maior número digitado
# Menor número digitado
# Média dos valores
# Utilize estruturas de repetição.

print('===== LEITOR DE NÚMEROS =====')

# Variáveis
quantidade_pares = 0
quantidade_impares = 0
soma = 0

# Primeiro número
numero = int(input('Digite o 1º número: '))

maior = numero
menor = numero

# Verificando se o primeiro número é par ou ímpar
if numero % 2 == 0:
    quantidade_pares += 1
else:
    quantidade_impares += 1

soma += numero

# Repetição para os outros 9 números
for contador in range(2, 11):

    numero = int(input(f'Digite o {contador}º número: '))

    # Soma
    soma += numero

    # Verificar par ou ímpar
    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1

    # Verificar maior número
    if numero > maior:
        maior = numero

    # Verificar menor número
    if numero < menor:
        menor = numero

# Média
media = soma / 10

# Resultados
print('\n===== RESULTADOS =====')

print('Quantidade de pares:', quantidade_pares)
print('Quantidade de ímpares:', quantidade_impares)
print('Maior número:', maior)
print('Menor número:', menor)
print(f'Média dos valores: {media:.2f}')