# sprawdzanie czy podana liczba jest liczbą pierwsza
number = int(input ("Give a number: "))
x = [a for a in range (2, number) if number % a == 0]

def prime(z):
	if number > 1:
		if len(x) == 0:
			print ("The number is prime")
		else:
			print ("The number is not prime")
	else:
		print ("The number is not prime")
             
prime(number)
