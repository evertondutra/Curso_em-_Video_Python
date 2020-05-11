"""
Faça um proggrama que tenha uma lista chamada números e duas
funções chamadas sorteia() e somo(). A primeira função ira sortear
5 números e vai colocá-las dentro de uma listae a segunda função irá
 mostras a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista:',end=' ')
    for c in range(0, 5):
        sleep(0.5)
        lista.append(randint(1, 10))
        print(lista[c],end=' ')
    print('PRONTO!')

def somapar(lista):
    som = 0
    for c in lista:
        if c % 2 == 0:
            som += c
    print(f'Somando os valores pares de {lista}, temos {som}')

numeros = []
sorteia(numeros)
somapar(numeros)

