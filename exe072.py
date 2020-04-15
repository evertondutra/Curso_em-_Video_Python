"""
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extensão, de zero a vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20)
e mostrá-lo por extenso.
"""
ext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze','dezesseis','dezesete','desoito',
       'dezenove','vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    else:
        print('Tente novamente')
print(f'Você digitou o número {ext[n]}')


