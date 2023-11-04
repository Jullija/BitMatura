#  Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.

def zmiana(number, s_base):
    result = ""
    digits = "0123456789ABCDEF"
    while number > 0:
        result = digits[number % s_base] + result
        number //= s_base
    return result
