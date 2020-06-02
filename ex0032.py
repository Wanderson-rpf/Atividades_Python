"""
Mostrar que tipo de triangulo será formado.
- equilátero: todos os lados iguais
- Isosceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
print('=' * 60)
print('VERIFICANDO TIPO DO TRIANGULO'.center(60))
print('=' * 60)

r1 = float(input('Informe o comprimento da 1° reta: '))
r2 = float(input('Informe o comprimento da 2° reta: '))
r3 = float(input('Informe o comprimento da 3° reta: '))
print('=' * 60)

if r1 == r2 and r2 == r3:
    print('Todos os lados do triangulo são iguais, ele é equilátero')
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('Dois lados do triangulo são iguais, ele é isosceles.')
else:
    print('Todos os lados do triangulo são diferentes, ele é escaleno.')
print('=' * 60)
