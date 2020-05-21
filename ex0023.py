"""
Faça um algoritmo que leia um numero positivo e imprima seus divisores.
"""
print('-' * 50)
print('DIVISORES DE UM NUMERO'.center(50))
print('-' * 50)

num = int(input('Digite um numero inteiro positivo: '))  # Entrada de dados
print('-' * 50)

divisor = 0  # Variável que vai fazer a divisão do numero fornecido

# Cabeçalho de saída
print('RESULTADO'.center(50))
print(f'Os divisores de {num} são: ', end='')

while divisor < num:  # Enquanto divisor menor que numero de entrada
    divisor += 1  # Divisor recebe divisor + 1, para fazer o loop ate o final
    result = num % divisor  # resultado recebe o resto da divisão entre o numero e o divisor
    if result == 0:  # se o resultado for igual a "0"
        print(divisor, end=' ')  # imprime o divisor
print('-' * 50)

# http://www.matematicadidatica.com.br/Divisores.aspx
