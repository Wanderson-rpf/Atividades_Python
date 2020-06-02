"""
Crie um programa que leia o nome de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao total (sem considerar espaços)
Quantas letras tem o primeiro nome
"""
print('=' * 40)
nome = str(input('Informe o nome e sobre nome: ')).strip()
print('=' * 40)

print('RESUMO DE INFORMAÇÕES DO NOME'.center(40))
print('=' * 40)

print(f'- Nome com letras maiúsculas: {nome.upper()}')
print(f'- Nome com letras minúsculas: {nome.lower()}')
print(f'- O nome possui {len(nome) - nome.count(" ")} letras.')
separar = nome.split()
print(f'- O primeiro nome tem {len(separar[0])}')

