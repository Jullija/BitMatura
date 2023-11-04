 # Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie: l - liczba całkowita oznaczająca
# licznik, m - liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
# m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie

def kalkulator():
    print("Wpisz licznik:")
    l = int(input())
    print("Wpisz mianownik:")
    m = int(input())
    number = (l,m)
    print("Wybierz działanie: \n 1. Dodawanie \n 2.Odejmowanie \n 3. Mnożenie \n 4. Dzielenie \n 5. Potęgowanie \n 6. Skracanie \n 7. Wypisz aktualną liczbę \n 0. Zakończ działanie kalkulatora")
    action = input()
    while action!="0":
        if action == "1":
            print("Wprowadź licznik drugiej liczby:")
            l1 = int(input())
            print("Wprowadź mianownik drugiej liczby:")
            l2 = int(input())
            number2 = (l1,l2)
            number = add(number,number2)
            print("wynik:", number)
        elif action == "2":
            print("Wprowadź licznik drugiej liczby:")
            l1 = int(input())
            print("Wprowadź mianownik drugiej liczby:")
            l2 = int(input())
            number2 = (l1,l2)
            number = substract(number,number2)
            print("wynik:", number)
        elif action == "3":
            print("Wprowadź licznik drugiej liczby:")
            l1 = int(input())
            print("Wprowadź mianownik drugiej liczby:")
            l2 = int(input())
            number2 = (l1,l2)
            number = multiply(number,number2)
            print("wynik:", number)
        elif action == "4":
            print("Wprowadź licznik drugiej liczby:")
            l1 = int(input())
            print("Wprowadź mianownik drugiej liczby:")
            l2 = int(input())
            number2 = (l1,l2)
            number = divide(number,number2)
            print("wynik:", number)
        elif action == "5":
            number = power(number)
            print("wynik:", number)
        elif action == "6":
            number = abbreviate(number)
            print("wynik:", number)
        elif action == "7":
            print(number)
        else:
            print("Wprowadzono zły argument, wprowadź jeszcze raz")
            action = input()
            continue
        print("Wybierz działanie: \n 1. Dodawanie \n 2.Odejmowanie \n 3. Mnożenie \n 4. Dzielenie \n 5. Potęgowanie \n 6. Skracanie \n 7. Wypisz aktualną liczbę \n 0. Zakończ działanie kalkulatora")
        action = input()
        

def nwd(x,y):
    while y:
        x,y = y, x%y
    return abs(x)

def abbreviate(number):
    nwd_number = nwd(number[0],number[1])
    return(number[0]//nwd_number,number[1]//nwd_number)


def add(number1,number2):
    if number1[1] == number2[1]:
        return (number1[0]+number2[0],number1[1])
    else:
        number = (number1[0]*number2[1]+number2[0]*number1[1],number1[1]*number2[1])
        return abbreviate(number)
    
def substract(number1,number2):
    if number1[1] == number2[1]:
        return (number1[0]-number2[0],number1[1])
    else:
        number = (number1[0]*number2[1]-number2[0]*number1[1],number1[1]*number2[1])
        return abbreviate(number)
    
def multiply(number1,number2):
    number = (number1[0]*number2[0],number1[1]*number2[1])
    return abbreviate(number)

def divide(number1,number2):
    number = (number1[0]*number2[1],number1[1]*number2[0])
    return abbreviate(number)

def power(number):
    print("Wprowadź potęgę:")
    power = int(input())
    number = (number[0]**power,number[1]**power)
    return abbreviate(number)

kalkulator()