# Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest tablica
# T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zwraca pary liczb leżące obok 
# siebie w tablicy, które są komplementarne

import math



def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i < math.sqrt(x) + 1:
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def zad13(tab):
    n = len(tab)
    result =[]
    for i in range(n-1):
        for j in range(n-1):
            if is_prime(tab[i][j]+tab[i][j+1]):
                result.append((tab[i][j],tab[i][j+1]))
            if is_prime(tab[i][j]+tab[i+1][j]):
                result.append((tab[i][j],tab[i+1][j]))
            if is_prime(tab[i][j]+tab[i+1][j+1]):
                result.append((tab[i][j],tab[i+1][j+1]))

    return result


x = [
    [2, 6, 2, 4],
    [2, 6, 3, 8],
    [9, 1, 3, 2],
    [2, 4, 17, 6]
]
print(zad13(x))
print(is_prime(1 + 6))
