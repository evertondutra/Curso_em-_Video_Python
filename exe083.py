"""
Crie um programa onde o usuário digite uma expressão
qualquer que use parênteses. Seu aplicativo devera analizar
se a expressão passada esta com os parênteses abertos e
fechados na ordem correta.
"""
expr = input('Digite a expressão: ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão Válida')
else:
    print('\033[31mExpressão Inválida\033[m')