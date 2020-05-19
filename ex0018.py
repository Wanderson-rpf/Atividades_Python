"""
Escreva um algoritmo que leia certa quantidade de números e imprima
o maior deles e quantas vezes o maior números foi lido. A quantidade
de números a serem lidos devem ser fornecida pelo usuário.
"""
from random import randint

num = list()
qtd_num = int(input('Informe a quantidade de números o programa vai ler: '))

for i in range(qtd_num):
    n = randint(1, 100)
    num.append(n)

print('-' * 40)
print('RESUMO'.center(40))
print('-' * 40)

print(f'- Os números lidos foram: {num}')
print(f'- O maior número lido foi: {max(num)}')
print(f'- O maior Valor foi repetido: {num.count(max(num))} vezes')
