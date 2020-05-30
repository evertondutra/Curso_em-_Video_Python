"""
Faça um programa que tenha uma função chamada ficha(), que receba
dois parâmetros opcionais: o nome do jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente.
"""

def ficha(jog='Desconhecido', gols=0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')



n = input('Nome do jogador: ')
g = input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

