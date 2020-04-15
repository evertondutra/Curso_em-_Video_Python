print('\033[33m-=-\033[m' * 17)
print('\033[31m ' * 11, 'Analisador de Triângulos\033[m')
print('\033[33m-=-\033[m' * 17)
s1 = float(input('Primerio seguimento: '))
s2 = float(input('Segundo seguimento: '))
s3 = float(input('Terceiro seguimento:? '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os seguimentos acima \033[34mpodem formar\033[m um triângulo.')
else:
    print('Os seguimentos \033[31mnão podem\033[m formar um triângulo.')