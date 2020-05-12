"""
Crie um programa que tenha uma função fatorial() que receba dois
parâmetros: o primeiro que indique o número a calcular e o outro
chamado show, que será um valor lógico(opcional) indicando se será
mostrado ou não na tela o processo de calculo do fatorial
"""


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opcional) mostrar o cálculo
    :return: O valor do fatorial de um número num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

n = int(input('De qual número deseja ver o fatorial? '))
r = input('Deseja ver o calculo?[S/N] ')
if r in 'Nn':
    r = False
print(fatorial(n, r))
help(fatorial)