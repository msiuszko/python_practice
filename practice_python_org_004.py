#wyświetlanie liczby podanej przez użytkownika i wyświetlanie wszystkich dzielników
print("Give the number: ")
user_input = int(input())

for element in range (1,user_input+1):
    if (user_input % element) == 0:
        print(element)
