"""
Faça um programa que leia um numero inteiro positivo par N
e imprima todos os numeros pares de 0 ate N em ordem decrescente.
"""
print('-'*60)
n = int(input('Digite um numero positivo PAR para iniciar o programa: '))
print('-'*60)
print('Valores pares em ordem decrescente, ate o valor informado.')
while n % 2 != 0 or n < 0:
    print('Valor invalido.')
    n = int(input('Digite um numero positivo PAR para iniciar o programa: '))
for i in range(n, 0-1, -1):
    print(f'{i}', end=' ')
