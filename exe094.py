"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
A) Quantas pessoa cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
"""
pessoa = {}
todos = []
soma = 0
print('*'*30)
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    while True:
        pessoa['sexo'] = input('Sexo [F/M]: ').strip()[0]
        if pessoa['sexo'] in 'MmFf':
            break
        else:
            print('ERRO! Por favor, digite M ou F.')
    todos.append(pessoa.copy())
    soma += pessoa['idade']
    while True:
        r = input('Deseja continuar [S/N]? ').strip()[0]
        if r in 'SsNn':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if r in 'Nn':
        break
print('='*30)
print(f'A) Temos {len(todos)} pessoas cadastradas')
print((f'B) A média de idade é {soma/len(todos):.1f} anos'))
print('C) As mulheres cadastradas foram ',end=' ')
for n in todos:
    if n['sexo'] in 'Ff':
        print(n['nome'],end=' ')
print()
print('D) A lista das pessoas acima da média:')
for d in todos:
    if (d['idade']) > soma/len(todos):
        print('     ')
        for k,v in pessoa.items():
            print(f'{k} = {v}: ', end='')
        print()
print(f'{"<<< ENCERRANDO >>>":^30}')
