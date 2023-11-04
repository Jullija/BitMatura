# Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.

def sito(number):
    Numbers = [True]*number
    Numbers[0], Numbers[1] = False, False
    for i in range(2, number):
        if Numbers[i]:
            for j in range(2*i, number, i):
                Numbers[j] = False

    for i in range(2, number):
        if Numbers[i]:
            print(i)


sito(100)
