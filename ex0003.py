"""
Faça um algoritmo utilizando o comando WHILE que mostre uma contagem regressiva
na tela, iniciando em 10 e terminando em 0. Mostrar mensagem "FIM!" após a contagem.
"""
from time import sleep

cont = 11
while cont != 0:
    cont -= 1
    print(f'{cont}', end=' - ')
    sleep(0.5)
print('Fim.')
