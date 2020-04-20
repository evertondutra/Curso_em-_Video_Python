"""
 Crie um programa onde o usuário possa digitar 7 valores numéricos
 e cadastre-os em uma lista única que mantenha separados os valores
 par e ímpares. No final,, mostre os valores par e ímpares
 em ordem crescente.
"""
lista = []
listap = []
listai = []
for c in range(7):
    while True:
        lista.append(input(f'Digite o {c+1}º valor: '))
        if lista[c].isnumeric():
            lista[c]=int(lista[c])
            break
        else:
            print('\033[31mNúmero inválido.\033[m')
            lista.pop()
for n in lista:
    if n%2==0:
        listap.append(n)
    else:
        listai.append(n)
listap.sort()
listai.sort()
print(f'Os valores pares digitados foram: {listap}')
print(f'Os valores ímpares digitados foram: {listai}')

"""
OU

num[[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Informe o {1}º valor: ))
    if valor % 2 == 0:
        num[0].append(valor}
    else:
        num[1].appemd(valor)
print('='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores ímpares digitados foram {num[1]}') 
"""
