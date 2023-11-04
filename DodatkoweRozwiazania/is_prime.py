# Proszę sprawdzić czy liczba jest liczbą pierwszą.
import math

class testing_wrapper:
    def __init__(self):
        self.__test_count = 0
        self.__test_passed = 0

    def test_ok(self):
        self.__test_count += 1
        self.__test_passed += 1
        print(f'Test {self.__test_count}\tPASSED')

    def test_fail(self):
        self.__test_count += 1
        print(f'Test {self.__test_count}\tFAILED')

    def summary(self):
        print(f'Passed: {self.__test_passed}/{self.__test_count} tests')


def is_prime(number):
    
    # for i in range(2,number):
    #     if (number%i) == 0:
    #         return False
    # return True


    # for i in range(2,int(math.sqrt(number))+1):
    #     if (number%i) == 0:
    #         return False
    # return True
    
    # if number==2 or number==3: return True
    # if number%2==0 or number<2: return False
    # for i in range(3, int(number**0.5)+1, 2):   # only odd numbers
    #     if number%i==0:
    #         return False    

    # return True
    
    
    
    
    
    if number == 2 or number == 3:
        return True
    
    if number == 1 or number == 0:
        return False
    
    last_number = math.sqrt(number)
    last_number = math.ceil(last_number)

    cur_div = 2

    while cur_div <= last_number:
        if number % cur_div == 0:
            return False
        cur_div += 1
    
    return True

if __name__ == '__main__':
    tester = testing_wrapper()
    tester.test_ok() if not is_prime(20) else tester.test_fail()
    tester.test_ok() if is_prime(2) else tester.test_fail()
    tester.test_ok() if not is_prime(1) else tester.test_fail()
    tester.test_ok() if not is_prime(0) else tester.test_fail()
    tester.test_ok() if not is_prime(36) else tester.test_fail()
    tester.test_ok() if is_prime(7) else tester.test_fail()

    tester.summary()

# Sprawdzamy czy liczba jest jedną z początkowych liczb pierwszych (dwójka lub trójka), następnie sprawdzamy czy jest to mniejsza lub równa 1 lub czy
# dzieli się przez dwie powyższe, jeśli nie sprawdzamy kolejne potencjalne dzielniki idąc od 5 wzorem +2, +4, czyli sprawdzamy czy liczba dzieli
# się kolejno przez 5, 7, 11, 13, jeśli dojdziemy do pierwiastka z naszej liczby i pętla zakończy się nie zwracając False, oznacza, że znaleźliśmy
# liczbę pierwszą.


