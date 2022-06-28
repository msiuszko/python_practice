import random 

#łączenie list, set służy do wyświetlenia unikalnych wartości
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = a + b
print (set(c))

#pętla służąca do printowania 10 liczb z zakresu od 1 do 100
x = 0
listaa = []
while x < 10:
    listaa.append(random.randint(1, 100))
    x = x + 1
print(listaa)

x = 0
listab = []
while x < 10:
    listab.append(random.randint(1, 100))
    x = x + 1
print(listab)

#łączy listę a i b i wyświetla unikatowe elementy
d = listaa + listab
print(set(d))
