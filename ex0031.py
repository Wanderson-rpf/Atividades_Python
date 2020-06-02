"""
Faça um programa que mostre a tabuada de varios numeros, um de cada vez,
para cada valor digitado pelo usuário.
O programa sera interrompido quando o numero solicitado for negativo.
"""
print('=' * 50)
print('TABUADA'.center(50))
print('=' * 50)

while True:
    print('Digite um numero negativo para sair do programa.')
    print('=' * 50)
    valor = int(input('Informe um valor para fazer a tabuada: '))
    if valor < 0:
        break
    for i in range(1, 10):
        print(f'{i} x {valor} = {valor * i}')
