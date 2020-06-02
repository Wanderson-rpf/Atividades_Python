"""
Crie um programa que faça o computador jogar jokenpô com vc.
"""
from random import randint

print('=' * 50)
print('JOGO JOKENPÔ'.center(50))
print('=' * 50)

jogadas = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print("""SUAS OPÇÕES:
[0] - Pedra
[1] - Papel
[2] - Tesoura""")
jogador = int(input('Digite sua jogada (0, 1 ou 2): '))
print('=' * 50)

print('=' * 50)
print('-= RESULTADO =-'.center(50))
print('=' * 50)

if computador == 0:
    if jogador == 0:
        print('Jogo empatou!!!')
    elif jogador == 1:
        print('PARABÉNS !!! Você ganhou.')
    elif jogador == 2:
        print('Que pena você perdeu.')
    else:
        print('Jogada invalida.')

elif computador == 1:
    if jogador == 0:
        print('Que pena você perdeu.')
    elif jogador == 1:
        print('Jogo empatou!!!')
    elif jogador == 2:
        print('PARABÉNS !!! Você ganhou.')
    else:
        print('Jogada invalida.')

elif computador == 2:
    if jogador == 0:
        print('PARABÉNS !!! Você ganhou.')
    elif jogador == 1:
        print('Que pena você perdeu.')
    elif jogador == 2:
        print('Jogo empatou!!!')
    else:
        print('Jogada invalida.')


print(f'JogadA do computador: {jogadas[computador]}')
print(f'Sua jogada: {jogadas[jogador]}')
