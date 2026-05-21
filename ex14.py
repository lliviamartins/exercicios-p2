# Crie um programa que simule um sistema simples de login.

# O sistema deverá:

# Solicitar usuário e senha
# Permitir no máximo 3 tentativas
# Exibir:
# “Acesso permitido” caso os dados estejam corretos
# “Usuário bloqueado” após 3 tentativas inválidas
# Considere:

# usuario_correto = "admin"
# senha_correta = "1234"

print('===== SISTEMA DE LOGIN =====')

# Dados corretos
usuario_correto = 'admin'
senha_correta = '1234'

# Número de tentativas
tentativas = 0

# Loop
while tentativas < 3:

    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')

    # Verificação
    if usuario == usuario_correto and senha == senha_correta:
        print('Acesso permitido!')
        break

    else:
        tentativas += 1
        print('Usuário ou senha incorretos.')

# Bloqueio após 3 erros
if tentativas == 3:
    print('Usuário bloqueado!')