"""
Crie um programa que leia um nome e duas notasde vários alunos e
 guarde tudo em uma lista composta. No final, mostre o boletim
 contendo a média de cada um e permita que o usuário possa
 mostrar a nota de cada aluno individualmente.
"""
aluno = []
sala = []
med = 0
print('='*30)
print(f'{"AVALIAÇÃO DE ALUNOS":^30}')
print('='*30)
while True:
    aluno.append(input('Nome: '))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    sala.append(aluno[:])
    aluno.clear()
    resp = input('Continua?[S/N] ').strip().title()[0]
    if resp in 'N':
        print(f'{"-=-"*10}')
        break
    else:
        print('-'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-'*30)
for p,a in enumerate(sala):
    print(f'{p}   {a[0]:<10}      {(a[1]+a[2])/2:.1f}')
print('='*30)
while True:
    r = int(input('Mostrar notas de qual aluno? Digite [999] para sair. '))
    if r == 999:
        break
    else:
        print(f'Notas de {sala[r][0]} são {sala[r][1:]} ')
        print('_'*30)
print(f'{"FIM":^30}')
