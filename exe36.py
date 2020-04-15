'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos
 ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ele não pode exeder a 30 % do do
 salário ou então o empréstimo será negado.
'''
valor = float(input('Informe o valor da imóvel: R$'))
sal = float(input('Informe o seu salário: R$'))
meses = valor / (sal / 100 * 30)
anos = float(input(f'Informe quanto anos para pagar. Mínimo de \033[31m{int(meses/12)}\033[m anos: '))
tempo = anos * 12
parcela = valor / tempo
if parcela <= (sal / 100 * 30):
    print('\033[32mEMPRÉSTIMO APROVADO!')
    print(f'O valor do imóvel é R${valor:.2f}, em {int(tempo)} prestações de R${parcela:.2f}.\033[m')
else:
    print('\033[31mEmpréstimo negado para essa compra.\033[m')