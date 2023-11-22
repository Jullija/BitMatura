def countSort(arr, maxi):
    n = len(arr)
    count = [0 for _ in range(maxi+1)]
    result = [0 for _ in range(n)]
    for number in arr:
        count[number] += 1
    for i in range(1, maxi+1):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        count[arr[i]] -= 1
        result [count[arr[i]]] = arr[i]
    return result


arr=[1,4,3,5,6,2,7,19,3,10,22,15,4]
maxi = max(arr)
print(arr)
print(countSort(arr, maxi))
