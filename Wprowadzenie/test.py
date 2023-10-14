def test_function():
    print("Hello world")

def test_function2(x, y):
    sum = x + y
    print(sum)

test_function2(2, 3)




a = 5      #int
b = "ala"  #string
c = 5.3    #float
d = True   #boolean

a = 5
print(a)
a = "ala"
print(a)




b = 0
while b < 10:
    b += 1
    print(b)


b = 0
for i in range (0, 10):
    b += 1
    print(b)





ala_ma_kota = True

if ala_ma_kota:
    print("Ala ma kota")
else:
    print("Ala nie ma kota")


a = 2

if a > 0:
    print ("Dodatnia")
elif a < 0:
    print ("Ujemna")
else:
    print("Zero")



array = []
array.append(1)
array.append(2)
print(array)
array.remove(1)
print(array)


for i in array:
    print(i)



array = [5, 4, 3, 2, 1]
for idx, value in enumerate(array):
    print(idx, value)



tmp = (1, 2)

for i in tmp:
    print(i)



two_dim_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in two_dim_array:
    print(i)



for i in two_dim_array:
    print(i[0])


dic = {}
dic["one"] = 1
dic["two"] = 2
print(dic)


for key in dic:
    print(key)

    
for value in dic.values():
    print(value)

for key, value in dic.items():
    print (key, value)


    
array = [5, 4, 3, 2, 1]
for idx, value in enumerate(array):
    print(idx, value)