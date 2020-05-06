"""
Faça um programa que tenha uma função chamada área(),
Que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""
def area():
    a = float(input('LARGURA (m): '))
    b = float(input("COPRIMENTO (m): "))
    ar = a * b
    print(f'A área de um terreno {a} X {b} é de {ar}m²')


print('-'*40)
print(f'{"CONTROLE DE TERRENO":^40}')
print('-'*40)
area()

"""
OU
def area(a, b):
    ar = a * b
    print(f'A área de um terreno {a} X {b} é de {ar}m²')


print('-'*40)
print(f'{"CONTROLE DE TERRENO":^40}')
print('-'*40)
a = float(input('LARGURA (m): '))
b = float(input("COPRIMENTO (m): "))
area(a, b)
"""