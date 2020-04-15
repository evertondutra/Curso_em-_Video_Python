'''n = float(input('Informe um valor: '))
print(f'O valor digitado po {n} e a sua porção inteira é {int(n)}')
'''
import math
n = float(input('Informe um valor: '))
print(f'O vloar digitado foi {n} e a sua porção inteira é {math.trunc(n)}')
'''
Ou 
from math import trunc
n = float(input('Informe um valor: '))
print(f'O vloar digitado foi {n} e a sua porção inteira é {trunc(n)}')
'''
