"""
Faça um programa que tenha uma função chamada escreva(),
 que receba um texto qualquer com parametros e mostre uma
 mensagem som tamanho adaptável.
 Ex:
 escreva('Olá, Mundo!")
 Saída
 ------------
  Olá, Mundo
 ------------
"""
def escreva(msg):
    tam = len(msg)+4
    print('~' *tam)
    print(f'  {msg}')
    print('~'* tam)


escreva('Everton Dutra')
escreva('Eduardo')
escreva('Anne')
escreva('Graziele')
