# Desenvolva um programa que funcione como uma calculadora simples utilizando funções.

# O sistema deverá possuir um menu com as opções:

# 1 - Soma
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão
# 5 - Sair
# Requisitos:

# Cada operação deve ser realizada por uma função diferente
# O programa deverá permanecer em execução até que o usuário escolha “Sair”
# Validar divisão por zero
# Exibir mensagens de erro quando necessário

print('===== CALCULADORA =====')

# Função de soma
def soma(n1, n2):
    return n1 + n2

# Função de subtração
def subtracao(n1, n2):
    return n1 - n2

# Função de multiplicação
def multiplicacao(n1, n2):
    return n1 * n2

# Função de divisão
def divisao(n1, n2):

    if n2 == 0:
        return 'Erro: divisão por zero!'
    
    return n1 / n2


# Loop principal
while True:

    print('\n===== MENU =====')

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')

    opcao = input('Escolha uma opção: ')

    # Sair do programa
    if opcao == '5':
        print('Encerrando calculadora...')
        break

    # Validando opção
    if opcao not in ['1', '2', '3', '4']:
        print('Opção inválida!')
        continue

    # Entrada de números
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    # Soma
    if opcao == '1':
        resultado = soma(numero1, numero2)
        print('Resultado:', resultado)

    # Subtração
    elif opcao == '2':
        resultado = subtracao(numero1, numero2)
        print('Resultado:', resultado)

    # Multiplicação
    elif opcao == '3':
        resultado = multiplicacao(numero1, numero2)
        print('Resultado:', resultado)

    # Divisão
    elif opcao == '4':
        resultado = divisao(numero1, numero2)
        print('Resultado:', resultado)