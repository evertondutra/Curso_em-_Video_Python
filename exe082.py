"""
Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, creie duas lista extras que vão conter apenas os
 valores pares e ímpares digitado respectivamente. Ao final, mostre
 o conteúdo das três listas geradas.
"""
lista = []
pares = []
impares = []
while True:
    while True:
        n = input('Digite um número: ')
        if n.isnumeric():
            break
        else:
            print('\033[31mNúmero inválido\033[m.')
    n = int(n)
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    print(f'{"--":>20}')
    while True:
        r = input('\033[33mDeseja continuar?[S/N]\033[m ').strip().lower()[0]
        if r in 'sn':
            break
        else:
            print('\033[31mResposta inválida.\033[m')
    if r == 'n':
        break
print('\033[36m==\033[m'*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
