# Uma loja deseja automatizar o cálculo de descontos em compras.

# Crie um programa que:

# Solicite o valor total da compra
# Solicite a quantidade de parcelas
# Regras:

# Compras acima de R$ 500 recebem 10% de desconto
# Compras parceladas em mais de 5 vezes possuem acréscimo de 8%
# O programa deve exibir:

# Valor original
# Valor final
# Valor de cada parcela

print('===== LOJA DE DESCONTOS =====')

# Entrada de dados
valor_compra = float(input('Digite o valor da compra: R$ '))
parcelas = int(input('Digite a quantidade de parcelas: '))

# Guardando o valor original
valor_original = valor_compra

# Desconto
if valor_compra > 500:
    desconto = valor_compra * 0.10
    valor_compra = valor_compra - desconto
    print('Desconto de 10% aplicado!')
else:
    print('Sem desconto.')

# Acréscimo
if parcelas > 5:
    acrescimo = valor_compra * 0.08
    valor_compra = valor_compra + acrescimo
    print('Acréscimo de 8% aplicado no parcelamento!')
else:
    print('Sem acréscimo.')

# Valor das parcelas
valor_parcela = valor_compra / parcelas

# Saída de dados
print('\n===== RESUMO DA COMPRA =====')

print(f'Valor original: R$ {valor_original:.2f}')
print(f'Valor final: R$ {valor_compra:.2f}')
print(f'Valor de cada parcela: R$ {valor_parcela:.2f}')