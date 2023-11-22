def insertSort(T):
    n = len(T)
    if n < 2:
        return T
    for idx in range(1, n):
        value = T[idx]
        curr_idx = idx - 1
        while curr_idx != -1 and value < T[curr_idx]:
            T[curr_idx + 1] = T[curr_idx]
            curr_idx -= 1
        T[curr_idx + 1] = value
    return T

arr=[1,4,3,5,6,2,7,19,3,10,22,15,4]
print(arr)
insertSort(arr)
print(arr)