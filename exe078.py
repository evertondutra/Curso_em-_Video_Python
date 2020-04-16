"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valore digitado e suas
respectivas posições na lista.
"""
val = []
maior = 0
for c in range(0,5):
    val.append(int(input(f'Digite o {c+1}º número: ')))
    if c == 0:
        maior = menor = val[c]
    elif val[c] > maior:
        maior = val[c]
    elif val[c] < menor:
        menor = val[c]
print('='*20)
print(f'Você digitou os valores {val}.')
print(f'O maior valor digitado foi {maior} nas posições ',end='')
for p, v in enumerate(val):
    if v >= maior:
        print(f'{p + 1}',end="...")
print(f'\nO menor valor digitado foi {menor} nas posições ',end='')
for p, v in enumerate(val):
    if v <= menor:
        print(f'{p + 1}',end='...')