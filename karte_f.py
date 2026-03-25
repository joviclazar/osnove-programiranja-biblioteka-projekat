import dodatno_f
import meni
import projekat
import projekcije_f
import reg_korisnika
import termini_f
import datetime

def rezervacija_karte_kupac():
    korisnik = reg_korisnika.trenutni_korisnik[2]
    kartica_lojalnosti = dodatno_f.provera_lojalnosti(korisnik)
    zeljena_sifra = input("Unesite šifru željenog termina(npr. 1111AA): ")
    if zeljena_sifra == "":
        meni.meni_karte_kupac()
    else:
        pass
    zeljena_sifra = zeljena_sifra.upper()
    for termin in termini_f.postojeci_termini:
        sifra = termin[0] + termin[1]
        if sifra == zeljena_sifra:
            if termin[3] == "V":
                sedista = termin[4].split("|")
                redovi = []
                for i in sedista:
                    red = [i[0], i[2:]]
                    redovi.append(red)
                prikaz_sedista(redovi, zeljena_sifra, korisnik, kartica_lojalnosti)
            else:
                print("Termin sa unetom šifrom se već završio.")
                print("Pokušajte ponovo.")
                rezervacija_karte_kupac()
        else:
            pass
    print("Nije pronađen nijedan termin sa datom šifrom!")
    projekcije_f.meni_nakon_ispisa_projekcija()

def provera_unesenog_imena(ime):
    for korisnik in projekat.korisnici:
        if korisnik[2] == ime:
            print("Uneli ste korisničko ime registrovanog kupca.")
            return None
    if " " in ime:
        print("Uneli ste ime i prezime neregistrovanog kupca.")
        return None
    else:
        print("Morate uneti korisničko ime registrovanog\nili ime i prezime neregistrovanog\nkupca! Pokušajte ponovo.")
        rezervacija_karte_prodavac()

def rezervacija_karte_prodavac():
    if meni.tip_karte == "K":
        ispis_cene_za_danasnji_dan()
    else:
        pass
    korisnik = input("Unesite korisničko ime registrovanog\n"
                     "ili ime i prezime neregistrovanog\n"
                     "kupca: ")
    if korisnik == "":
        meni.meni_karte_prodavac()
    provera_unesenog_imena(korisnik)
    if dodatno_f.provera_lojalnosti(korisnik) == True:
        print("Uneti kupac ostvaruje pravo na karticu lojalnosti\n"
              "i tako ostvaruje 10% popusta!")
        kartica_lojalnosti = True
    else:
        kartica_lojalnosti = False
    zeljena_sifra = input("Unesite šifru željenog termina(npr. 1111AA): ")
    if zeljena_sifra == "":
        meni.meni_karte_prodavac()
    else:
        pass
    zeljena_sifra = zeljena_sifra.upper()
    for termin in termini_f.postojeci_termini:
        sifra = termin[0] + termin[1]
        if sifra == zeljena_sifra:
            if termin[3] == "V":
                sedista = termin[4].split("|")
                redovi = []
                for i in sedista:
                    red = [i[0], i[2:]]
                    redovi.append(red)
                prikaz_sedista(redovi, zeljena_sifra, korisnik, kartica_lojalnosti)
            else:
                print("Termin sa unetom šifrom se već završio.")
                print("Pokušajte ponovo.")
                rezervacija_karte_prodavac()
        else:
            pass
    print("Nije pronađen nijedan termin sa datom šifrom!")
    projekcije_f.meni_nakon_ispisa_projekcija()

def prikaz_sedista(redovi, sifra, korisnik, kartica_lojalnosti):
    dodatno_f.ispis_sedista_matrica(redovi)
    sediste = input("Unesite željeno sedište(npr. 1A, zauzeta sedišta su obeležena sa X): ")
    if sediste == "":
        rezervacija_karte_kupac()
    if sediste[1].upper() == "X":
        print("Ne možete zauzeti zauzeto sedište!")
        prikaz_sedista(redovi, sifra, korisnik, kartica_lojalnosti)
    if reg_korisnika.trenutni_korisnik[4][0] == "k":
        rezervacija_karte_sediste_kupac(sediste.upper(), redovi, sifra, korisnik, kartica_lojalnosti)
    elif reg_korisnika.trenutni_korisnik[4][0] == "p":
        if meni.tip_karte == "R":
            rezervacija_karte_sediste_prodavac(sediste.upper(), redovi, sifra, korisnik, kartica_lojalnosti)
        elif meni.tip_karte == "K":
            prodaja_karte_sediste_prodavac(sediste.upper(), redovi, sifra, korisnik, kartica_lojalnosti)
def rezervacija_karte_sediste_kupac(sediste_str, redovi, sifra, korisnik, kartica_lojalnosti):
    rezervacija_karte_sediste(sediste_str, redovi, sifra, korisnik, kartica_lojalnosti)
    danasnji_datum = datetime.date.strftime(datetime.date.today(), '%d.%m.%Y.')
    karta = []
    karta.append(reg_korisnika.trenutni_korisnik[2])
    karta.append(sifra)
    karta.append(sediste_str)
    karta.append(danasnji_datum)
    karta.append("R")
    projekat.karte.append(karta)
    upisivanje_karata()
    print("Uspešno ste rezervisali kartu!")
    while True:
        opcija = input("Da li želite da rezervišete još karata(da/ne)? ")
        if opcija.lower() == "da":
            rezervacija_karte_kupac()
            break
        elif opcija.lower() == "ne":
            projekcije_f.meni_pretrage_termina()
            break
        else:
            print("Morate uneti odgovarajuću opciju!")

def prodaja_karte_sediste_prodavac(sediste_str, redovi, sifra, korisnik, kartica_lojanosti):
    rezervacija_karte_sediste(sediste_str, redovi, sifra, korisnik, kartica_lojanosti)
    danasnji_datum = datetime.date.strftime(datetime.date.today(), '%d.%m.%Y.')
    cena = odredjivanje_cene_karte(sifra, kartica_lojanosti)
    karta = []
    karta.append(korisnik)
    karta.append(sifra)
    karta.append(sediste_str)
    karta.append(danasnji_datum)
    karta.append("K." + reg_korisnika.trenutni_korisnik[2] + "." + cena)
    projekat.karte.append(karta)
    upisivanje_karata()
    print("Uspešno ste prodali kartu!")
    while True:
        opcija = input("Da li želite da prodate još karata(da/ne)? ")
        if opcija.lower() == "da":
            meni.tip_karte = "K"
            rezervacija_karte_prodavac()
            break
        elif opcija.lower() == "ne":
            meni.meni_karte_prodavac()
            break
        else:
            print("Morate uneti odgovarajuću opciju!")

def rezervacija_karte_sediste_prodavac(sediste_str, redovi, sifra, korisnik, kartica_lojalnosti):
    rezervacija_karte_sediste(sediste_str, redovi, sifra, korisnik, kartica_lojalnosti)
    danasnji_datum = datetime.date.strftime(datetime.date.today(), '%d.%m.%Y.')
    karta = []
    karta.append(korisnik)
    karta.append(sifra)
    karta.append(sediste_str)
    karta.append(danasnji_datum)
    karta.append("R")
    projekat.karte.append(karta)
    upisivanje_karata()
    print("Uspešno ste rezervisali kartu!")
    while True:
        opcija = input("Da li želite da rezervišete još karata(da/ne)? ")
        if opcija.lower() == "da":
            rezervacija_karte_prodavac()
            break
        elif opcija.lower() == "ne":
            meni.meni_karte_prodavac()
            break
        else:
            print("Morate uneti odgovarajuću opciju!")

def rezervacija_karte_sediste(sediste_str, redovi, sifra, korisnik, kartica_lojalnosti):
    sediste = []
    for slovo in sediste_str:
        sediste.append(slovo)
    for red in redovi:
        if red[0] == sediste[0]:
            for slovo in red[1]:
                if slovo == sediste[1]:
                    red[1] = red[1].replace(slovo, "X")
                    redovi1 = []
                    for i in redovi:
                        i = ".".join(i)
                        redovi1.append(i)
                    redovi1 = "|".join(redovi1)
                    for i in termini_f.postojeci_termini:
                        if (i[0] + i[1]) == sifra:
                            i[4] = redovi1
                        else:
                            pass
                    termini_f.upis_termina()
                    return None
                else:
                    pass
    print("Nije moguće zauzeti uneto sedište! Pokušajte ponovo.")
    prikaz_sedista(redovi, sifra, korisnik, kartica_lojalnosti)



def upisivanje_karata():
    karte_za_upis = []
    for karta in projekat.karte:
        if karta[2][1].upper() == "X":
            pass
        else:
            karte_za_upis.append("|".join(karta) + "\n")
    karte_fajl = open("karte.txt", "w", encoding="utf-8")
    for karta in karte_za_upis:
        karte_fajl.write(karta)
    karte_fajl.close()
    return None

def ispis_rezervisanih_karata_kupca(odgovarajuce_karte):
    print("{0:^15}|{1:^30}|{2:^15}|{3:^15}|{4:^13}|{5:^9}|{6:^11}".format("Šifra termina",
                                                                  "Naziv filma", "Datum termina", "Vreme početka",
                                                                  "Vreme kraja", "Sedište", "Tip karte"))
    for karta in odgovarajuce_karte:
        sifra = karta[1]
        sediste = karta[2]
        tip_karte = ""
        if karta[4][0] == "R":
            tip_karte = "Rezervisana"
        elif karta[4][0] == "K":
            tip_karte = "Kupljena"
        for projekcija in projekat.projekcije:
            for termin in termini_f.postojeci_termini:
                if karta[1][:4] == projekcija[0] and karta[1] == (termin[0] + termin[1]):
                    naziv_filma = projekcija[5]
                    vreme_pocetka = projekcija[2]
                    vreme_kraja = projekcija[3]
                    datum_termina = termin[2]
                    print("{0:^15}|{1:^30}|{2:^15}|{3:^15}|{4:^13}|{5:^9}|{6:^11}".format(sifra, naziv_filma, datum_termina,
                                                                                  vreme_pocetka, vreme_kraja, sediste, tip_karte))
                else:
                    pass
    return None

def ispis_rezervisanih_karata_prodavac(odgovarajuce_karte):
    print("{0:^15}|{7:^19}|{1:^30}|{2:^19}|{3:^15}|{4:^13}|{5:^9}|{6:^11}".format("Šifra termina",
                                                                          "Naziv filma", "Datum rezervacije",
                                                                          "Vreme početka",
                                                                          "Vreme kraja", "Sedište", "Tip karte", "Kupac"))
    for karta in odgovarajuce_karte:
        kupac = karta[0]
        sifra = karta[1]
        sediste = karta[2]
        tip_karte = ""
        if karta[4][0] == "R":
            tip_karte = "Rezervisana"
        elif karta[4][0] == "K":
            tip_karte = "Kupljena"
        for projekcija in projekat.projekcije:
            for termin in termini_f.postojeci_termini:
                if karta[1][:4] == projekcija[0] and karta[1] == (termin[0] + termin[1]):
                    naziv_filma = projekcija[5]
                    vreme_pocetka = projekcija[2]
                    vreme_kraja = projekcija[3]
                    datum_termina = termin[2]
                    print("{0:^15}|{7:^19}|{1:^30}|{2:^19}|{3:^15}|{4:^13}|{5:^9}|{6:^11}".format(sifra, naziv_filma,
                                                                                          datum_termina,
                                                                                          vreme_pocetka, vreme_kraja,
                                                                                          sediste, tip_karte, kupac))
            else:
                pass
    return None

def ispis_prodatih_karata_menadzer_1(odgovarajuce_karte):
    print("{0:^15}|{1:^19}|{2:^30}|{3:^15}|{4:^16}|{5:^8}|{6:^9}".format("Šifra termina", "Kupac",
                                                                          "Naziv filma", "Datum prodaje",
                                                                          "Prodavac",
                                                                          "Cena", "Sedište"))
    for karta in odgovarajuce_karte:
        info_kupovina = karta[4].split(".")
        prodavac = info_kupovina[1]
        cena = info_kupovina[2]
        kupac = karta[0]
        sifra = karta[1]
        datum_prodaje = karta[3]
        sediste = karta[2]
        for projekcija in projekat.projekcije:
            if karta[1][:4] == projekcija[0]:
                naziv_filma = projekcija[5]
                print("{0:^15}|{1:^19}|{2:^30}|{3:^15}|{4:^16}|{5:^8}|{6:^9}".format(sifra, kupac, naziv_filma,
                                                                                      datum_prodaje,
                                                                                      prodavac, cena,
                                                                                      sediste))
            else:
                pass
    return None

def ispis_prodatih_karata_menadzer_2(odgovarajuce_karte):
    print("{0:^29}|{1:^13}".format("Ukupan broj prodatih karata", "Ukupna cena"))
    ukupan_broj_prodatih = len(odgovarajuce_karte)
    ukupna_cena = 0
    for karta in odgovarajuce_karte:
        info_kupovine = karta[4].split(".")
        ukupna_cena += eval(info_kupovine[2])
    print("{0:^29}|{1:^13}".format(ukupan_broj_prodatih, str(ukupna_cena)))
    return None

def ispis_prodatih_karata_menadzer_3(odgovarajuce_karte, prodavci):
    print("{0:^16}|{1:^29}|{2:^13}".format("Prodavac", "Ukupan broj prodatih karata", "Ukupna cena"))
    for prodavac in prodavci:
        karte_prodavca = []
        for karta in odgovarajuce_karte:
            info_kupovina = karta[4].split(".")
            if info_kupovina[1] == prodavac:
                karte_prodavca.append(karta)
        ukupan_broj = len(karte_prodavca)
        ukupna_cena = 0
        for karta in karte_prodavca:
            info_kupovina = karta[4].split(".")
            ukupna_cena += eval(info_kupovina[2])
        print("{0:^16}|{1:^29}|{2:^13}".format(prodavac, ukupan_broj, str(ukupna_cena)))
    return None


def pregled_rezervisanih_karata_prodavac():
    odgovarajuce_karte = []
    for karta in projekat.karte:
            odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nema ni jedne rezervisane karte.")
        meni.meni_karte_prodavac()
    else:
        pass
    ispis_rezervisanih_karata_prodavac(odgovarajuce_karte)
    while True:
        opcija = input("[0] Natrag\n"
                       "Unesite željenu opciju: ")
        if opcija == "0":
            meni.meni_karte_prodavac()
            break
        else:
            print("Morate uneti odgovarajuću opciju!")


def pregled_rezervisanih_karata_kupac():
    odgovarajuce_karte = []
    for karta in projekat.karte:
        if karta[0] == reg_korisnika.trenutni_korisnik[2]:
            odgovarajuce_karte.append(karta)
        else:
            pass
    if odgovarajuce_karte == []:
        print("Vi nemate nijednu rezervisanu kartu.")
        meni.meni_karte_kupac()
    else:
        pass
    ispis_rezervisanih_karata_kupca(odgovarajuce_karte)
    while True:
        opcija = input("[0] Natrag\n"
                       "Unesite željenu opciju: ")
        if opcija == "0":
            meni.meni_karte_kupac()
            break
        else:
            print("Morate uneti odgovarajuću opciju!")

def ponistavanje_rezervacija_kupac():
    odgovarajuce_karte = []
    for karta in projekat.karte:
        if karta[0] == reg_korisnika.trenutni_korisnik[2]:
            odgovarajuce_karte.append(karta)
    ispis_rezervisanih_karata_kupca(odgovarajuce_karte)
    sifra = input("Unesite šifru termina za koji ste rezervisali kartu\n"
                  "koju želite da poništite(npr. 1111AA): ")
    if sifra == "":
        meni.meni_karte_kupac()
    sediste = input("Unesite sedište koje ste zauzeli pri rezervaciji\n"
                    "termina koji želite da poništite(npr. 1A): ")
    if sediste == "":
        meni.meni_karte_kupac()
    sifra = sifra.upper()
    sediste = sediste.upper()
    karta_pronadjena = False
    for karta in projekat.karte:
        if karta[1] == sifra and karta[0] == reg_korisnika.trenutni_korisnik[2] and karta[2] == sediste:
            projekat.karte.remove(karta)
            karta_pronadjena = True
    if karta_pronadjena == False:
        print("Nije pronađena Vaša karta sa datom šifrom i datim sedištem.\n"
              "Pokušajte ponovo.")
        ponistavanje_rezervacija_kupac()
    else:
        pass
    upisivanje_karata()
    for termin in termini_f.postojeci_termini:
        if (termin[0] + termin[1]) == sifra:
            redovi = termin[4].split("|")
            redovi_za_upis = []
            for red in redovi:
                if red[0] == sediste[0]:
                    red = [*red]
                    red[ord(sediste[1]) - ord('A') + 2] = sediste[1]
                    red = "".join(red)
                    redovi_za_upis.append(red)
                else:
                    redovi_za_upis.append(red)
            termin[4] = "|".join(redovi_za_upis)
    termini_f.upis_termina()
    print("Uspešno ste poništili rezervaciju!")
    while True:
        opcija = input("Da li želite da poništite još karata(da/ne)? ")
        opcija = opcija.lower()
        if opcija == "da":
            ponistavanje_rezervacija_kupac()
            break
        elif opcija == "ne":
            meni.meni_karte_kupac()
            break
        else:
            print("Morate uneti odgovarajuću opciju!")

def ponistavanje_rezervacija_prodavac():
    kupac = input("Unesite korisničko ime ili ime i prezime\n"
                  "kupca koji je kupio/rezervisao kartu: ")
    if kupac == "":
        meni.meni_karte_prodavac()
    sifra = input("Unesite šifru termina karte koju želite da poništite: ")
    if sifra == "":
        meni.meni_karte_prodavac()
    sediste = input("Unesite koje je sedište zauzeto kartom koju želite da poništite: ")
    if sediste == "":
        meni.meni_karte_prodavac()
    sifra = sifra.upper()
    sediste = sediste.upper()
    karta_pronadjena = False
    for karta in projekat.karte:
        if karta[1] == sifra and karta[0] == kupac and karta[2] == sediste:
            projekat.karte.remove(karta)
            karta_pronadjena = True
    if karta_pronadjena == False:
        print("Nije pronađena karta sa datim kupcem, šifrom i sedištem.\n"
              "Pokušajte ponovo.")
        ponistavanje_rezervacija_prodavac()
    upisivanje_karata()
    for termin in termini_f.postojeci_termini:
        if (termin[0] + termin[1]) == sifra:
            redovi = termin[4].split("|")
            redovi_za_upis = []
            for red in redovi:
                if red[0] == sediste[0]:
                    red = [*red]
                    red[ord(sediste[1]) - ord('A') + 2] = sediste[1]
                    red = "".join(red)
                    redovi_za_upis.append(red)
                else:
                    redovi_za_upis.append(red)
            termin[4] = "|".join(redovi_za_upis)
    termini_f.upis_termina()
    print("Uspešno ste poništili kartu!")
    while True:
        opcija = input("Da li želite da poništite još karata(da/ne)? ")
        opcija = opcija.lower()
        if opcija == "da":
            ponistavanje_rezervacija_prodavac()
            break
        elif opcija == "ne":
            meni.meni_karte_prodavac()
            break
        else:
            print("Morate uneti odgovarajuću opciju!")

def pretraga_karata_po_sifri():
    odgovarajuce_karte = []
    sifra = input("Unesite šifru projekcije čije karte želite da pregledate: ")
    if sifra == "":
        meni.meni_pretrage_karata_prodavac()
    for karta in projekat.karte:
        if karta[1][0:4] == sifra.upper():
            odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna karta koja odgovara Vašoj šifri projekcije.")
        print("Pokušajte ponovo.")
        pretraga_karata_po_sifri()
    else:
        ispis_rezervisanih_karata_prodavac(odgovarajuce_karte)
    meni_posle_pretrage_karata()

def pretraga_karata_po_imenu():
    odgovarajuce_karte = []
    ime = input("Unesite korisničko ime registrovanog kupca\n"
                "ili ime i prezime neregistrovanog kupca\n"
                "čije karte želite da pregledate: ")
    if ime == "":
        meni.meni_pretrage_karata_prodavac()
    for karta in projekat.karte:
        if karta[0] == ime:
            odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna karta koja odgovara Vašem unetom imenu.")
        print("Pokušajte ponovo.")
        pretraga_karata_po_imenu()
    else:
        ispis_rezervisanih_karata_prodavac(odgovarajuce_karte)
    meni_posle_pretrage_karata()

def pretraga_karata_po_datumu():
    odgovarajuce_karte = []
    datum = input("Unesite datum kog su rezervisane karte\n"
                  "koje želite da pregledate(dd.mm.yy.): ")
    if datum == "":
        meni.meni_pretrage_karata_prodavac()
    datum_format = '%d.%m.%Y.'
    try:
        datum_formatiran = datetime.datetime.strptime(datum, datum_format)
    except ValueError:
        print("Morate uneti datum u odgovarajućem formatu(dd.mm.yy.)!")
        pretraga_karata_po_datumu()
    for karta in projekat.karte:
        if karta[3] == datum:
            odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna karta koja odgovara Vašem datumu.")
        print("Pokušajte ponovo.")
        pretraga_karata_po_datumu()
    ispis_rezervisanih_karata_prodavac(odgovarajuce_karte)
    meni_posle_pretrage_karata()

def pretraga_karata_po_vremenu_pocetka():
    odgovarajuce_karte = []
    odgovarajuce_sifre_projekcija = []
    vreme = input("Unesite vreme u koje počinju projekcije\n"
                  "čije karte želite da pregledate(hh:mm): ")
    if vreme == "":
        meni.meni_pretrage_karata_prodavac()
    vreme_format = '%H:%M'
    try:
        vreme_formatirano = datetime.datetime.strptime(vreme, vreme_format).time()
    except ValueError:
        print("Morate uneti vreme u odgovarajućem formatu(hh:mm)!")
        pretraga_karata_po_vremenu_pocetka()
    for projekcija in projekat.projekcije:
        if projekcija[2] == vreme:
            odgovarajuce_sifre_projekcija.append(projekcija[0])
    for sifra in odgovarajuce_sifre_projekcija:
        for karta in projekat.karte:
            if sifra == karta[1][0:4]:
                odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna karta kojoj odgovara\n"
              "projekcija koja počinje u zadato vreme.\n"
              "Pokušajte ponovo.")
        pretraga_karata_po_vremenu_pocetka()
    else:
        ispis_rezervisanih_karata_prodavac(odgovarajuce_karte)
    meni_posle_pretrage_karata()

def pretraga_karata_po_vremenu_kraja():
    odgovarajuce_karte = []
    odgovarajuce_sifre_projekcija = []
    vreme = input("Unesite vreme u koje se završavaju projekcije\n"
                  "čije karte želite da pregledate(hh:mm): ")
    if vreme == "":
        meni.meni_pretrage_karata_prodavac()
    vreme_format = '%H:%M'
    try:
        vreme_formatirano = datetime.datetime.strptime(vreme, vreme_format).time()
    except ValueError:
        print("Morate uneti vreme u odgovarajućem formatu(hh:mm)!")
        pretraga_karata_po_vremenu_kraja()
    for projekcija in projekat.projekcije:
        if projekcija[3] == vreme:
            odgovarajuce_sifre_projekcija.append(projekcija[0])
    for sifra in odgovarajuce_sifre_projekcija:
        for karta in projekat.karte:
            if sifra == karta[1][0:4]:
                odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna karta kojoj odgovara\n"
              "projekcija koja se završava u zadato vreme.\n"
              "Pokušajte ponovo.")
        pretraga_karata_po_vremenu_kraja()
    else:
        ispis_rezervisanih_karata_prodavac(odgovarajuce_karte)
    meni_posle_pretrage_karata()

def pretraga_karata_po_tipu_karte():
    odgovarajuce_karte = []
    tip = ""
    opcija = input("[1] Rezervisana karta\n"
                   "[2] Kupljena karta\n"
                   "Odaberite koji tip karata želite da pregledate: ")
    if opcija == "1":
        tip = "R"
    elif opcija == "2":
        tip = "K"
    elif opcija == "":
        meni.meni_pretrage_karata_prodavac()
    else:
        print("Morate uneti odgovarajuću opciju!")
        pretraga_karata_po_tipu_karte()
    for karta in projekat.karte:
        if karta[4][0] == tip:
            odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna karta koja odgovara Vašem tipu karte.")
        print("Pokušajte ponovo.")
        pretraga_karata_po_tipu_karte()
    ispis_rezervisanih_karata_prodavac(odgovarajuce_karte)
    meni_posle_pretrage_karata()

def meni_posle_pretrage_karata():
    opcija = input("[0] Natrag\n"
                   "[1] Prodaja rezervisanih karata karata\n"
                   "Unesite željenu opciju: ")
    if opcija == "0":
        meni.meni_pretrage_karata_prodavac()
    elif opcija == "1":
        prodaja_rezervisane_karte()
    else:
        print("Morate uneti odgovarajuću opciju!")
        meni_posle_pretrage_karata()

def prodaja_rezervisane_karte():
    ispis_cene_za_danasnji_dan()
    ime = input("Unesite korisničko ime registrovanog ili\n"
                "ime i prezime neregistrovanog kupca čiju\n"
                "rezervisanu kartu želite da prodate: ")
    if ime == "":
        meni.meni_karte_prodavac()
    kartica_lojalnosti = dodatno_f.provera_lojalnosti(ime)
    sifra = input("Unesite šifru termina za koji je karta kupljena: ")
    if sifra == "":
        meni.meni_karte_prodavac()
    cena = odredjivanje_cene_karte(sifra, kartica_lojalnosti)
    sediste = input("Unesite oznaku sedišta za koje je karta kupljena: ")
    if sediste == "":
        meni.meni_karte_prodavac()
    karta_nadjena = False
    for karta in projekat.karte:
            if karta[0] == ime and karta[1] == sifra.upper() and karta[2] == sediste.upper():
                if karta[4][0] == "K":
                    print("Data karta je već prodata!"
                          "Pokušajte ponovo.")
                    prodaja_rezervisane_karte()
                else:
                    karta[4] = "K." + reg_korisnika.trenutni_korisnik[2] + "." + cena
                    karta[3] = datetime.datetime.strftime(datetime.date.today(), '%d.%m.%Y.')
                    karta_nadjena = True
    if karta_nadjena == False:
        print("Nije pronađena nijedna karta sa unetim atributima!\n"
              "Pokušajte ponovo.")
        prodaja_rezervisane_karte()
    else:
        pass
    upisivanje_karata()
    print("Uspešno ste prodali rezervisanu kartu!")
    while True:
        opcija = input("Da li želite da prodate još rezervisanih karata(da/ne)? ")
        if opcija.lower() == "da":
            prodaja_rezervisane_karte()
            break
        elif opcija.lower() == "ne":
            meni.meni_karte_prodavac()
            break
        else:
            print("Morate uneti odgovarajuću opciju!")
            print("Pokušajte ponovo.")

def odredjivanje_cene_karte(sifra, kartica_lojalnosti):
    danasnji_dan = datetime.date.today().weekday()
    cena = ""
    for projekcija in projekat.projekcije:
        if projekcija[0] == sifra[0:4]:
            cena = projekcija[6]
            break
        else:
            pass
    if danasnji_dan == 1:
        if kartica_lojalnosti == True:
            konacna_cena = int((eval(cena) - 50) * 0.9)
            return str(konacna_cena)
        else:
            konacna_cena = eval(cena) - 50
            return str(konacna_cena)
    elif danasnji_dan == 5 or danasnji_dan == 6:
        if kartica_lojalnosti == True:
            konacna_cena = int((eval(cena) + 50) * 0.9)
            return str(konacna_cena)
        else:
            konacna_cena = eval(cena) + 50
            return str(cena)
    else:
        if kartica_lojalnosti == True:
            konacna_cena = int(eval(cena) * 0.9)
            return str(konacna_cena)
        else:
            return str(cena)

def ispis_cene_za_danasnji_dan():
    danasnji_dan = datetime.date.today().weekday()
    if danasnji_dan == 1:
        print("Danas je utorak, sve karte su jeftinije 50 dinara!")
        return None
    elif danasnji_dan == 5:
        print("Danas je subota, sve karte su skuplje 50 dinara!")
        return None
    elif danasnji_dan == 6:
        print("Danas je nedelja, sve karte su skuplje 50 dinara!")
        return None
    else:
        return None