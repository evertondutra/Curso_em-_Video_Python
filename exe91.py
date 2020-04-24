"""
Crie um pograma onde 4 jogadores joguem dados e tenham
resultados aleatórios. Guarde esses resultados em um dicionário
No final, coloque esse dicionário em ordem, sabendo que o
vencedor tirou o maior número do dado.
"""
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = []
print(f'{"VALORES SORTEADOS:":^30}')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # coloca o dicionário em ordem pela posição indicada.
print('='*30)
print(f'{"=== RANKING DOS JOGADORES ===":^30}')

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} tirou {v[1]}')
    sleep(1)
