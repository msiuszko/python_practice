#zwraca elementy wspólne (bez duplikatów)
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print([x for x in set(a) if x in b])



#zwraca unikalne wartości dla liczb losowych z podanego zakresu, z określoną ilością liczb w liscie
q = random.sample(range(10,30), 10)
print(q)
w = random.sample(range(1,40), 12)
print(w)
print([e for e in set(q) if e in w])
