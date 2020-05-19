"""
Faça um programa que leia um numero inteiro positivo ímpar N
e imprima todos os numeros impares de 1 ate N em ordem decrescente.
"""
n = int(input('Digiete um valor positivo impar para iniciar o programa: '))
while n % 2 == 0 or n < 0:
    print('Valor invalido.')
    n = int(input('Digiete um valor positivo impar para iniciar o programa: '))
for i in range(n, 0, -1):
    print(f'{i}', end=' ')
