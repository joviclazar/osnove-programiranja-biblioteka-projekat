import karte_f
import pretraga_filmova
import reg_korisnika
import projekcije_f
import izvestaji_f
import izmena_karte_f
import rukovanje_projekcijama_f


def povratak_na_pocetni_meni():         #povratak na odgovarajući početni meni
    if reg_korisnika.trenutni_korisnik == []:
        meni_neregistrovanog()
    else:
        if reg_korisnika.trenutni_korisnik[4][0] == "k":
            meni_kupca()
        elif reg_korisnika.trenutni_korisnik[4][0] == "m":
            meni_menadzera()
        elif reg_korisnika.trenutni_korisnik[4][0] == "p":
            meni_prodavca()


def meni1():
    global reg_n

    print("[N] Neregistrovan korisnik \n"
          "[L] Logovanje\n"
          "[E] Izlaz")

    reg_n = input("Izaberite opciju: ")

    reg_n = reg_n.lower()

    if reg_n == "n":
        meni2()
    elif reg_n == "l":
        reg_korisnika.prijava()
    elif reg_n == "e":
        print("Hvala na poseti!")
        exit()
    else:
        print("Molimo Vas, unesite odgovarajuć unos!")
        meni1()


def meni2():
        x = input("Da li želite da se registrujete? \n"
                  "[D] Da \n"
                  "[N] Ne \n"
                  "Unesite opciju: ")
        x = x.lower()
        if x == "d":
            print("Započinjete registrovanje.\n"
                  "Prazan unos u bilo kom trenutku za izlaz. ")
            reg_korisnika.registracija_kupaca()
        elif x == "n":
            print("Nastaljate kao neregistrovan korisnik.")
            reg_korisnika.trenutni_korisnik = []
            meni_neregistrovanog()
        else:
            print("Unesite odgovorajuću opciju!")
            meni2()


def meni_neregistrovanog():
    print("[1] Pregled dostupnih filmova\n"
          "[2] Pretraga filmova\n"
          "[3] Pretraga termina projekcija\n"
          "[4] Povratak na početni meni za logovanje\n"
          "[0] Izlaz")
    opcija = input("Odaberite opciju: ")
    if opcija == "1":
        pretraga_filmova.ispis_filmova()
    elif opcija == "2":
        pretraga_filmova.pretraga_filmova()
    elif opcija == "3":
        projekcije_f.meni_pretrage_termina()
    elif opcija == "4":
        meni1()
    elif opcija == "0":
        print("Hvala na poseti!")
        exit()
    else:
        print("Unesite odgovorajuću opciju!")
        meni_neregistrovanog()


def meni_prodavca():
    print("[1] Pregled dostupnih filmova \n"
          "[2] Pretraga filmova \n"
          "[3] Pretraga termina projekcija\n"
          "[4] Karte\n"
          "[5] Izmena ličnih podataka\n"
          "[6] Odjava \n"
          "[0] Izlaz")
    opcija = input("Odaberite opciju: ")
    if opcija == "1":
        pretraga_filmova.ispis_filmova()
    elif opcija == "2":
        pretraga_filmova.pretraga_filmova()
    elif opcija == "5":
        reg_korisnika.izmena_licnih_podataka()
    elif opcija == "3":
        projekcije_f.meni_pretrage_termina()
    elif opcija == "6":
        meni1()
    elif opcija == "4":
        meni_karte_prodavac()
    elif opcija == "0":
        print("Hvala na poseti!")
        exit()
    else:
        print("Unesite odgovorajuću opciju!")
        meni_prodavca()


def meni_menadzera():
    print("[1] Pregled dostupnih filmova\n"
          "[2] Pretraga filmova\n"
          "[3] Pretraga termina projekcija\n"
          "[4] Izmena ličnih podataka\n"
          "[5] Registracija novih prodavaca/menadžera\n"
          "[6] Rukovanje filmovima\n"
          "[7] Rukovanje projekcijama\n"
          "[8] Izveštaji\n"
          "[9] Odjava \n"
          "[0] Izlaz")
    opcija = input("Odaberite opciju: ")
    if opcija == "1":
        pretraga_filmova.ispis_filmova()
    elif opcija == "2":
        pretraga_filmova.pretraga_filmova()
    elif opcija == "4":
        reg_korisnika.izmena_licnih_podataka()
    elif opcija == "3":
        projekcije_f.meni_pretrage_termina()
    elif opcija == "5":
        while True:
            x = input("Da li želite da registrujete novog \n"
                      "menadžera ili prodavca? \n"
                      "[M] Menadžera \n"
                      "[P] Prodavca \n"
                      "Odaberite opciju: ")
            x = x.lower()
            if x == "m":
                reg_korisnika.registracija_menadzera()
            elif x == "p":
                reg_korisnika.registracija_prodavaca()
            elif x == "":
                meni_menadzera()
            else:
                print("Morate uneti odgovarajuću opciju!\nPokušajte ponovo.")
    elif opcija == "6":
        rukovanje_filmovima()
    elif opcija == "7":
        rukovanje_projekcijama()
    elif opcija == "8":
        meni_izvestaja()
    elif opcija == "9":
        meni1()
    elif opcija == "0":
        print("Hvala na poseti!")
        exit()
    else:
        print("Unesite odgovorajuću opciju!")
        meni_menadzera()


def rukovanje_projekcijama():
    opcija = input("[1] Dodavanje projekcija\n"
                   "[2] Izmena projekcija\n"
                   "[3] Brisanje projekcija\n"
                   "[4] Ispis projekcija\n"
                   "[0] Natrag\n"
                   "Unesite odgovarajuću opciju: ")
    if opcija == "1":
        rukovanje_projekcijama_f.dodavanje_projekcija()
    elif opcija == "2":
        rukovanje_projekcijama_f.izmena_projekcija_meni()
    elif opcija == "3":
        rukovanje_projekcijama_f.brisanje_projekcija()
    elif opcija == "4":
        rukovanje_projekcijama_f.ispis_projekcija()
    elif opcija == "0":
        povratak_na_pocetni_meni()
    else:
        print("Morate uneti odgovarajuću opciju!\nPokušajte ponovo.")
        rukovanje_projekcijama()


def rukovanje_filmovima():
    opcija = input("[1] Dodavanje filmova\n"
                   "[2] Izmena filmova\n"
                   "[3] Brisanje filmova\n"
                   "[0] Natrag\n"
                   "Unesite odgovarajuću opciju:")
    if opcija == "1":
        pretraga_filmova.dodavanje_filmova()
    elif opcija == "2":
        pretraga_filmova.izmena_filmova()
    elif opcija == "3":
        pretraga_filmova.brisanje_filmova()
    elif opcija == "0":
        povratak_na_pocetni_meni()
    else:
        print("Unesite odgovarajuću opciju!\nPokušajte ponovo.")
        rukovanje_filmovima()


def meni_izvestaja():
    opcija = input("[1] Lista prodatih karata za odabran datum prodaje\n"
                   "[2] Lista prodatih karata za odabran datum termina bioskopske projekcije\n"
                   "[3] Lista prodatih karata za odabran datum prodaje i odabranog prodavca\n"
                   "[4] Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) prodaje\n"
                   "[5] Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) održavanja projekcije\n"
                   "[6] Ukupan broj i ukupna cena prodatih karata za zadati film u svim projekcijama\n"
                   "[7] Ukupan broj i ukupna cena prodaith karata za izabran dan prodaje i odabranog prodavca\n"
                   "[8] Ukupan broj i ukupna cena prodatih karata po prodavcima u poslednjih 30 dana\n"
                   "[0] Natrag\n"
                   "Unesite odgovarajuću opciju: ")
    if opcija == "1":
        izvestaji_f.izvestaj_datum_prodaje()
    elif opcija == "2":
        izvestaji_f.izvestaj_datum_termina()
    elif opcija == "3":
        izvestaji_f.izvestaj_datum_prodaje_prodavac()
    elif opcija == "4":
        izvestaji_f.izvestaj_broj_cena_dan_prodaje()
    elif opcija == "5":
        izvestaji_f.izvestaj_broj_cena_dan_projekcije()
    elif opcija == "6":
        izvestaji_f.izvestaj_broj_cena_film()
    elif opcija == "7":
        izvestaji_f.izvestaj_broj_cena_dan_prodaje_prodavac()
    elif opcija == "8":
        izvestaji_f.izvestaj_broj_cena_po_prodavcima()
    elif opcija == "0":
        povratak_na_pocetni_meni()
    else:
        print("Morate uneti odgovarajuću opciju!")
        meni_izvestaja()


def meni_kupca():
    print("[1] Pregled dostupnih filmova \n"
          "[2] Pretraga filmova \n"
          "[3] Pretraga termina projekcija \n"
          "[4] Karte\n"
          "[5] Izmena ličnih podataka\n"
          "[6] Odjava \n"
          "[0] Izlaz")
    opcija = input("Odaberite opciju: ")
    if opcija == "1":
        pretraga_filmova.ispis_filmova()
    elif opcija == "2":
        pretraga_filmova.pretraga_filmova()
    elif opcija == "5":
        reg_korisnika.izmena_licnih_podataka()
    elif opcija == "3":
        projekcije_f.meni_pretrage_termina()
    elif opcija == "4":
        meni_karte_kupac()
    elif opcija == "6":
        meni1()
    elif opcija == "0":
        print("Hvala na poseti!")
        exit()
    else:
        print("Unesite odgovorajuću opciju!")
        meni_kupca()


def meni_karte_kupac():
    opcija = input("[1] Rezervacija karata\n"
                   "[2] Pregled rezervisanih karata\n"
                   "[3] Poništavanje rezervacija\n"
                   "[0] Natrag\n"
                   "Unesite željenu opciju: ")
    if opcija == "1":
        karte_f.rezervacija_karte_kupac()
    elif opcija == "2":
        karte_f.pregled_rezervisanih_karata_kupac()
    elif opcija == "3":
        karte_f.ponistavanje_rezervacija_kupac()
    elif opcija == "0":
        povratak_na_pocetni_meni()
    else:
        print("Morate uneti odgovarajuću opciju!")
        meni_karte_kupac()


global tip_karte
def meni_karte_prodavac():
    opcija = input("[1] Rezervacija karata\n"
                   "[2] Pregled karata\n"
                   "[3] Poništavanje rezervisanih/prodatih karata\n"
                   "[4] Pretraga karata\n"
                   "[5] Direktna prodaja karata\n"
                   "[6] Prodaja rezervisane karte\n"
                   "[7] Izmena karte\n"
                   "[0] Natrag\n"
                   "Unesite željenu opciju: ")
    if opcija == "1":
        global tip_karte      #promenjiva koja odredjuje da li se karta kupuje ili rezerviše
        tip_karte = "R"
        karte_f.rezervacija_karte_prodavac()
    elif opcija == "2":
        karte_f.pregled_rezervisanih_karata_prodavac()
    elif opcija == "3":
        karte_f.ponistavanje_rezervacija_prodavac()
    elif opcija == "4":
        meni_pretrage_karata_prodavac()
    elif opcija == "5":
        tip_karte = "K"
        karte_f.rezervacija_karte_prodavac()
    elif opcija == "6":
        karte_f.prodaja_rezervisane_karte()
    elif opcija == "7":
        izmena_karte_f.biranje_karte()
    elif opcija == "0":
        povratak_na_pocetni_meni()
    else:
        print("Morate uneti odgovarajuću opciju!")
        meni_karte_prodavac()


def meni_pretrage_karata_prodavac():
    opcija = input("[1] Šifra projekcije\n"
                   "[2] Ime kupca\n"
                   "[3] Datum rezervacije karte\n"
                   "[4] Vreme početka projekcije\n"
                   "[5] Vreme kraja projekcije\n"
                   "[6] Tip karte\n"
                   "[0] Povratak\n"
                   "Unesite željenu opciju: ")
    if opcija == "1":
        karte_f.pretraga_karata_po_sifri()
    elif opcija == "2":
        karte_f.pretraga_karata_po_imenu()
    elif opcija == "3":
        karte_f.pretraga_karata_po_datumu()
    elif opcija == "4":
        karte_f.pretraga_karata_po_vremenu_pocetka()
    elif opcija == "5":
        karte_f.pretraga_karata_po_vremenu_kraja()
    elif opcija == "6":
        karte_f.pretraga_karata_po_tipu_karte()
    elif opcija == "0":
        meni_karte_prodavac()
    else:
        print("Morate uneti odgovarajuću opciju!")
        meni_pretrage_karata_prodavac()