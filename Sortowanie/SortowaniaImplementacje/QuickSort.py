def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range (p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)



arr=[1,4,3,5,6,2,7,19,3,10,22,15,4]
print(arr)
quickSort(arr, 0, len(arr)-1)
print(arr)