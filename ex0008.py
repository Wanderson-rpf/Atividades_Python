"""
Escreva um programa que leia 10 números e escreva o menor valor e o maior valor lido
"""
# Utilizando lista e comandos referentes a lista.
numeros = list()

for c in range(1, 11):
    valor = int(input(f'Digite o {c}° valor: '))
    numeros.append(valor)
print(f'- O maior valor dititado foi {max(numeros)}\n- o menor valor digitado foi {min(numeros)}')

