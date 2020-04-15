from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja? '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o Seno de {seno:.2f}')
print(f'O ângulo de {angulo} tem o Cosseno de {cos:.2f}')
print(f'O ângulo de {angulo} tem o Tangente de {tan:.2f}')

'''
import math
angulo = float(input('Digite o ângulo que você deseja? '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem o Seno de {seno:.2f}')
print(f'O ângulo de {angulo} tem o Cosseno de {cos:.2f}')
print(f'O ângulo de {angulo} tem o Tangente de {tan:.2f}')
'''