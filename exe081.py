"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    while True:
        n = input('Digite um valor: ')
        if n.isnumeric():
            n = int(n)
            lista.append(n)
            break
        else:
            print('\033[31mNúmero inválido\033[m')
    while True:
        resp = input('Quer continuar?[S/N] ').strip().upper()
        if resp in 'SN':
            break
        else:
            print('\033[31mResposta inválida\033[m.')
    if resp == 'N':
        break
print('\033[33m==\033[m'*20)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores decrescente são {lista}')
print('O valor 5 faz parte da lista' if 5 in lista else print('O valor 5 não foi encontrado na lista'))

