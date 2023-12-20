def duplicate(arr):
    dic = {}
    for num in arr:
        dic[num] = dic.get(num, 0) + 1
    print(dic)

    return True if len(set(arr)) < len(arr) else False



#duplicate([1,2,3, 1])



def majority(arr):
    dic = {}
    for num in arr:
        dic[num] = dic.get(num, 0) + 1

    maxi = 0
    maxi_key = 0
    for key, value in dic.items():
        if value > maxi:
            maxi = value
            maxi_key = key
    print(maxi_key)


#-----SECOND ANSWER-----
    arr.sort()
    mid = len(arr) // 2
    print(arr[mid])


#majority([2,2,1,1,1,2,2, 3, 3, 3, 3, 3, 3, 3, 3, 3])



def anagram(s, t):
    if len(s) != len(t):
        return False
    
    dic = {}
    for letter in s:
        dic[letter] = dic.get(letter, 0) + 1


    for letter in t:
        if letter not in dic:
            return False

        dic[letter] -= 1
    
    for value in dic.values():
        if value != 0:
            return False
    
    return True

#print(anagram(s = "anagram", t = "nagaram"))
    


def merge(arr1, arr2):
    arr1_ref = 0
    arr2_ref = 0
    ans = []


    while arr1_ref < len(arr1) and arr2_ref < len(arr2):
        if arr1[arr1_ref] < arr2[arr2_ref]:
            ans.append(arr1[arr1_ref])
            arr1_ref += 1
        else:
            tmp = arr2[arr2_ref]
            ans.append(tmp)
            arr2_ref += 1
            

    while arr1_ref< len(arr1):
        ans.append(arr1[arr1_ref])
        arr1_ref += 1

    while arr2_ref< len(arr2):
        ans.append(arr2[arr2_ref])
        arr2_ref += 1
        
    print(ans)

#merge([1,2,4, 5, 6, 8,], [1,3,4, 5])




def cookies(g, s):
    g.sort(reverse = True)
    s.sort(reverse = True)

    i, j = 0, 0
    ans = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            ans += 1
            j += 1
        i += 1
    print(ans)


#cookies(g = [1,2], s = [1,2,3])


def meetings(intervals):
    intervals.sort()
    for i in range (len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
        
    return True


#print(meetings([[7,10],[2,4]]))





