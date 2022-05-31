import java.util.Scanner;

public class main {
    public static int licznik = 0;
    public static int licznik2 = 0;
    public static int i = 0;
    public static int[] zakaz = new int[100];
    public static Pracownicy nowy[] = new Pracownicy[100];
    public static Scanner scan = new Scanner(System.in);
    public static int wybor = 0;
    public static int wybor2 = 0;
    public static String im, naz;
    public static int wi, bru, inte, pro, si;

    public static void main(String[] args) {
        System.out.println("Witaj w tutaj 'w'\nCo chcesz zrobic?");
        poczatek();
    }
    public static void poczatek() {
        System.out.println("1.Dodac\n2.Edytowac\n3.Usunac\n4.Wyswietlic\n5.Wyjsc");
        try{
            wybor = scan.nextInt();
            if (wybor<1 || wybor>5){
                System.out.println("Nie ladnie wpisywac inne liczby ;<\nTeraz zaczynasz od nowa ;c");
                zakoncz();
            }
        } catch (Exception e) {
            System.out.println("Nie tak latwo, to nie c++ ;3\nTeraz zaczynasz od nowa ;c");
            zakoncz();
        }
        switch (wybor){
            case 1:
                dodaj();
                break;
            case 2:
                edytuj();
                break;
            case 3:
                usun();
                break;
            case 4:
                wyswietl();
                break;
            case 5:
                zakoncz();
                break;
        }
        poczatek();
    }

    public static void dodaj(){
        System.out.println("Kogo chcesz dodac?\n1.Rolnika\n2.Uslugi\n3.Przemysl");
        try{
            wybor = scan.nextInt();
            licznik++;
            i=licznik-1;
            if (wybor<1 || wybor>3){
                System.out.println("Nie ladnie wpisywac inne liczby ;<\nTeraz zaczynasz od nowa ;c");
                zakoncz();
            }
        } catch (Exception e) {
            System.out.println("Nie tak latwo, to nie c++ ;3\nTeraz zaczynasz od nowa ;c");
            zakoncz();
        }
        try {
            switch (wybor) {
                case 1:
                    dodaj_r(i);
                    break;
                case 2:
                    dodaj_u(i);
                    break;
                case 3:
                    dodaj_p(i);
                    break;
            }
        }catch (Exception e){
            System.out.println("Nie ladnie tak oszukiwac ;c \nZaczynasz od nowa");
            zakoncz();
        }
    }
    public static void dodaj_r(int i){
        System.out.print("");
        im = scan.nextLine();
        System.out.println("Podaj imie nowego rolnika: ");
        im = scan.nextLine();
        System.out.println("Podaj jego nazwisko: ");
        naz = scan.nextLine();
        System.out.println("Ile ma lat: ");
        wi = scan.nextInt();
        System.out.println("Jakie ma wynagrodzenie(brutto): ");
        bru = scan.nextInt();
        nowy[i] = new Rolnik(i + 1, im, naz, wi, bru);
    }
    public static void dodaj_u(int i){
        System.out.print("");
        im = scan.nextLine();
        System.out.println("Podaj imie nowego pracownika w uslugach: ");
        im = scan.nextLine();
        System.out.println("Podaj jego nazwisko: ");
        naz = scan.nextLine();
        System.out.println("Ile ma lat: ");
        wi = scan.nextInt();
        System.out.println("Jakie ma wynagrodzenie(brutto): ");
        bru = scan.nextInt();
        System.out.println("Jaka posiada inteligencje: ");
        inte = scan.nextInt();
        System.out.println("Jaka ma prowizje(od 5 do 20): ");
        pro = scan.nextInt();
        if (pro>=5 && pro<=20) {
            nowy[i] = new Uslugi(i+1, im, naz, wi, bru, inte, pro);
        }
        else {
            System.out.println("Minimalna prowizja to 5,a maksymalna to 20, powtorz probe, bo wpisales zla liczbe ;c");
            dodaj_u(i);
        }

    }
    public static void dodaj_p(int i){
        System.out.print("");
        im = scan.nextLine();
        System.out.println("Podaj imie nowego pracownika w przemysle: ");
        im = scan.nextLine();
        System.out.println("Podaj jego nazwisko: ");
        naz = scan.nextLine();
        System.out.println("Ile ma lat: ");
        wi = scan.nextInt();
        System.out.println("Jakie ma wynagrodzenie(brutto): ");
        bru = scan.nextInt();
        System.out.println("Jaka ma sile: ");
        si = scan.nextInt();
        nowy[i] = new Przemysl(i+1, im, naz, wi, bru, si);
    }

    public static void edytuj(){
        System.out.println("Kogo chcesz zmodyfikowac:\n|\t\t\tID\t\t\t|\t\t\tIMIE\t\t\t|\t\t\tNAZWISKO\t\t\t|\t\t\tWIEK\t\t\t|\t\t\tKIM JEST\t\t\t|\t\t\tNETTO\t\t\t|");
        for (int i=0; i<licznik; i++){
            try {
                nowy[i].przedstaw_sie();
            }catch (Exception e){

            }
        }
        System.out.print("Wpowadz jego ID: ");
        try {
            wybor = scan.nextInt();
        }catch (Exception e){
            System.out.println("Nie tak latwo, to nie c++ ;3\nTeraz zaczynasz od nowa ;c");
            zakoncz();
        }
        if (wybor > licznik || wybor <= 0 || wybor == zakaz[0] || wybor == zakaz[1] || wybor == zakaz[2] || wybor == zakaz[3] || wybor == zakaz[4] || wybor == zakaz[5]) {
            System.out.println("Nie ma takiego ID ;c\nSprobuj jeszcze raz");
            edytuj();
        }else {
            System.out.println("Kim bedzie pracownik: \n1.Rolnik\n2.Uslugi\n3.Przemysl");
            try {
                wybor2 = scan.nextInt();
                if (wybor2 < 1 || wybor2 > 3) {
                    System.out.println("Nie ladnie wpisywac inne liczby ;<\nTeraz zaczynasz od nowa ;c");
                    zakoncz();
                }
            } catch (Exception e) {
                System.out.println("Nie tak latwo, to nie c++ ;3\nTeraz zaczynasz od nowa ;c");
                zakoncz();
            }
            switch (wybor2) {
                case 1:
                    dodaj_r(wybor - 1);
                    break;
                case 2:
                    dodaj_u(wybor - 1);
                    break;
                case 3:
                    dodaj_p(wybor - 1);
                    break;
            }
            System.out.println("edytujem");
            poczatek();
        }
    }
    public static void usun(){
        System.out.println("Kogo chcesz usunac:\n|\t\t\tID\t\t\t|\t\t\tIMIE\t\t\t|\t\t\tNAZWISKO\t\t\t|\t\t\tWIEK\t\t\t|\t\t\tKIM JEST\t\t\t|\t\t\tNETTO\t\t\t|");
        for (int i=0; i<licznik; i++){
            try {
                nowy[i].przedstaw_sie();
            }catch (Exception e){

            }
        }
        System.out.print("Wpowadz jego ID: ");
        try {
            wybor = scan.nextInt();
        }catch (Exception e){
            System.out.println("Nie tak latwo, to nie c++ ;3\nTeraz zaczynasz od nowa ;c");
            zakoncz();
        }
            if (wybor > licznik || wybor <= 0 || wybor == zakaz[0] || wybor == zakaz[1] || wybor == zakaz[2] || wybor == zakaz[3] || wybor == zakaz[4] || wybor == zakaz[5]) {
                System.out.println("Nie ma takiego ID ;c\nSprobuj jeszcze raz");
                usun();
            }else{
                nowy[wybor - 1] = null;
                zakaz[licznik2] = wybor;
                licznik2++;
            }
        /*nowy[wybor - 1] = null;
        zakaz[licznik2] = wybor;
        licznik2++;
        System.out.println("usuwam");*/
    }
    public static void wyswietl(){
        System.out.println("Pracownicy:\n|\t\t\tID\t\t\t|\t\t\tIMIE\t\t\t|\t\t\tNAZWISKO\t\t\t|\t\t\tWIEK\t\t\t|\t\t\tKIM JEST\t\t\t|\t\t\tNETTO\t\t\t|");
        for (int i=0; i<licznik; i++){
            try {
                nowy[i].przedstaw_sie();
            }catch (Exception e){

            }
        }
        /*System.out.println("wyswietlam");*/
    }
    public static void zakoncz(){
        System.out.println("bb");
        System.exit(66);
    }
}