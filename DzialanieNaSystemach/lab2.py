def nwd(a, b): #O(log(min(a, b)))
    while b !=0 :
        r = a % b
        a = b
        b = r
    return a





def systems(number, base):
    res = ""
    digits = "0123456789ABCDEF"
    while number > 0:
        tmp = number % base
        res = digits[tmp] + res
        number //= base
    return int(res)





import math
def task20(number):
    # length = 0
    # while number > 0:
    #     length += 1
    #     number //= 10
    #n = int(math.log10(number)) + 1

    n = len(str(number))
    new_number = 0
    save_numb = number

    while number > 0:
        last_digit = number % 10
        new_number += last_digit ** n
        number //= 10

    return new_number == save_numb






def task59():
    file = open("liczby.txt", 'r')
    ans = 0

    while True:
        line = file.readline()
        if not line:
            break

        number1 = line
        number2 = number1[::-1]

        number1 = int(number1)
        number2 = int(number2)

        added = str(number1 + number2)

        if added == added[::-1]:
            ans += 1


    return ans



def swap(number):
    new_number = 0
    while number > 0:
        new_number *= 10 
        new_number += number % 10 
        number //= 10 
    return new_number





def task59_2():
    file = open("liczby.txt", 'r')
    ans = 0

    while True:
        number = file.readline()
        if not number:
            break


        number = int(number)
        number_swap = swap(number)

        added = number + number_swap
        if added == swap(added):
            ans += 1

    return ans






def digits_sum(num):
    new_number = 0
    while num > 0:
        last_digit = num % 10
        new_number += last_digit
        num //= 10
    return new_number




def task66():
    file = open("trojki.txt", "r")
    ans = 0

    while True:
        line = file.readline()
        if not line:
            break

        numbers = line.split() 

        if digits_sum(int(numbers[0])) + digits_sum(int(numbers[1])) == int(numbers[2]):
            ans += 1

    return ans



def sieve_eratostenes(number):
    numbers = [True] * number # [True for _ in range (number)]
    numbers[0], numbers[1] = False, False

    for i in range (2, number):
        if numbers[i]:
            for j in range (2*i, number, i):
                numbers[j] = False
    

    for i in range(2, number):
        if numbers[i]:
            print(i)
