"""
Leia uma sequencia de números inteiros e determinar se eles são pares ou não.
Deverá ser informado o número de dados lidos e números de valores pares.
o processo termina quando for digitado 1000.
"""
lista_pares = list()
cont = 0

while True:
    numeros = int(input('Digite um numero inteiro ou "1000" para sair: '))
    if numeros == 1000:
        break
    cont += 1
    if numeros % 2 == 0:
        lista_pares.append(numeros)

print('-' * 40)
print('RESUMO'.center(40))
print('-' * 40)
print(f'- Foram informados {cont} números')
print(f'- Foram informados {len(lista_pares)} números pares')

