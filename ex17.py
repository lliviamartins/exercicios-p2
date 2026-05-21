# Uma escola deseja automatizar o controle de notas dos alunos.

# Crie um programa que:

# Solicite o nome de 5 alunos
# Solicite 3 notas para cada aluno
# Utilize uma função para calcular a média
# O programa deverá exibir:

# Nome do aluno
# Média final
# Situação:
# Aprovado (média ≥ 7)
# Recuperação (5 ≤ média < 7)
# Reprovado (média < 5)
# Ao final, o sistema também deverá mostrar:

# Quantidade de aprovados
# Quantidade de recuperação
# Quantidade de reprovados
# Melhor média da turma
# Nome do aluno com maior média

print('===== SISTEMA ESCOLAR =====')

# Função para calcular média
def calcular_media(n1, n2, n3):

    media = (n1 + n2 + n3) / 3
    return media

# Contadores
aprovados = 0
recuperacao = 0
reprovados = 0

# Variáveis para melhor aluno
melhor_media = 0
melhor_aluno = ''

# Repetição para os 5 alunos
for contador in range(1, 6):

    print(f'\n===== ALUNO {contador} =====')

    nome = input('Digite o nome do aluno: ').title()

    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    # Chamando a função
    media = calcular_media(nota1, nota2, nota3)

    # Verificando situação
    if media >= 7:
        situacao = 'Aprovado'
        aprovados += 1

    elif media >= 5:
        situacao = 'Recuperação'
        recuperacao += 1

    else:
        situacao = 'Reprovado'
        reprovados += 1

    # Verificando melhor média
    if media > melhor_media:
        melhor_media = media
        melhor_aluno = nome

    # Exibindo resultado do aluno
    print('\n----- RESULTADO -----')

    print('Aluno:', nome)
    print(f'Média final: {media:.2f}')
    print('Situação:', situacao)

# Resultado final da turma
print('\n===== RESULTADO FINAL DA TURMA =====')

print('Quantidade de aprovados:', aprovados)
print('Quantidade de recuperação:', recuperacao)
print('Quantidade de reprovados:', reprovados)

print(f'Melhor média da turma: {melhor_media:.2f}')
print('Aluno com maior média:', melhor_aluno)
