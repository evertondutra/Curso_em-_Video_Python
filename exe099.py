"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu
programa tem que analisar todos os valores e dizer
qual deles é o maior.
"""
from time import sleep
def lin():
    print('='* 45)


def maior( *valores):
    cont = m = 0
    lin()
    print('Analizando valores passado...')
    for p,v in enumerate(valores):
        print(v, end=" ")
        sleep(0.5)
        if p == 0:
            m = v
        if v > m:
            m = v
        cont += 1
    print()
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m} .')



maior(2, 9, 4 , 5 , 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()