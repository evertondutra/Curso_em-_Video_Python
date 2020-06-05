def aumentar(preço, taxa):
    res = preço + (preço / 100 * taxa)
    return res


def diminuir(preço, taxa):
    res = preço - (preço /100 * taxa)
    return res


def dobro(preço):
    d = preço * 2
    return d


def metade(preço):
    m = preço / 2
    return m

