# Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę
# zaimplementować funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
# (1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
# (2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
# Funkcja powinna zwrócić liczbę znalezionych trójek


def nwd(number1, number2):
    while number2 > 0:
        number1, number2 = number2, number1 % number2
    return number1


def trojki(tab):
    n = len(tab)
    counter = 0
    for i in range(n-3+1):  # trójki obok siebie
        if nwd(nwd(tab[i], tab[i+1]), tab[i+2]) == 1:
            print(tab[i], tab[i+1], tab[i+2])
            counter += 1
    for i in range(4, n+1):  # 4
        for j in range(n-i+1):  # 0
            # tab[0], tab[1], tab[2 + 4 - 3]
            if nwd(nwd(tab[j], tab[j+1]), tab[j+2+(i-3)]) == 1:
                print(tab[j], tab[j+1], tab[j+2+(i-3)])
                counter += 1
            if nwd(nwd(tab[j], tab[j+1+(i-3)]), tab[j+2+(i-3)]) == 1:  # tab[0], tab[1+1], tab[3]
                print(tab[j], tab[j+1+(i-3)], tab[j+2+(i-3)])
                counter += 1
    return counter
