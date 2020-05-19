"""
Faça um programa que leia um numero inteiro positivo N e imprima
os numeros naturais de 0 ate N em ordem crescente.
"""
n = int(input('Digite um numero positivo: '))

print('Contagem ate o numero digitado:', end=' ')
for i in range(0, n+1):
    print(f'{i}', end=' ')
