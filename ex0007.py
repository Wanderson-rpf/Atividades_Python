"""
Faca um programa que leia 10 inteiros positivos, ignorando os negativos,
e imprima sua media
"""
c = 0
soma = 0

print('-' * 45)
print('Entrada de 10 valores'.center(45))
while True:
    valor = int(input(f'Digite o valor: '))
    if valor < 0:
        print('Valor negativo, o mesmo não será adicionado a soma.')
    else:
        soma += valor
        media = valor / 10
        c += 1
    if c == 10:
        break
print('-' * 45)
print(f'- A soma dos valores positivos é {soma}\n- A media da somas dos valores positivos é {media}')
