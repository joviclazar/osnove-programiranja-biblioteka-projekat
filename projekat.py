import meni
import termini_f


global korisnici
def ucitavanje_korisnika():
    global korisnici
    korisnici = []
    korisnici_fajl = open("registrovanikorisnici.txt", "r", encoding="utf-8")
    for linija in korisnici_fajl.readlines():
        linija_razdvojena = linija.split("|")
        korisnici.append(linija_razdvojena)
    korisnici_fajl.close()


global linije_filmova
def ucitivanje_filmova():
    filmovi = open("filmovi.txt", "r", encoding="utf-8")
    global linije_filmova
    linije_filmova = []
    for linija in filmovi.readlines():
        linija_razdvojeno = linija[:-1].split("|")
        linije_filmova.append(linija_razdvojeno)
    filmovi.close()


global opisi_filmova
def ucitavanje_opisa_filmova():
    global opisi_filmova
    opisi_filmova = []
    opisi_filmova_fajl = open("opisi_filmova.txt", "r", encoding="utf-8")
    for linija in opisi_filmova_fajl.readlines():
        opisi_filmova.append(linija)
    opisi_filmova_fajl.close()


global sale
def ucitavanje_sala():
    global sale
    sale = []
    sale_fajl = open("sale.txt", "r", encoding="utf-8")
    for sala in sale_fajl:
        sala_razdvojeno = sala.split("|")
        sifra_sale = sala_razdvojeno[0]
        redovi = []
        for i in range(int(sala_razdvojeno[1])):
            redovi.append(str(i+1) + "." + sala_razdvojeno[2][:-1])
        konacna_sala_za_upis = []
        konacna_sala_za_upis.append(sifra_sale)
        konacna_sala_za_upis.append("|".join(redovi))
        sale.append(konacna_sala_za_upis)
    sale_fajl.close()


global projekcije
def ucitavanje_projekcija():
    global projekcije
    projekcije = []
    projekcije_fajl = open("projekcije.txt", "r", encoding="utf-8")
    for projekcija in projekcije_fajl.readlines():
        projekcija_razdvojeno = projekcija[:-1].split("|")
        projekcije.append(projekcija_razdvojeno)
    projekcije_fajl.close()


global karte
def ucitavanje_karta():
    global karte
    karte = []
    karte_fajl = open("karte.txt", "r", encoding="utf-8")
    for karta in karte_fajl.readlines():
        karta_lista = karta[:-1].split("|")
        karte.append(karta_lista)
    karte_fajl.close()

def ucitavanje_svih_entita():       #ucitavanje svih entiteta
    ucitavanje_karta()
    ucitavanje_projekcija()
    ucitavanje_sala()
    ucitavanje_korisnika()
    ucitavanje_opisa_filmova()
    ucitivanje_filmova()
    termini_f.kreiranje_termina()

ucitavanje_svih_entita()

if __name__ == "__main__":
    print("{0:^33}".format("Bioskop"))
    print("{0:^34}".format("Dobro došli!"))
    print("-" * 35)
    meni.meni1()