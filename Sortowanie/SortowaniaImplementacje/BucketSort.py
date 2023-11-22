def insertSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    for idx in range(1, n):
        value = arr[idx]
        curr_idx = idx - 1
        while curr_idx != -1 and value < arr[curr_idx]:
            arr[curr_idx + 1] = arr[curr_idx]
            curr_idx -= 1
        arr[curr_idx + 1] = value
    return arr



arr=[1,4,3,5,6,2,7,19,3,10,22,15,4]
print(arr)
insertSort(arr)
print(arr)