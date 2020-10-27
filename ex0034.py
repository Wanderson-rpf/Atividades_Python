"""
Faça um programa que leia 5 valores numericos e guarde em uma lista.
no final mostre qual foi o maior e o menor valor digitado  as suas respectivas posições.

"""
lista_num = []

for i in range(1, 6):
    num = int(input('Digite um valor inteiro: '))
    lista_num.append(num)
print('-' * 50)
print(f'A lista de números foi: {lista_num}')
print(f'O maior valor digitado foi {max(lista_num)} e esta na {lista_num.index(max(lista_num)) + 1}° posição.')
print(f'O menor valor digitado foi {min(lista_num)} e esta na {lista_num.index(min(lista_num)) + 1}° posição.')
print('-' * 50)

