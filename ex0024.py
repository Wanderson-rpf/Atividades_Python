"""
Escreva um programa que leia um numero inteiro e calcule a soma do todos
os divisores desse numero, com exceção dele proprio.
Ex: a soma dos divisores do numero 66 é 1 + 2 + 3 + 11 + 22 + 33 = 78
"""
print('-' * 50)
print('SOMA DOS DIVISORES DE UM NUMERO'.center(50))
print('-' * 50)

num = int(input('Digite um numero inteiro positivo: '))
divisor = 0
soma = 0

while divisor < num:
    divisor += 1
    resultado = num % divisor
    if resultado == 0:
        soma += divisor
print('-' * 50)
print(f'A soma dos divisores de {num} é {soma-num}')
print('-' * 50)
