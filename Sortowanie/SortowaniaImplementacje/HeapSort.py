def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(T, n, idx):
    l = left(idx)
    r = right(idx)
    curr_idx = idx
    if l < n and T[curr_idx] < T[l]:
        curr_idx = l
    if r < n and T[curr_idx] < T[r]:
        curr_idx = r
    if curr_idx != idx:
        T[idx], T[curr_idx] = T[curr_idx], T[idx]
        heapify(T, n, curr_idx)


def buildHeap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)


def heapSort(T):
    n = len(T)
    buildHeap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)
    return T


def insertToHeap(T, key):
    T = heapSort(T)
    n = len(T)
    idx = n
    T.append(key)
    while idx > -1:
        parent_idx = parent(idx)
        if T[parent_idx] > key:
            T[idx], T[parent_idx] = T[parent_idx], T[idx]
            idx = parent_idx
        else:
            return idx


def heapPop(T):
    n = len(T)
    T = heapSort(T)
    T[0] = T.pop(n - 1)
    heapify(T, n - 1, 0)
    return T[0]



arr=[1,4,3,5,6,2,7,19,3,10,22,15,4]
print(arr)
heapSort(arr)
print(arr)