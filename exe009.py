n = int(input('Digite um npumero para ver a sua tabuada: '))
lista = []
for i in range(11):
    print(f'{n} X {i} = {n*i}')
    lista.append(n*i)

print(lista)
