"""
Faça um programa que ajude a um jogador da Mega Sena a criar
palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.
"""
from random import randint
from time import sleep
jogo = []
print('-'*40)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*40)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-='*3,f'SORTEANDO {n} JOGOS', '=-'*3)
for c in range(1,n+1):
    for num in range(0,6):
        sort = (randint(1,60))
        while sort in jogo:
            sort = randint(1,60)
        jogo.append(sort)
    jogo.sort()
    print(f'Jogo {c}: {jogo}')
    jogo.clear()
    sleep(1)
print(f'{"-=-=-=-=-= BOA SORTE =-=-=-=-=-":^30}')
