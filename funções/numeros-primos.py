def maior_primo(n):
    for ct in range(n, 1, -1):
        if ePrimo(ct):
            return ct


def ePrimo(k):
    i = 1
    cont = 0
    while i <= k:
        if k % i == 0:
            cont += 1
        i += 1
        if cont > 2:
            return False
    return True