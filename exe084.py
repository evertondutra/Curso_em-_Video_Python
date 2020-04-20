"""
Fça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
todos = []
lista = []
maior = menor = 0
print('='*30)
print(f'{"CADASTRO DE PESSOAS":^30}')
print('='*30)
while True:
    lista.append(input('Nome: '))
    lista.append(float(input('Peso: ')))
    if len(todos)== 0:
        maior = menor = lista[1]
    else:
        if lista[1]>maior:
            maior = lista[1]
        if lista[1]<menor:
            menor=lista[1]
    todos.append(lista[:])
    lista.clear()
    resp = input('Deseja continuar?[S/N] ').strip().lower()[0]
    if resp == 'n':
        break
    else:
        print('-'*30)
print('='*30)
print(f'O total de pessoas cadastradas são {len(todos)}')
print(f'O maior peso foi {maior:.2f}Kg. Peso de ',end='')
for p in todos:
    if p[1]==maior:
        print(p[0],end=' ')
print(f'\nO peso mais leve foi de {menor:.2f}kg. Peso de ',end='')
for p in todos:
    if p[1]==menor:
        print(p[0],end=' ' )
