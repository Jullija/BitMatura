def bubbleSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



arr=[1,4,3,5,6,2,7,19,3,10,22,15,4]
print(arr)
bubbleSort(arr)
print(arr)