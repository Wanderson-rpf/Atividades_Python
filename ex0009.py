"""
Faça um programa que leia um numero inteiro N e depois imprima os N primeiros numeros
naturais impares
"""
print('-' * 50)
print("Gerador de números ímpares positivos".center(50))
print('-' * 50)

n = int(input("Digite o valor para mostrar a quantidade em números impares: "))
i = 0
impar = 1

print(f'- O valor informado foi {n}\n- Os números impares são: ', end='')
while i < n:
    print(f'{impar}', end=' ')
    i = i + 1
    impar += 2
