'''
Escreva um programa que leia dois número inteiros
e compare-os mostrando na tela uma mensagem :
-O primeiro valor é maior.
- O segundo valor é maior.
- O dois valores são iguais.
'''
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número:'))
if n1 == n2:
    print('Os dois valores são iguais.')
elif n1 > n2:
    print('O primeiro valor é maior.')
else:
    print('O segundo valor é maior.')
