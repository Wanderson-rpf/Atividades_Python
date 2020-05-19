"""
Faça um programa que leia um números inteiro positivo N
e calcule a soma dos N primeiros números naturais.
"""
soma = 0
n = int(input('Digite um numero positivo para iniciar: '))
while n < 0:
    print('Valor invalido.')
    n = int(input('Digite um numero positivo para iniciar: '))

print('- A seguencia de números é: ', end='')
for i in range(0, n+1):
    soma += i
    print(f'{i}', end=' ')
print()
print(f'- A soma dos números é : {soma}')
