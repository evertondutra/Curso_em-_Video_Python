from random import randint
from time import sleep
n = randint(0, 5)
print('-=-'*17)
print('Vou pensar em um número de 0 a 5. Tente advinhar...')
print('-=-'*17)
ne = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if ne == n:
    print('PARABÉNS, você conseguiu me vencer!!!!')
else:
    print(f'GANHEI! Eu pensei no número {n} e não no {ne}!')
print('FIM')
