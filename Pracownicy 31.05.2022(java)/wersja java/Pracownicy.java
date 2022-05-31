public class Pracownicy {
    public String imie, nazwisko, jest;
    public int wiek, kwota_brutto, ID;
    public float netto;

    public Pracownicy(int id, String imie7, String nazwisko7, int wiek7, int kwota_brutto7){
        ID = id;
        imie = imie7;
        nazwisko = nazwisko7;
        wiek = wiek7;
        kwota_brutto = kwota_brutto7;
    }
    public void przedstaw_sie(){
        System.out.println("Hej, jestem "+imie+" "+nazwisko+"\nMam "+wiek+" lat\nI dostaje "+kwota_brutto+"zl brutto\nJestem Pracownikiem");
    }
}