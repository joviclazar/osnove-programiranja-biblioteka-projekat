import datetime
import meni
import projekat
import reg_korisnika
import termini_f
import karte_f

def upis_projekcija():
    projekcije_fajl = open("projekcije.txt", "w", encoding="utf-8")
    for projekcija in projekat.projekcije:
        linija_za_pisanje = "|".join(projekcija) + "\n"
        projekcije_fajl.write(linija_za_pisanje)
    projekcije_fajl.close()
    return None

def meni_pretrage_termina():
    opcija = input("[1] Pretraga po filmovima\n"
                   "[2] Pretraga po salama\n"
                   "[3] Pretraga po datumu\n"
                   "[4] Pretraga po početku projekcije\n"
                   "[5] Pretraga po kraju projekcije\n"
                   "[0] Povratak na početni meni\n"
                   "Izaberite željeni kriterijum pretrage: ")
    if opcija == "1":
        pretraga_po_filmovima()
    elif opcija == "2":
        pretraga_po_salama()
    elif opcija == "3":
        pretraga_po_datumu()
    elif opcija == "4":
        pretraga_po_pocetku()
    elif opcija == "5":
        pretraga_po_kraju()
    elif opcija == "0":
        meni.povratak_na_pocetni_meni()
    else:
        print("Morate uneti odgovarajuću opciju!")
        meni_pretrage_termina()

def meni_nakon_ispisa_projekcija():
    opcija = input("[1] Pretraga termina projekcija\n"
                   "[2] Rezervacija karte\n"
                   "[0] Povratak na početni meni\n"
                   "Odaberite jednu od opcija: ")
    if opcija == "1":
        meni_pretrage_termina()
    elif opcija == "2":
        if reg_korisnika.trenutni_korisnik == []:
            print("Morate se ulogovati da biste rezervisali kartu!\n"
                  "Ako nemate nalog, možete se registrovati na početnom meniju.")
            meni_nakon_ispisa_projekcija()
        else:
            karte_f.rezervacija_karte_kupac()
    elif opcija == "0":
        meni.povratak_na_pocetni_meni()
    else:
        print("Morate uneti odgovarajuću opciju!")
        meni_nakon_ispisa_projekcija()

def ispis_termina_projekcija(odgovarajuce_projekcije):
    if odgovarajuce_projekcije == []:
        print("Nije pronađena nijedna projekcija koja odgovara Vašoj pretrazi!")
        meni_pretrage_termina()
    odgovarajuci_termini = []
    for projekcija in odgovarajuce_projekcije:
        for termin in termini_f.postojeci_termini:
            if projekcija[0] == termin[0] and termin[3] == "V":
                odgovarajuci_termini.append(termin)
            else:
                pass
    print("{0:^16}|{1:^6}|{2:^13}|{3:^11}|{4:^30}|{5:^30}|{6:^18}"
          .format("Šifra termina","Sala", "Vreme početka", "Vreme kraja", "Datum projekcije",
                  "Naziv filma", "Osnovna cena karte"))
    for termin in odgovarajuci_termini:
        for linija in odgovarajuce_projekcije:
            if linija[0] == termin[0]:
                sifra = termin[0] + termin[1]
                sala = linija[1]
                vreme_p = linija[2]
                vreme_k = linija[3]
                datum = termin[2]
                naziv_filma = linija[5]
                cena_k = linija[6]
                print("{0:^16}|{1:^6}|{2:^13}|{3:^11}|{4:^30}|{5:^30}|{6:^18}"
                      .format(sifra,sala,vreme_p,vreme_k,datum,naziv_filma,cena_k))
    meni_nakon_ispisa_projekcija()

def pretraga_po_filmovima():
    odgovarajuce_projekcije = []
    ime_filma = input("Unesite ime filma čije projekcije želite da vidite: ")
    if ime_filma == "":
        meni_pretrage_termina()
    ime_filma = ime_filma.lower()
    for projekcija in projekat.projekcije:
        if ime_filma in projekcija[5].lower():
            odgovarajuce_projekcije.append(projekcija)
    ispis_termina_projekcija(odgovarajuce_projekcije)

def pretraga_po_salama():
    odgovarajuce_projekcije = []
    opcija = input("[1] Sala1\n"
                   "[2] Sala2\n"
                   "[3] Sala3\n"
                   "Izaberite jednu od sala: ")
    sala = ""
    if opcija == "":
        meni_pretrage_termina()
    elif opcija == "1":
        sala = "S1"
    elif opcija == "2":
        sala = "S2"
    elif opcija == "3":
        sala = "S3"
    else:
        print("Morate uneti odgovarajuću opciju!")
        pretraga_po_salama()
    for projekcija in projekat.projekcije:
        if sala == projekcija[1]:
            odgovarajuce_projekcije.append(projekcija)
    ispis_termina_projekcija(odgovarajuce_projekcije)

def pretraga_po_datumu():
    odgovarajuce_projekcije = []
    datum_format = '%d.%m.%Y.'
    datum_str = input("Unesite željeni datum(dd.mm.yy.): ")
    if datum_str == "":
        meni_pretrage_termina()
    else:
        pass
    try:
        datum = datetime.datetime.strptime(datum_str, datum_format)
    except ValueError:
        print("Morate uneti datum u odgovarajućem formatu(dd.mm.yy.)!")
        pretraga_po_datumu()
    sifre = []
    odgovarajuci_termini = []
    for termin in termini_f.postojeci_termini:
        if termin[2] == datum_str:
            odgovarajuci_termini.append(termin)
            sifre.append(termin[0])
        else:
            pass
    for projekcija in projekat.projekcije:
        if projekcija[0] in sifre:
            odgovarajuce_projekcije.append(projekcija)
        else:
            pass
    ispis_termina_projekcija_po_datumu(odgovarajuce_projekcije, odgovarajuci_termini, datum_str)

def ispis_termina_projekcija_po_datumu(odgovarajuce_projekcije, odgovarajuci_termini, datum_str):
    if odgovarajuce_projekcije == [] or odgovarajuci_termini == []:
        print("Nije pronađena nijedna projekcija koja odgovara Vašoj pretrazi!")
        meni_pretrage_termina()
    else:
        pass
    odgovarajuci_termini_za_ispis = []
    for projekcija in odgovarajuce_projekcije:
        for termin in odgovarajuci_termini:
            if projekcija[0] == termin[0]:
                if termin[3] == "V":
                    if termin[2] == datum_str:
                        odgovarajuci_termini_za_ispis.append(termin)
                    else:
                        pass
                else:
                    pass
            else:
                pass
    print("{0:^16}|{1:^6}|{2:^13}|{3:^11}|{4:^30}|{5:^30}|{6:^18}"
          .format("Šifra termina","Sala", "Vreme početka", "Vreme kraja", "Datum projekcije",
                  "Naziv filma", "Osnovna cena karte"))
    a = -1
    for linija in odgovarajuce_projekcije:
        a += 1
        sifra = odgovarajuci_termini_za_ispis[a][0] + odgovarajuci_termini_za_ispis[a][1]
        sala = linija[1]
        vreme_p = linija[2]
        vreme_k = linija[3]
        datum = odgovarajuci_termini_za_ispis[a][2]
        naziv_filma = linija[5]
        cena_k = linija[6]
        print("{0:^16}|{1:^6}|{2:^13}|{3:^11}|{4:^30}|{5:^30}|{6:^18}"
              .format(sifra,sala,vreme_p,vreme_k,datum,naziv_filma,cena_k))
    meni_nakon_ispisa_projekcija()

def pretraga_po_pocetku():
    odgovarajuce_projekcije = []
    pocetak = input("Unesite željeno vreme početka projekcije.\n"
                    "Sve projekcije počinju u xx:00 ili xx:30: ")
    for projekcija in projekat.projekcije:
        if pocetak == projekcija[2].lower():
            odgovarajuce_projekcije.append(projekcija)
    ispis_termina_projekcija(odgovarajuce_projekcije)

def pretraga_po_kraju():
    odgovarajuce_projekcije = []
    kraj = input("Unesite željeno vreme kraja projekcije.\n"
                    "Sve projekcije se završavaju u xx:00 ili xx:30: ")
    for projekcija in projekat.projekcije:
        if kraj == projekcija[3].lower():
            odgovarajuce_projekcije.append(projekcija)
    ispis_termina_projekcija(odgovarajuce_projekcije)