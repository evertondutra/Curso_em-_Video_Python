'''
Faça um programa que peça o ano de nascimento de um jove e informe,
 de acordo com a sua idade, se ele ainda deve se alistar ao serviço militar,
 se é hora de ele se alistar ou se ja passou do alistamento. Seu programa
 tambem deverá mostrar o tempo que falta ou o que ja passou do prazo
'''
from datetime import date
ano = int(input('Informe o ano de nascimento XXXX: '))
atual = date.today().year
idade = atual - ano
if idade < 18:
    print(f'A sua idade é {idade} anos e \033[33mainda falta {18 - idade} anos para se alista.\033[m')
    print(f'O seu alistamento será em {atual + (18 - idade)}')
elif idade == 18:
    print(f'A sua idade é {idade} anos e \033[34mesta na hora de se alistar.\033[m')
else:
    print(f'A sua idade é {idade} anos e \033[31mjá passou {idade - 18} anos do tempo de se alistar\033[m')
    print(f'Seu alistamento foi no ano de {atual - ( idade - 18)}')
