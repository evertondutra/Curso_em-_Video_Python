"""
Crie um módulo chamado moeda.py que tenha as funções
imcorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessa funções.
"""
from exe107 import moeda

p = float(input('digite o preço: RS '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando o preço em 10%, temo {moeda.aumentar(p, 10)}')
print(f'Diminuir o preço em 10%, temos {moeda.diminuir(p, 10)}')