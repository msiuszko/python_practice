# sprawdzanie czy podana liczba jest liczbą pierwsza
import sys

number = (input("Give a number:"))
number = int(number)
prime = False

def pierwsza(number):
    for x in range (2, number -1):
        if number % x != 0:
            continue
        elif number % x == 0:
            print("To nie jest liczba pierwsza")
        sys.exit("To nie l. pierwsza")
    sys.exit("To nie pierwsza")
