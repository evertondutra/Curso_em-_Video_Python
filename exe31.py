dis = int(input('Informe a distância da sua viagem em km: '))
if dis <= 200:
    print(f'O preço da passagem é de R${dis * 0.50:.2f} ')
else:
    print(f'O preço da passagem é de R${dis * 0.45:.2f}')
