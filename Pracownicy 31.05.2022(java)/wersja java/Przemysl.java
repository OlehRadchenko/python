public class Przemysl extends Pracownicy{
    public float sila;
    public void przedstaw_sie(){
        netto = (float) (kwota_brutto * 0.1 * sila - wiek*10);
        System.out.println("|\t\t\t" + ID + "\t\t\t|\t\t\t" + imie + "\t\t\t|\t\t\t" + nazwisko + "\t\t\t|\t\t\t" + wiek + "\t\t\t|\t\t\t"+jest+"\t\t\t|\t\t\t" + Math.round(netto) + "\t\t\t|");
    }
    public Przemysl(int id, String imie, String nazwisko, int wiek, int kwota_brutto, float sila) {
        super(id, imie, nazwisko, wiek, kwota_brutto);
        this.sila = sila;
        jest = "Przemysl";
    }
}