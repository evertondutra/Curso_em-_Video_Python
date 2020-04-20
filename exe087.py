"""

"""
lista = [[0,0,0],[0,0,0],[0,0,0]]
soma = somac = maior = 0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c]=int(input(f'Digite um valor para [{l}, {c}]: '))
        if c == 2 :
            somac+=lista[l][c]
        if l == 1 and lista[l][c] > maior:
            maior = lista[l][c]
print('='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]',end='')
        if lista[l][c] % 2 ==0:
            soma+=lista[l][c]

    print()
print('='*30)
print(lista)

print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {somac}.')
print(f'O maior valor da segunda linha é {maior}.')