vel = int(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('\033[31mMultado! Você excedeu o limite permitido que é de 80 km/h\033[m')
    print(f'Você deve pagar uma multa de R${(vel - 80) * 7:.2f}')
print('Tenha um bom dia! Dirija com segurança!')
