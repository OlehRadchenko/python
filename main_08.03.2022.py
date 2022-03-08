szescian = lambda a:a*a*a
prostopadloscian = lambda a,b,c:a*b*c
kula = lambda r:(4/3)*(3.14)*(r*r*r)
opcja = int(input("Wybierz co chcesz obliczyc?\n1. Objetosc sześcianu\n2. Objetosc prastopadloscianu\n3. Objetosc kuli\n"))
if(opcja == 1):
    a = int(input("Podaj dlugosc odcinka a: "))
    print("Objetosc szescianu o boku: ",a," = ",szescian(a))
elif(opcja == 2):
    a = int(input("Podaj dlugosc odcinka a: "))
    b = int(input("Podaj dlugosc odcinka b: "))
    c = int(input("Podaj dlugosc odcinka c: "))
    print("Objetosc prostopadloscianu o bokach: ",a,", ",b,", ",c," = ",prostopadloscian(a,b,c))
elif(opcja == 3):
    r = int(input("Podaj promien kuli: "))
    print("Objetosc kuli o promieniu: ",r," = ",kula(r))
else:
    print("Nie klam, ta liczba jest poza zakresem")