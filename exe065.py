"""
Crie um programa que leia vários números pelo teclado. No final, mostre a média, o maior e o menor
número digitado, e pergunte se o uspuario deseja continuar.
"""
cont = maior = menor = soma = 0
resp = 'S'
while resp != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    resp = input('Deseja continuar?[S/N]:').strip().upper()[0]
print(f'A média entre os {cont} números digitados  é {soma / cont:.1f}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
