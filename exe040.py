"""
Crie umprograma que leia duas notas de um aluno,
e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5,0: REPROVADO
- Média entre 5,0 e 6,9: RECUPERAÇÃO
- Média 7,0 ou superior: APROVADO
"""
print('='*30)
print(F'{"CALCULANDO MÉDIA":^30}')
print('='*30)
n1= float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    est = 'REPROVADO'
elif 5 <= med < 7:
    est = 'de RECUPERAÇÃO'
else:
    est = 'APROVADO'
print(f'A média é {med:.2f} e o aluno esta {est}.')