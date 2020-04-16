"""
Crie um programa onde o usuário possa digitar 5 valores númericos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar
sort()). No final, mostre a lista ordenada na tela.
"""
lista = []
for c in range(0, 5):
    n = int(input(f'Digite o {c+1}º número. '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('='*40)
print(f'os valores digitados em ordem foram {lista}. ')