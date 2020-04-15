"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique
o menor e o maior que estao na tupla.
"""
from random import randint
sort = (randint(1, 10), randint(1, 10),
randint(1, 10),randint(1, 10),randint(1, 10))
print('Os valores sorteados foram: ',end='')
for n in sort:
    print(f'{n} ',end='')
print(f'\nO maior valor sorteado foi {max(sort)}')
print(f'O menor valor digitado foi {min(sort)}')



