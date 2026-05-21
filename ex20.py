# Uma empresa deseja controlar o estoque de produtos.

# Desenvolva um programa utilizando listas e funções que permita:

# Menu:
# 1 - Cadastrar produto
# 2 - Listar produtos
# 3 - Buscar produto
# 4 - Remover produto
# 5 - Encerrar sistema
# Cada produto deverá possuir:

# Nome
# Quantidade
# Preço
# O sistema deverá:

# Permitir cadastro de vários produtos
# Exibir todos os produtos cadastrados
# Buscar produto pelo nome
# Remover produto da lista
# Exibir o valor total do estoque:
# quantidade × preço
# Utilize:

# Funções
# Estruturas de repetição
# Estruturas condicionais
# Listas e dicionários

print('===== SISTEMA DE ESTOQUE =====')

# Lista de produtos
estoque = []

# Função para cadastrar produto
def cadastrar_produto():

    nome = input('Digite o nome do produto: ').title()
    quantidade = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preço: R$ '))

    produto = {
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }

    estoque.append(produto)

    print('Produto cadastrado com sucesso!')


# Função para listar produtos
def listar_produtos():

    if len(estoque) == 0:
        print('Nenhum produto cadastrado.')
        return

    valor_total = 0

    print('\n===== PRODUTOS CADASTRADOS =====')

    for produto in estoque:

        total_produto = produto['quantidade'] * produto['preco']

        valor_total += total_produto

        print(f'''
Nome: {produto['nome']}
Quantidade: {produto['quantidade']}
Preço: R$ {produto['preco']:.2f}
Valor em estoque: R$ {total_produto:.2f}
''')

    print(f'Valor total do estoque: R$ {valor_total:.2f}')


# Função para buscar produto
def buscar_produto():

    busca = input('Digite o nome do produto: ').title()

    encontrado = False

    for produto in estoque:

        if produto['nome'] == busca:

            print('\n===== PRODUTO ENCONTRADO =====')

            print(f'''
Nome: {produto['nome']}
Quantidade: {produto['quantidade']}
Preço: R$ {produto['preco']:.2f}
''')

            encontrado = True

    if encontrado == False:
        print('Produto não encontrado.')


# Função para remover produto
def remover_produto():

    nome = input('Digite o nome do produto que deseja remover: ').title()

    for produto in estoque:

        if produto['nome'] == nome:

            estoque.remove(produto)

            print('Produto removido com sucesso!')
            return

    print('Produto não encontrado.')


# Sistema principal
while True:

    print('''
===== MENU =====

1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto
4 - Remover produto
5 - Encerrar sistema
''')

    opcao = input('Escolha uma opção: ')

    # Cadastro
    if opcao == '1':
        cadastrar_produto()

    # Listagem
    elif opcao == '2':
        listar_produtos()

    # Busca
    elif opcao == '3':
        buscar_produto()

    # Remoção
    elif opcao == '4':
        remover_produto()

    # Encerrar
    elif opcao == '5':
        print('Sistema encerrado.')
        break

    # Opção inválida
    else:
        print('Opção inválida!')