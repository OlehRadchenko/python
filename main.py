from random import seed
from random import randint

f = open("XD.txt", "x")
f.write("The English Wikipedia is the English-language edition of Wikipedia, an online encyclopedia."
        " It was founded on 15 January 2001 as Wikipedia's first edition and, as of October 2021,"
        " has the most articles of any edition, at 6,460,320. As of March 2022, 11% of"
        " articles in all Wikipedias belong to the English-language edition;"
        "this share was more than 50% in 2003. The edition's one-billionth edit was made on 13 January 2021.")
f.close()

f = open("XD.txt", "r")
print(f.read())
f.close()

f = open("XD.txt", "a")
for x in range(10):
    f.write("\nXD")
f.close()

f = open("XD.txt", "r")
print(f.read())
f.close()

f = open("XD.txt", "r")
files = f.read()
print("Liter w pliku:", len(files))
f.close()

losowe = ["Krol","a","ale","zeby","gdyby","moze","jezeli","nie","jednak","Tetris","gdy","zagral","wygral","przegral","Paryz","marzec","grudzien","zjadl","koza","kolacja","klawiatura","dom","monitor","pies","wiek","i","zaatakowal","Linux","zabil","uzyskal"]
seed(1)
f = open("XD.txt", "a")
y = int(input())
f.write("\n")
for x in range(y):
    liczba = randint(0, 29)
    f.write(losowe[liczba])
    f.write(" ")
    if(x % 10 == 0 and x != 0):
        f.write("\n")
f.close()

# f = open("XD.txt", "a")
# fb = open("X2", "r")
# tab[200] = fb.split()
# f.close()