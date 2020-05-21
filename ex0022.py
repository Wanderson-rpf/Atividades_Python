"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
uma sequencia arbitrária de notas (validas no intervalo de 10 a 20) e que mostre
na tela, como resultado, a correspondente media aritmética.
O numero de notas com que o aluno pretenda efetuar o calculo não será fornecido ao
programa, o qual terminará quando for introduzido um valor que não seja válido como
nota de aprovação.
"""
print('-' * 41)
print('CALCULO DE MÉDIA DE ALUNO'.center(41))
print('-' * 41)

print('\033[31mAVISO:\nDigite uma nota fora intervalo de 10 a 20\npara sair do programa.\033[m')
print('-' * 41)

cont = 0
soma_nota = 0
media = 0.0
while True:
    nota = float(input('Informe a nota do aluno: '))
    if nota < 10 or nota > 20:
        print('-' * 41)
        print('A ultima nota digitada esta fora do \nintervalo de 10 ate 20. Programa encerrado.')
        print('-' * 41)
        break
    cont += 1
    soma_nota += nota
    media = soma_nota / cont

print(f'- A media do aluno baseado nas notas informadas é: {media:.1f}')
