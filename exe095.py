"""
Aprimore o exercício 93 para que ele funcione
com vários jogadores, incluindo um sistema de
visualização de detalhes de aproveitamento de cada jogador.
"""
dic = {}
gols = []
jogadores = []
while True:
    dic['nome'] = input('Nome do jogador: ')
    part = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    for g in range(0, part):
        gols.append(int(input(f'Quantos gols na partida {g+1}: ')))
    dic['gols'] = gols[:]
    dic['total'] = sum(gols)
    jogadores.append(dic.copy())
    gols.clear()
    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r in 'NS':
            break
        else:
            print('ERRO! Digite S ou N.')
    if r == 'N':
        break
print('='*40)
print('Cod ',end='')
for i in dic.keys():
    print(f'{i:<15}',end='')
print()
print('='*40)
for k,v in enumerate(jogadores):
    print(f'{k:<4}',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*40)
while True:
    busca = int(input('Mostra dados de qual jogador?(999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for j, g in enumerate(jogadores[busca]["gols"]):
            print(f'No jogo {j+1} fez {g} gols.')
    print('='*40)
