

def fun1():  #O()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = 0
    for i in range (0, len(arr)):
        sum += arr[i]



def fun2():  #O()
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sum = 0
    for i in range (0, len(arr)):
        for j in range (0, len(arr[i])):
            sum += arr[i][j]



def fun3(): #O()
    target = 5
    arr = [1, 2, 3, 4, 5, 6, 7]
    for i in range(len(arr)):
        if arr[i] == target:
            return i


def fun4(): #O()
    target = 2
    n = len(arr)
    arr = [1, 2, 3, 4, 5, 6, 7]
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if target < arr[middle]:
            right = middle - 1
        elif target > arr[middle]:
            left = middle + 1
        else:
            return middle



def fun5(): #O()
    a = 1
    b = 2
    if a > b:
        return True
    else:
        return False
    #można zapisać jako: return a > b


def fun6(): #O()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum
    for i in range (0, len(arr), 3):
        print(arr[i])


def fun7(): #O()
    for _ in range (10):
        target = 2
        n = len(arr)
        arr = [1, 2, 3, 4, 5, 6, 7]
        left = 0
        right = n - 1
        while left <= right:
                middle = (left + right) // 2
                if target < arr[middle]:
                        right = middle - 1
                elif target > arr[middle]:
                        left = middle + 1
                else:
                        return middle

