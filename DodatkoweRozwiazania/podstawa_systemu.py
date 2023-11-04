# Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry. Proszę napisać program, który wczytuje dwie
# liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie 2-16) w którym liczby są różno-cyfrowe. Program powinien wypisać
# znalezioną podstawę, jeżeli podstawa taka nie istnieje należy wypisać komunikat o jej braku. . Na przykład: dla liczb 123 i 522 odpowiedzią jest
# podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11).

def common_digit(number1, number2, s_base):
    Digits = [False] * s_base
    while number1 != 0:
        digit = number1 % s_base
        Digits[digit] = [True]
        number1 //= s_base
    while number2 != 0:
        digit = number2 % s_base
        if Digits[digit]:
            return True
        number2 //= s_base
    return False


def czy_ma_wspolne(number1, number2):
    s_base = 2
    for s_base in range(2, 17):
        if common_digit(number1, number2, s_base) == False:
            print(s_base)
            break
    else:
        print("brak systemu")


czy_ma_wspolne(20, 7)
