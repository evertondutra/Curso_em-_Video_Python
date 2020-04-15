"""
Crie um programa que tenha uma tupla única com nomes
de produtos e seus respectivos preços, na sequencia.
No final uma listagem de preços, organizando os dados
em forma tabular.
"""
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            "Livro", 34.90)
print('-'*38)
print(f'{"LISTAGEM DE PREÇO":^38}')
print('-'*38)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${listagem[pos]:>6.2f}')
print('-'*38)