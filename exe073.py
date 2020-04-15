"""
Crie uma tupla preenchida com os 20 primeiros colocado da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os cincos primeiros colocados
B) Os 4 últimos colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição da tabela esta o time da Chapecoense.
"""
pos = 0
tab = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia',
         'Vasco', 'Atlético', 'Fluminense', 'Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí' )
print(f'Os cincos primeiros são: {tab[0:5]}')
'''print('Os cincos primeiros times são: ',end=' ')
for c in range(0,5):
    print(tab[c], end=', ')'''
print('\033[31m=--=\033[m'*10)
#ult = tab[-4:]
print(f'\nOs quatro últimos são: {tab[-4:]}')
print('\033[31m=--=\033[m'*10)
print(f'Os times em ordem alfabética é {sorted(tab)}')
print('\033[31m=--=\033[m'*10)
'''for c in tab:
    pos +=1
    if c == 'Chapecoense':
        col = pos+1
print(f'O time da Chapecoense está na {col}ª posição da tabela do brasileirão.')'''
print(f'O time da Chapecoense está na posição {tab.index("Chapecoense")+1}')
print('\033[31m=--=\033[m'*10)
