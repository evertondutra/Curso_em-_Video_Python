"""
Crie um programa que possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número ja exista la dentro,
ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""
val = []
p = 0
while True:
    while True:
        n = input('Digite um valor: ')
        if n.isnumeric() == True:
            break
        print('Número não digitado.')
    n = int(n)
    if n not in val:
        val.append(n)
        print('Adicionado com sucesso...')
    else:
        print('Valor Duplicado! Náo será adicionado.')
    while True:
        resp = input('Deseja continuar?[S/N] ').strip().upper()
        if resp in 'NS':
            break
        print('Resposta inválida.')
    if resp == 'N':
        break
print('\033[31m=\033[m'*32)
print(f'Os valores digitados foram        {val}.')
val.sort()
print(f'Os valores em ordem crescente são {val}.')
