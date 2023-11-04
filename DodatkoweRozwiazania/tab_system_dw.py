# Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę jedynek,
# np. 22 = 10110 i 14 = 1110. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2>N1. Proszę napisać funkcję,
# która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba zgodnych
# elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne tablice powinny
# pozostać nie zmieniane.


def jedynki_binarne(x):
    ile = 0
    while x > 0:
        if x % 2 == 1:
            ile += 1
        x //= 2
    return ile


def zad14(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    for i in range(n2 - n1 + 1): #tablica, w której przesuwa się mała tablica w dużej tablicy
        for j in range(n2 - n1 + 1):  
            ile = 0
            for k in range(i, i + n1):  #sprawdzanie elementów w małej tablicy
                for l in range(j, j + n1):  
                    if jedynki_binarne(tab1[k - i][l - j]) == jedynki_binarne(tab2[k][l]):
                        ile += 1
            if ile / (n1 * n1) > 1 / 3:
                return True
    return False


x = [
    [1, 1, 0],
    [0, 0, 0],
    [0, 1, 0]
]
y = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]
print(zad14(x, y))
