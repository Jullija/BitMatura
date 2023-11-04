# Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę
# zaimplementować funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
# (1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
# (2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
# Funkcja powinna zwrócić liczbę znalezionych trójek


def nwd(number1, number2):
    while number2 > 0:
        number1, number2 = number2, number1 % number2
    return number1


#jedna przerwa obojętnie jakiej długości
def trojki(tab):
    n = len(tab)
    counter = 0
    for i in range(n-3+1):  # trójki obok siebie
        if nwd(nwd(tab[i], tab[i+1]), tab[i+2]) == 1:
            print(tab[i], tab[i+1], tab[i+2])
            counter += 1
    for i in range(4, n+1):
        for j in range(n-i+1):  
            if nwd(nwd(tab[j], tab[j+1]), tab[j+2+(i-3)]) == 1:
                print(tab[j], tab[j+1], tab[j+2+(i-3)])
                counter += 1
            if nwd(nwd(tab[j], tab[j+1+(i-3)]), tab[j+2+(i-3)]) == 1: 
                print(tab[j], tab[j+1+(i-3)], tab[j+2+(i-3)])
                counter += 1
    return counter


#jedna przerwa długości max 1
def trojki2(tab):
    n = len(tab)
    counter = 0
    for i in range(n-3+1):  # trójki obok siebie 123
        if nwd(nwd(tab[i], tab[i+1]), tab[i+2]) == 1:
            print(tab[i], tab[i+1], tab[i+2])
            counter += 1
    
   
    for i in range(n-4):# co dwa, np 1 3 5
        if nwd(nwd(tab[i], tab[i+2]), tab[i+4]) == 1:
            print(tab[i], tab[i+1], tab[i+2])
            counter += 1
            
    for i in range (n-3): # jeden przerwy, np 1 2 4
        if nwd(nwd(tab[i], tab[i+1]), tab[i+3]) == 1:
            print(tab[i], tab[i+1], tab[i+3])
            counter += 1
        if nwd(nwd(tab[i], tab[i+2]), tab[i+3]) == 1:
            print(tab[i], tab[i+2], tab[i+3])
            counter += 1 
        
        