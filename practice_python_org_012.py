# ćwiczenie funkcji
# generuje listę liczb, w drugiej linii pobiera pierwszą i ostatnią wartość z listy
import random

list = random.sample(range(1,500), 10)
print(list)

def my_list():
    return [list[0], list[-1]]

print(my_list())