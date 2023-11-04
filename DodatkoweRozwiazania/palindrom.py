# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.

def digit_counter(number):
    suma = 0
    while number > 0:
        suma += 1
        number = number // 10
    return suma


def na_binary(number):
    power = 0
    result = 0
    while number > 0:
        if number % 2 != 0:
            result += 10 ** power
        power += 1
        number = number // 2
    return result


def czy_palindrom(number):
    digits = digit_counter(number)
    while digits > 1:
        number_tip = number % (10 ** (digits - 1))
        # to jest zabranie tej pierwszej jedynki z liczby 121
        first_digit = (number - number_tip) // 10 ** (digits - 1)
        last_digit = number % 10  # zabranie ostatniej 1 z 121
        if first_digit != last_digit:
            return False
        number -= number - number_tip
        number //= 10
        digits -= 2
    return True


def zad3(x):
    print("czy palindrom: ")
    print(czy_palindrom(x))
    print("binar")
    x = na_binary(x)
    print(x)
    print(czy_palindrom(x))


zad3(21)
