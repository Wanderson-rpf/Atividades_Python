"""
Faca um programa que leia 10 inteiros e imprima sua media
"""
soma = 0

for i in range(1, 11):
    valor = int(input(f'Digite o {i}° valor: '))
    soma += valor
media = soma / 10
print(f'A media dos valores é {media}')
