import random 
zgadles = 0

graj = True
while graj:
    x = random.randint(1,9)
    print(x)
    print("Zgadnij liczbę w przedziale 1-9")
    y = int(input())
    if x == y:
        print("Zgadłes")
        zgadles += 1
    elif y > x:
        print("Podałeś za wysoką liczbę") 
    else:
        print("Podałeś za małą liczbę")
    print('Chcesz zagrać jeszcze raz?', end = '')
    if (input().lower() == 'q'): 
        break

print('Zgadłeś {} razy.'.format(zgadles))