"""
teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)
"""
"""
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')
"""
"""galera = []
dado = []
for c in range(0, 3):
    dado.append(input('NOME: '))
    dado.append(int(input('IDADE: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print(galera)
"""
dado = []
galera = []
p = 0
for c in range(0, 2):
    while True:
        dado.append(input('Email: '))
        if dado[0] in '@' and '.com':
            break
        else:
            print('Email inválido')

print(dado)