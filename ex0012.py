"""
Faça um programa que leia um numero inteiro positivo N e imprima
todos os números naturais de 0 ate N em ordem decrescente
"""
n = int(input('Digite um numero inteiro positivo: '))
print('Contagem de numeros ate o numero digitado, \nem ordem decrescente: ', end=' ')
for i in range(n, 0, -1):
    print(f'{i}', end=' ')
