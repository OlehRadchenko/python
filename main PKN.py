import numpy as np
wynik = 0
bot_wynik = 0
x=0
print('Slyszalem ze chcesz zagrac w "Papier, kamien, nozyce"')
while wynik!=3 or bot_wynik!=3:
    x+=1
    print("Runda ", x)
    print("Wybierz: \n1.Papier\n2.Kamien\n3.Nozyce")
    wybor = int(input())
    if(wybor == 1):
        print("Wybrales papier")
    elif(wybor == 2):
        print("Wybrales kamien")
    elif(wybor == 3):
        print("Wybrales nozyce")
    else:
        print("Nie prawidlowa wartosc ;c. A wiec przegrales")
        exit()

    los = int(np.random.randint(3, size=1) + 1)
    if(los == 1):
        print("Bot wybral papier")
    elif(los == 2):
        print("Bot wybral kamien")
    elif(los == 3):
        print("Bot wybral nozyce")
    else:
        print("Bot jest glupi ;c")

    if(wybor == los):
        bot_wynik += 1
        wynik += 1
    elif((wybor == 1 and los == 2) or (wybor == 2 and los == 3) or (wybor == 3 and los == 1)):
        wynik += 1
    else:
        bot_wynik += 1
    print("Aktualny wynik: \nTy - ", wynik, "\nBot - ", bot_wynik, "\n\n\n")
    if(wynik == 3):
        print("Brawo, wygrales!")
        exit()
    elif(bot_wynik == 3):
        print("Bot wygral ;c")
        exit()