"""
Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima
na saída cada um dos algarismos que compõem o número.
"""
print('=' * 70)
num = int(input('Digite um numero inteiro que esteja entre 100 e 999: '))
print('=' * 70)

while num < 100 or num > 999:  # Verificando a entrada do usuário e solicitando entrada válida.
    print('ATENÇÃO! O numero digitado não esta no intervalo de 100 e 999.\nTente novamente.')
    print('=' * 70)
    num = int(input('Digite um numero inteiro que esteja entre 100 e 999: '))
    print('=' * 70)

# Calculo matemático
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10

print('RESULTADO'.center(70))
print('=' * 70)

print(f'O numero digitado foi {num}')
print(f'- Unidade: \t{u}')  # O "\t" é para alinha de forma tabular
print(f'- Dezena: \t{d}')
print(f'- Centena: \t{c}')
print('=' * 70)
