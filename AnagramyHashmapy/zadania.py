def rownowazne(word1, word2):
    dic = {}
    for letter in word1:
        dic[letter] = dic.get(letter, 0) + 1

    for letter in word2:
        if letter not in dic:
            print("Nie są równoważne")
            return

        dic[letter] -= 1
        if dic[letter] < 0:
            print("Nie są równoważne")
            return
    print("Równoważne")
    return
#rownowazne("ABCA", "ABCC")

def podrzedne(word1, word2):
    dic = {}
    for letter in word1:
        dic[letter] = 1

    k = 0
    for letter in word2:
        if letter in dic:
            dic[letter] = 0
        elif letter not in dic:
            k += 1
    
    for value in dic.values():
        if value != 0:
            print("Niepodrzędne")
            return
    print("Podrzędne ", k)
    return

#podrzedne("HHGGFFEEDDCCBBAA", "ABCDEFGH")

def wzorzec27(pattern, text):
    if pattern in text:
        print("Wzorzec w tekście")
        return True

    for i in range(len(text) - len(pattern) + 1):
        count_diff = 0
        for j in range(len(pattern)):
            if pattern[j] != text[i+j]:
                count_diff += 1
        if count_diff == 1:
            print("Wzorzec w tekście")
            return True
        
    print("Wzorca nie ma w tekście")
    return False
wzorzec27("sport", "bezsportie")



def palindromA(W):
    #pierwszy warunek - tylko z liter A
    if W == "A":
        print("Palindrom")
        return True

    #drugi warunek - parzysta długość i te śmieszne takie
    if len(W) % 2 == 0:
        if (W[0] == W[len(W) - 1]) and (palindromA(W[0:len(W) //2]) or palindromA(W[(len(W))//2:])):
            print("Palindrom")
            return True
        print("Nie palindrom")
        return False
    print("Nie palindrom")
    return False



#palindromA("AAAAAAAAAA")


def kulki(message):
    dic={"cc":"a", "bcc":"b", "bbcc":"c", "cbcc":"d", "bbbcc":"e", "bcbcc":"f", "cbbcc":"g", "bbbbcc":"h", "bbcbcc":"i", "bcbbcc":"j", "cbbbcc":"k", "cbcbcc":"l", 
         "bbbbbcc":"m", "bbbcbcc":"n", "bbcbbcc":"o", "bcbbbcc":"p", "cbbbbcc":"r", "cbbcbcc":"s", "cbcbbcc":"t", "bbbbbbcc":"u", "bbbbcbcc":"w", "bbbcbbcc":"x", 
         "bbcbbbcc":"y", "bcbbbbcc":"z"}
    
    i = 1
    ans = ""
    tmp = 0
    while i < len(message):
        if message[i] == message[i-1] == "c": #znaleźliśmy koniec słowa
            letter = dic[message[tmp:i+1]]
            ans+=letter
            tmp = i+1
            i += 2
        else:
            i += 1
    print(ans)

#kulki("bbbbbcccccbcbbccbbbbbbcccbbbbcccc")




def szyfr(word): #ord -> zamienia literkę na znak ASCII
    ans = ""
    for (i, val) in enumerate(word):
        coded_letter = ord(val) + (i + 1)
        ans += chr(coded_letter)
    print(ans)


def deszyfrowanie(word): #ord -> zamienia literkę na znak ASCII
    ans = ""
    for (i, val) in enumerate(word):
        coded_letter = ord(val) - (i + 1)
        ans += chr(coded_letter)
    print(ans)



szyfr("BIT")
deszyfrowanie("CKW")






def genotyp(word):

    i = 1
    start_idx = 0
    ans = []
    looking_for_B = False
    while i < len(word):
        if looking_for_B:
            if word[i] == word[i-1] == "A": #np    AA CDCD AA DBB
                start_idx = i-1
                i +=1

            if word[i] == word[i-1] == "B": #genotyp found
                ans.append(word[start_idx:i+1])
                looking_for_B = False
                i+=2
            else:
                i+=1
        elif word[i] == word[i-1] == "A": #start genu
            looking_for_B = True
            start_idx = i-1
            i +=1
        else:
            i += 1

    print(ans)


#genotyp("AACDCDAADBB")




def hasla(password):
    for char in password:
        print(char.isalpha())
        # if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        #     return False

hasla("Aa2")


