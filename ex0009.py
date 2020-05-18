"""
Faça um programa que leia um numero inteiro N e depois imprima os N primeiros numeros
naturais impares
"""
print("Gerador do n primeiros números ímpares positivos\n")
# leia o valor de n
n = int(input("Digite o valor de n: "))

i = 0  # contador de ímpares impressos

ímpar = 1  # primeiro número ímpar

while i < n:  # imprima os n primeiros impares, um por linha
    print(ímpar)  # imprima o próximo número ímpar
    i = i + 1  # incremente o contador
    ímpar = ímpar + 2  # determine o próximo ímpar
