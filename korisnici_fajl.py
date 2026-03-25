import meni
import reg_korisnika

global korisnici
korisnici = []
korisnici_fajl = open("registrovanikorisnici.txt", "r", encoding="utf-8")
for linija in korisnici_fajl.readlines():
    linija_razdvojena = linija.split("|")
    korisnici.append(linija_razdvojena)
korisnici_fajl.close()

def upis_korisnika(korisnik_dodat):
    korisnici_upis = []
    for korisnik_razdvojeno in korisnici:
        korisnik_spojeno = "|".join(korisnik_razdvojeno)
        korisnici_upis.append(korisnik_spojeno)
    korisnici_upis.append(korisnik_dodat)

    korisnici_fajl = open("registrovanikorisnici.txt", "w", encoding="utf-8")
    for korisnik in korisnici_upis:
        korisnici_fajl.write(korisnik)
    korisnici_fajl.close()