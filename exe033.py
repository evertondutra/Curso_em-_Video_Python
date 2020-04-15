n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior número foi \033[31m{maior}\033[m')
print(f'O menor número foi \033[35m{menor}\033[m')

'''
lista = [n1, n2, n3]
lista.sort()
print(f'O maior número foi {lista[2]}')
print(f'O menor número foi {lista[0]}')
'''
