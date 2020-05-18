"""
Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""
print('-' * 40)
print('Soma de valores'.center(40))
soma = 0
for i in range(1, 11):
    valores = int(input(f'Digite {i}° valor: '))
    soma += valores
print(f'A soma dos valores é {soma}.')
print('-' * 40)
