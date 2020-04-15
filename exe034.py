sal = float(input('Qual o salário do funcionário? R$'))
if sal <= 1250:
    nsal = sal + sal / 100 * 15
else:
    nsal = sal + sal / 100 * 10
print(f'Quem ganhava R$\033[33m{sal:.2f}\033[m, passa a ganhar R$\033[33m{nsal:.2f}\033[m agora. ')
