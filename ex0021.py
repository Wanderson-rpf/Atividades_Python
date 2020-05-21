"""
Faça um programa que receba dois números. Calcule e mostre:
- A soma dos números pares deste intervalo de números, incluindo os números digitados
- A multiplicação dos números ímpares deste intervalo, incluindo os digitados.
"""
n1 = int(input('Informe o número inicial: '))
n2 = int(input('Informe o numero final: '))
soma_par = 0
mult_impar = 1

for i in range(n1, n2+1):
    if i % 2 == 0:
        soma_par += i
    else:
        mult_impar *= i

print(f'- A soma dos números pares no intervalo de {n1} ate {n2} é {soma_par}')
print(f'- A multiplicação do números ímpares no intervalos de {n1} ate {n2} é {mult_impar}')
