"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua area e a quantidade de tinta necessária para pinta-la.
Sabendo que cada litro de tinta pinta uma area de 2m².
"""
print('=' * 50)
print('OBS: 1 litro de tinta pinta uma area de 2m².')
print('=' * 50)

larg = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
print('=' * 50)

area = alt * larg
tinta = area / 2

print('RESULTADO'.center(50))
print(f'A área da parede é {area}m²')
print(f'Serão necessários {tinta} litros de tinta.')
print('=' * 50)
