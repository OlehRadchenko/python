public class Uslugi extends Pracownicy{
    public float inteligencja, prowizja; //prowizja: 5-20 limit
    public void przedstaw_sie() {
        netto = (float) (kwota_brutto * 0.2 * inteligencja + (kwota_brutto * prowizja/100));
        System.out.println("|\t\t\t" + ID + "\t\t\t|\t\t\t" + imie + "\t\t\t|\t\t\t" + nazwisko + "\t\t\t|\t\t\t" + wiek + "\t\t\t|\t\t\t"+jest+"\t\t\t|\t\t\t" + Math.round(netto) + "\t\t\t|");
    }
    public Uslugi(int id, String imie, String nazwisko, int wiek, int kwota_brutto, float inteligencja, float prowizja) {
        super(id, imie, nazwisko, wiek, kwota_brutto);
        this.inteligencja = inteligencja;
        this.prowizja = prowizja;
        jest = "Uslugi";
    }
}