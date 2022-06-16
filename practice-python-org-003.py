a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
 if x < 5:
  print(x)
#print([e for e in a if e < 5]) - to jest druga możliwość wykonania polecenia nr 1
print([e for e in a if e < 5])
#print([a for a in a if a<5])- to jest drua opcja do polecenia nr 2

print("Podaj liczbę ")
liczba = int(input())
print([a for a in a if a < liczba])

