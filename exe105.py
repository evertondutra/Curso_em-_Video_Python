"""
Faça um programa que tenha uma função notas() que pode receber várias
notas de um aluno e vai retornar um dicionário com as
seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicionar também as docstrings.
"""
def notas(*n, sit = False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: notas (uma ou mais)
    :param sit: situação (valor opcional)
    :return: dicionário com várias informaçoes sobre o aluno.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'boa'
        elif r['média'] >= 5:
            r['situação'] = 'razoavél'
        else:
            r['situação'] = 'ruim'
    return r


resp = notas(4, 5, 9, 2, sit=True)
#print(resp)
#help(notas)
for k,v in resp.items():
    print(k, v)
