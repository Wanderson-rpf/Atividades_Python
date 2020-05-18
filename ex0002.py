"""
Escreva um programa que escreva na tela, de 1 ate 100, de 1 em 1, 3 vezes.
A primeira vez deve usar a estrutura de repetição FOR, a segunda WHILE
e a terceira DO WHILE.
"""

print('-= Utilizando FOR =-')
for i in range(1, 101):
    print(i)

print('-= Utilizando WHILE =-')
cont = 1
while cont != 101:
    print(cont)
    cont += 1

print('-= Outra forma de WHILE = -')
c = 0
while True:
    c += 1
    print(c)
    if c == 100:
        break
