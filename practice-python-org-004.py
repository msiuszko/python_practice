print("Podaj liczbę: ")
user_input = int(input())

#x = range(1,a,1)
for element in range (1,user_input+1):
#    print(n)
    if (user_input % element) == 0:
        print(element)
