"""
Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitp em
cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feito durante o campeonato.
"""
dic = {}
gols = []
dic['nome'] = input('Nome do jogador: ')
part = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for g in range(0, part):
    gols.append(int(input(f'Quantos gols na partida {g}: ')))
dic['gols'] = gols[:]
dic['total'] = sum(gols)
print('='*30)
print(dic)
print('='*30)
for k,v in dic.items():
    print(f'O campo {k} tem o valor {v}.')
print('='*30)
print(f'O jogador {dic["nome"]} jogou {len(dic["gols"])} partidas.')
for p, g in enumerate(gols):
    print(f'=> Na partida {p}, fez {g} gols.')
print(f'Foi um total de {sum(gols)} gols.')