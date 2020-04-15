"""
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final mostre:
A) Quantas vezes o número 9 aparece.
B) Em que posição foi digitado o primeiro  valor 3.
C) Quais foram os números pares.
"""
num = (int(input('Digite o primeiro número: ')),
       int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o quarto número: ')))
print(f'O número 9 apareceu {num.count(9)} vezes.')
print(f'O número 3 foi digitado na posição {num.index(3) + 1}' if 3 in num else 'Não foi digitado nenhum número 3')
print(f'Os números pares são ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
