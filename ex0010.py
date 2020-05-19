"""
Faça um programa que calcule e mostre a soma dos 50 primeiros numeros pares
"""
cont = 0
num_par = list()

while cont < 100:
    if cont % 2 == 0:
        num_par.append(cont)
    cont += 1
print(f'Os valores primeiros 50 valores pares são:\n{num_par}')
print(f'A soma dos 50 valores pares é {sum(num_par)}')
