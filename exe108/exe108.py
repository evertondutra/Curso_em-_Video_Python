"""
Adapte o código do desafio 107, criando uma função adicional
chamado moeda() que consiga mostrar os valores com um valor
 monetário formatado.
"""
import moeda

p = float(input('digite o preço: RS '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando o preço em 10%, temo {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuir o preço em 10%, temos {moeda.moeda(moeda.diminuir(p, 10))}')