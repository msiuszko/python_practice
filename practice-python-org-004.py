print("Podaj liczbę: ")
a = int(input())

#x = range(1,a,1)
for n in range (1,a+1):
#    print(n)
    if (a % n) == 0:
        print(n)
   
    