"""
Atividade 01:
Faça um programa que determine e mostre os cinco primeiros múltiplos de 3,
considerando numeros maiores que 0.
"""
num_list = []
for num in range(3, 100, 3):
    if num % 3 == 0 and num <= 15:
        num_list.append(num)
print(f'Os cinco primeiros numeros multiplos de 3 são: {num_list}')
