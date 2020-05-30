"""
Crie um programa que tenha a função leiaint(), que vai funcionar
de forma semelhantea função input() do python, só que fazendo
a validação para aceitar apenas um valor numérico.
Ex:
n = leiaint('Digite um número')
"""
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')