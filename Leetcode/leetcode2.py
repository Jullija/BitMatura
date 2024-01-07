def paths(path):
    directions = {"N": (0, 1), "E":(1, 0), "S": (0, -1), "W": (-1, 0)}
    visited = {(0, 0)}
    last = (0, 0)
    for letter in path:
        vector = directions[letter]
        curr = (last[0] + vector[0], last[1] + vector[1])
        if curr in visited:
            return True
        else:
            visited.add(curr) 
            last = curr
    return False

# print(paths("SS"))




def sortSentence(s):
    ans = ""
    words = s.split()
    last = 0
    i = 0
    while i < len(words):
        for word in words:
            num  = int(word[-1]) 
            if num == last + 1:
                ans += word[0:len(word) - 1] + " "
                last = num
                i += 1
                break    
    print(ans)
    
    
def sortSentence2(sentence):
    ans = ""
    words = sentence.split()
    sorted = ["" for _ in range (len(words))]
    for word in words:
        num = int(word[-1]) - 1
        sorted[num] = word[0:len(word) - 1]
        
    for word in sorted:
        ans += word + " "
    print(ans)
    
    
#sortSentence("is2 sentence4 This1 a3")

   
   
   
   
def frequencySort(word):
    dic = {}
    ans = ""
    for letter in word:
        dic[letter] = dic.get(letter, 0) + 1 
        
    for i in sorted(dic.items(), key = lambda item:item[1]):
        ans += i[0] * i[1]   
    print(ans[::-1])
   
    
    
#frequencySort("tree")