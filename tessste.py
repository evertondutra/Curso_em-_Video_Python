def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


r1 = fatorial(5)
r2 = fatorial(4)
r3 = fatorial()
print(f'Os resultados são {r1}, {r2}, {r3}.')