dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pagar = dias*60 + 0.15*km
print(f'O total a pagar é de R${pagar:.2f}')
