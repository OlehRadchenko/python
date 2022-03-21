import math

"""
pierwsza = 100
druga = 20

MyGames = ["Gothic", "Tetris", "LoL", "Minecraft", "Stalker", "Asassin"]
MyFilms = ["Breaking Bad", "Wojny Klonów", "Wiedźmin", "Perfekcyjny Chaos", "Dark"]
print(MyGames)
print(MyFilms)
MyHobby = MyGames + MyFilms
print(MyHobby)

Los = [2, 6, 8, 9, 2, 6, 4, 6, 7, 9]
for x in range(10):
    if Los[x] % 2 == 0:
        print("Liczba ", Los[x], " jest parzysta")
    else:
        print("Liczba ", Los[x], " nie jest parzysta")

    def silnia(n):
        if n<=1:
            return 1;
        else:
            return n * silnia(n-1)


    for x in range(10):
            wynik = silnia(Los[x])
            print("Silnia z ", Los[x], " jest równa ", wynik)
a = float(input())
b = float(input())
h = float(input())


delta = lambda a, b, c: (b*b) - (4*a*c)
print(math.sqrt(delta(a, b, h)))

a = float(input())
b = float(input())
h = float(input())
pole_trap = lambda a,b,h: ((a+b)*h)/2
print(pole_trap(a,b,h))
"""
czworoscian_foremny = lambda a, H: math.sqrt((1/2*a*1/2*a) + (a*a)) * 1/3 * H
