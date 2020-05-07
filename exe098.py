"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa
tem que realizar três contagens através da função criada:
A) De 1 à 10, de 1 em 1
B) De 10 até 0,de 2 em 2
C) Uma contagem personalizada.
"""
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
            sleep(0.5)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=" ")
            cont -= p
            sleep(0.5)
        print('FIM!')

def lin():
    print("="*30)

lin()
contador(1,10,1)
lin()
contador(10, 0, 2)
lin()
print("Agora é a sua vez de personalizar a contagem!")
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo: '))
lin()
contador(ini, fim, pas)