"""
Desenvolva um programa que leia o comprimento de tres retas e dica
ao usuário se elas podem ou não formar um triangulo.
"""
print('=' * 50)
print('VERIFICAÇÃO DE RETA PARA TRIANGULO'.center(50))
print('=' * 50)

r1 = float(input('Informe o comprimento da 1° reta: '))
r2 = float(input('Informe o comprimento da 2° reta: '))
r3 = float(input('Informe o comprimento da 3° reta: '))
print('=' * 50)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('-> As retas formam um triangulo')
else:
    print('-> As retas não formam um triangulo.')
