import turtle
import time
import random

global typ, wynik, nagralo, pieniadze
typ = 0
wynik = 0
nagralo = False
pieniadze = 10

turtle.bgcolor('grey')
turtle.title("Wyścig żółwi")

# ustawienie miejsca napisu oraz jego koloru
meta = turtle.Turtle()
meta.color('white')
meta.penup()
meta.goto(280, 320)

#rysowanie linii mety + napis
meta.write("Meta", font=("Arial", 15, "bold"))
meta.penup()
meta.goto(300, 300)
meta.pendown()
meta.goto(300, -300)
meta.hideturtle()
def program():
    global typ, wynik, nagralo, pieniadze
    #tworzenie zółwi
    cyan = turtle.Turtle()
    cyan.shape('turtle')
    cyan.color('cyan')
    cyan.pensize(7)
    cyan.penup()
    cyan.goto(-200, 200)
    cyan.pendown()

    red = turtle.Turtle()
    red.shape('turtle')
    red.color('red')
    red.pensize(7)
    red.penup()
    red.goto(-200, 100)
    red.pendown()

    purple = turtle.Turtle()
    purple.shape('turtle')
    purple.color('purple')
    purple.pensize(7)
    purple.penup()
    purple.goto(-200, 0)
    purple.pendown()

    blue = turtle.Turtle()
    blue.shape('turtle')
    blue.color('blue')
    blue.pensize(7)
    blue.penup()
    blue.goto(-200, -100)
    blue.pendown()

    green = turtle.Turtle()
    green.shape('turtle')
    green.color('green')
    green.pensize(7)
    green.penup()
    green.goto(-200, -200)
    green.pendown()


    #wypisuję zapytanie
    napis = turtle.Turtle()
    napis.color('black')
    napis.penup()
    napis.goto(-150, 350)
    napis.hideturtle()
    napis.pendown()
    napis.write('Obstaw który zółw wygra:', font=("Arial", 20, 'bold'))
    napis.penup()
    '''iksy = [-200, -100, 0, 100, 200]
    kolory = ['cyan']
    kolor = 0
    for i in iksy:
        napis.goto(i,320)
        napis.color'''
    napis.goto(-200, 320)
    napis.color('cyan')
    napis.write('1 - cyjanowy', font=("Arial", 10))
    napis.goto(-100, 320)
    napis.color('red')
    napis.write('2 - czerwony', font=("Arial", 10))
    napis.goto(0, 320)
    napis.color('purple')
    napis.write('3 - fioletowy', font=("Arial", 10))
    napis.goto(100, 320)
    napis.color('blue')
    napis.write('4 - niebieski', font=("Arial", 10))
    napis.goto(200, 320)
    napis.color('green')
    napis.write('5 - zielony', font=("Arial", 10))


    monety = turtle.Turtle()
    monety.penup()
    monety.hideturtle()
    def wznow():
        if pieniadze<-5:
            print("Za duże długi, nie możesz dalej grać...")
            turtle.bye()
        monety.clear()
        monety.goto(-450, 350)
        monety.write('Monet masz: ' + str(pieniadze), font=("Arial", 20))
    wznow()
    nagralo = False


    def poczatek():
    #odliczanie startowe
        odliczanie = turtle.Turtle()
        odliczanie.clear()
        odliczanie.hideturtle()
        odliczanie.color('white')
        odliczanie.penup()
        odliczanie.goto(-20, 270)
        odliczanie.hideturtle()

        for x in range(3):
            odliczanie.write(3-x, font=("Arial", 40, 'bold'))
            time.sleep(1)
            odliczanie.clear()
        odliczanie.goto(-40, 250)
        odliczanie.write("Start!", font=("Arial", 30, 'bold'))


        #sprawdzanie czy któryś z zółwi wygrał
        def sprawdz():
            global wynik
            if cyan.position()[0] >= 300:
                odliczanie.clear()
                odliczanie.goto(-60, 250)
                odliczanie.color('cyan')
                odliczanie.write('Wygrał CYJANOWY!', font=("Arial", 20, 'bold'))
                wynik = 1
                time.sleep(3)
                odliczanie.clear()
                return False
            elif red.position()[0] >= 300:
                odliczanie.clear()
                odliczanie.goto(-60, 250)
                odliczanie.color('red')
                odliczanie.write('Wygrał CZERWONY!', font=("Arial", 20, 'bold'))
                wynik = 2
                time.sleep(3)
                odliczanie.clear()
                return False
            elif purple.position()[0] >= 300:
                odliczanie.clear()
                odliczanie.goto(-60, 250)
                odliczanie.color('purple')
                odliczanie.write('Wygrał FIOLETOWY!', font=("Arial", 20, 'bold'))
                wynik = 3
                time.sleep(3)
                odliczanie.clear()
                return False
            elif blue.position()[0] >= 300:
                odliczanie.clear()
                odliczanie.goto(-60, 250)
                odliczanie.color('blue')
                odliczanie.write('Wygrał NIEBIESKI!', font=("Arial", 20, 'bold'))
                wynik = 4
                time.sleep(3)
                odliczanie.clear()
                return False
            elif green.position()[0] >= 300:
                odliczanie.clear()
                odliczanie.goto(-60, 250)
                odliczanie.color('green')
                odliczanie.write('Wygrał ZIELONY!', font=("Arial", 20, 'bold'))
                wynik = 5
                time.sleep(3)
                odliczanie.clear()
                return False
            else:
                return True

        def sprawdz2():
            if (cyan.position()[0] >= 300 or red.position()[0] >= 300 or purple.position()[0] >= 300 or blue.position()[0] >= 300 or green.position()[0] >= 300):
                return False
            else:
                return True

        kolejnosc = []
        zolwie = ["cyan", "red", "purple", "blue", "green"]
        for x in range(5, 0, -1):
            losowa = random.randint(0, x - 1)
            kolejnosc.append(zolwie[losowa])
            zolwie.pop(losowa)

        while sprawdz2():
            for x in range(5):
                if kolejnosc[x] == "cyan":
                    if random.randint(0,400)==1:
                        cyan.right(180)
                        cyan.forward(random.randint(0,30))
                    else:
                        cyan.forward(random.randint(0, 70))
                        if not sprawdz(): break
                elif kolejnosc[x] == "red":
                    if random.randint(0,400)==1:
                        red.right(180)
                        red.forward(random.randint(0,30))
                    else:
                        red.forward(random.randint(0, 70))
                        if not sprawdz(): break
                elif kolejnosc[x] == "purple":
                    if random.randint(0,400)==1:
                        purple.right(180)
                        purple.forward(random.randint(0,30))
                    else:
                        purple.forward(random.randint(0, 70))
                        if not sprawdz(): break
                elif kolejnosc[x] == "blue":
                    if random.randint(0,400)==1:
                        blue.right(180)
                        blue.forward(random.randint(0,30))
                    else:
                        blue.forward(random.randint(0, 70))
                        if not sprawdz(): break
                elif kolejnosc[x] == "green":
                    if random.randint(0, 400) == 1:
                        green.right(180)
                        green.forward(random.randint(0, 30))
                    else:
                        green.forward(random.randint(0, 70))
                        if not sprawdz(): break
        global typ, wynik, nagralo
        if typ == wynik:
            global pieniadze
            odliczanie.goto(-160, 250)
            odliczanie.color('black')
            odliczanie.write('Udało ci się zgadnąć wygranego!(wygrana: obstawione monety x3)', font=("Arial", 15, 'bold'))
            pieniadze+=3
            wznow()
            time.sleep(2)
        else:
            odliczanie.goto(-160, 250)
            odliczanie.color('black')
            odliczanie.write('Nie udało ci się zgadnąć wygranego!', font=("Arial", 15, 'bold'))
            time.sleep(2)
        odliczanie.clear()
        cyan.clear()
        blue.clear()
        red.clear()
        green.clear()
        purple.clear()

        cyan.hideturtle()
        blue.hideturtle()
        red.hideturtle()
        green.hideturtle()
        purple.hideturtle()

        napis.clear()
        monety.clear()
        program()

    def wcisnieto(a):
        global nagralo
        if not nagralo:
            global pieniadze, typ
            nagralo=True
            napis.clear()
            napis.penup()
            napis.goto(-150, 350)
            typ = a
            if(a==1):
                napis.color('cyan')
                napis.write('Stawiasz na cyjanowego', font=("Arial", 20, 'bold'))
            elif(a==2):
                napis.color('red')
                napis.write('Stawiasz na czerwonego', font=("Arial", 20, 'bold'))
            elif(a==3):
                napis.color('purple')
                napis.write('Stawiasz na fioletowego', font=("Arial", 20, 'bold'))
            elif(a==4):
                napis.color('blue')
                napis.write('Stawiasz na niebieskiego', font=("Arial", 20, 'bold'))
            else:
                napis.color('green')
                napis.write('Stawiasz na zielonego', font=("Arial", 20, 'bold'))
            pieniadze-=1
            wznow()
            poczatek()

    def wcisnieto_1():
        wcisnieto(1)
    def wcisnieto_2():
        wcisnieto(2)
    def wcisnieto_3():
        wcisnieto(3)
    def wcisnieto_4():
        wcisnieto(4)
    def wcisnieto_5():
        wcisnieto(5)

    turtle.onkey(wcisnieto_1, '1')
    turtle.onkey(wcisnieto_2, '2')
    turtle.onkey(wcisnieto_3, '3')
    turtle.onkey(wcisnieto_4, '4')
    turtle.onkey(wcisnieto_5, '5')

    turtle.listen()
    turtle.mainloop()
program()