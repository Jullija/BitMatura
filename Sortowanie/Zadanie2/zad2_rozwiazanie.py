from zad2testy import runtests

def snow( S ):
    S.sort(reverse = True) #sortowanie malejąco. aby na początku zebrać najwiecej śniegu
    ans = 0
    for i in range (len(S)):
        if S[i] <= i: #sprawdzenie, czy w danym dniu możemy w ogóle dojsć do tego śniegu
            break
        ans += S[i] - i #odejmowanie i, czyli ile śniegu się stopiło
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )





