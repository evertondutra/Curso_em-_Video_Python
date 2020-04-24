"""
Faça um programa que leia nome e média de
um aluno, guardando também a situação em
um dicionário. No final mostre o conteúdo
de estrutura na tela.
"""
aluno = dict()

aluno['nome'] = input('Nome: ')
aluno['média'] = float(input(f'Média do aluno {aluno["nome"]}: '))
print('='*30)
if aluno["média"] < 5:
    aluno['situação'] = 'Reprovado'
elif aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')
