while True:
#dopóki warunek jest spełniony wykonuj pętle 
    print("Podaj liczbę ")
    number = int(input())
    if number % 4 == 0:
        print("To jest wielokrotność liczby 4")

    elif number % 2 == 0:
        print("To jest liczba parzysta ")

    else:
        print("To jest liczba nieparzysta")
            #break

    print("Podaj drugą liczbę")
    number2 = int(input())
    if number % number2 == 0:
        print("Te liczby możesz podzielić ")
    else:
        print("Tych liczb nie możesz podzielić")