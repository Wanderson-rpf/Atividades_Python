"""
Faça um programa que leia um numero inteiro positivo ímpar N
e imprima todos os numeros imapres de 1 ate N em ordem crescente.
"""
n = int(input('Digite um valor positivo ímpar para iniciar o programa: '))
while n % 2 == 0 or n < 0:
    print('Valor invalido.')
    n = int(input('Digite um valor positivo ímpar para iniciar o programa: '))
for i in range(1, n+1):
    if i % 2 != 0:
        print(f'{i}', end=' ')
