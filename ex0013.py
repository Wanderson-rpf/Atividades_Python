"""
Faça um programa que leia um numero inteiro positivo par N
e imprima todos os numeros pares de 0 ate N em ordem crescente.
"""
n = int(input('Digite um numero positivo PAR para iniciar o programa: '))
while n % 2 != 0 or n < 0:
    print('Valor invalido!')
    n = int(input('Digite um numero positivo PAR para iniciar o programa: '))

for i in range(0, n+1):
    if i % 2 == 0:
        print(f'{i}', end=' ')
