'''
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base da conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
'''

n = int(input('Informe um número inteiro para conversão: '))
esc = int(input('''[1] para \033[32mBinário\033[m:
[2] para \033[36mOctal\033[m:
[3] para \033[34mHexadecimal\033[m:'''))
if esc == 1:
    print(f'A conversão do {n} para binário é {bin(n)[2:]}')
elif esc == 2:
    print(f'A conversão do {n} para octal é {oct(n)[2:]}')
elif esc == 3:
    print(f'A conversão do {n} para hexadecimal é {hex(n)[2:]} ')
else:
    print('Opção inválida.')
