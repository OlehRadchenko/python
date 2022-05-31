public class Rolnik extends Pracownicy{
    public void przedstaw_sie(){
        netto = (float) (kwota_brutto - 0.23*kwota_brutto/1.23);
        System.out.println("|\t\t\t"+ID+"\t\t\t|\t\t\t"+imie+"\t\t\t|\t\t\t"+nazwisko+"\t\t\t|\t\t\t"+wiek+"\t\t\t|\t\t\t"+jest+"\t\t\t|\t\t\t"+Math.round(netto)+"\t\t\t|");
    }
    public Rolnik(int id, String imie, String nazwisko, int wiek, int kwota_brutto) {
        super(id, imie, nazwisko, wiek, kwota_brutto);
        jest = "Rolnik";
    }
}