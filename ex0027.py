"""
Crie um algoritmo que leia um numero e mostre o seu dobro
trilo e raiz quadrada.
"""
print('=' * 50)
num = float(input('Digite um numero: '))
print('=' * 50)
print('RESUMO'.center(50))
print('=' * 50)
print(f'- O dobro do numero é \t{num * 2}')
print(f'- O triplo do numero é \t{num * 3}')
print(f'- A raiz quadrada é \t{num**(1/2):.1f}')
print('=' * 50)
