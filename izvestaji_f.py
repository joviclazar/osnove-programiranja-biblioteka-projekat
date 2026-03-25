import karte_f
import projekat
import datetime
import meni
import termini_f


def provera_datuma(datum):
    try:
        datum_formatiran = datetime.datetime.strptime(datum, '%d.%m.%Y.')
        return True
    except ValueError:
        print("Morate uneti datum u odgovarajućem formatu(dd.mm.yy.)!\n"
              "Pokušajte ponovo.")
        return False


def izvestaj_datum_prodaje():
    tip_izvestaja = "1"
    odgovarajuce_karte = []
    zeljeni_datum = input("Unesite željeni datum prodaje(dd.mm.yy.): ")
    if zeljeni_datum == "":
        meni.meni_izvestaja()
    if provera_datuma(zeljeni_datum) is False:
        izvestaj_datum_prodaje()
    for karta in projekat.karte:
        if karta[3] == zeljeni_datum and karta[4][0] == "K":
            odgovarajuce_karte.append(karta)
        else:
            pass
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna karta za zadati datum prodaje.\n"
              "Pokušajte ponovo.")
        izvestaj_datum_prodaje()
    else:
        karte_f.ispis_prodatih_karata_menadzer_1(odgovarajuce_karte)
    meni_posle_izvestaja(tip_izvestaja, odgovarajuce_karte, prodavci=[])


def izvestaj_datum_termina():
    tip_izvestaja = "2"
    odgovarajuce_karte = []
    odgovarajuci_termini = []
    zeljeni_datum = input("Unesite željeni datum termina projekcije(dd.mm.yy.): ")
    if zeljeni_datum == "":
        meni.meni_izvestaja()
    if provera_datuma(zeljeni_datum) is False:
        izvestaj_datum_termina()
    for termin in termini_f.postojeci_termini:
        if termin[2] == zeljeni_datum:
            odgovarajuci_termini.append(termin[0] + termin[1])
        else:
            pass
    for karta in projekat.karte:
        for termin in odgovarajuci_termini:
            if karta[1] == termin and karta[4][0] == "K":
                odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna odgovarajuća karta!\nPokušajte ponovo.")
        izvestaj_datum_termina()
    else:
        karte_f.ispis_prodatih_karata_menadzer_1(odgovarajuce_karte)
    meni_posle_izvestaja(tip_izvestaja, odgovarajuce_karte, prodavci=[])


def izvestaj_datum_prodaje_prodavac():
    tip_izvestaja = "3"
    odgovarajuce_karte = []
    prodavac = input("Unesite korisničko ime željenog prodavca: ")
    if prodavac == "":
        meni.meni_izvestaja()
    zeljeni_datum = input("Unesite željeni datum prodaje(dd.mm.yy.): ")
    if zeljeni_datum == "":
        meni.meni_izvestaja()
    if provera_datuma(zeljeni_datum) is False:
        izvestaj_datum_prodaje_prodavac()
    for karta in projekat.karte:
        if karta[4][0] == "R":
            pass
        else:
            info_kupovina = karta[4].split(".")
            if karta[3] == zeljeni_datum and info_kupovina[1] == prodavac and info_kupovina[0] == "K":
                odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna odgovarajuća karta!\nPokušajte ponovo.")
        izvestaj_datum_prodaje_prodavac()
    else:
        karte_f.ispis_prodatih_karata_menadzer_1(odgovarajuce_karte)
    meni_posle_izvestaja(tip_izvestaja, odgovarajuce_karte, prodavci=[])


def izvestaj_broj_cena_dan_prodaje():
    tip_izvestaja = "4"
    odgovarajuce_karte = []
    izabran_dan = input("Unesite željeni dan u nedelji: ")
    if izabran_dan == "":
        meni.meni_izvestaja()
    if provera_unetog_dana(izabran_dan) == False:
        print("Morate uneti jedan od dana u nedelji!\nPokušajte ponovo.")
        izvestaj_broj_cena_dan_prodaje()
    dan = odredjivanje_dana_u_nedelji(izabran_dan.lower())
    for karta in projekat.karte:
        datum_karte = datetime.datetime.strptime(karta[3], '%d.%m.%Y.')
        if datum_karte.weekday() == dan and karta[4][0] == "K":
            odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna odgovarajuća karta!\nPokušaje ponovo.")
        izvestaj_broj_cena_dan_prodaje()
    else:
        karte_f.ispis_prodatih_karata_menadzer_2(odgovarajuce_karte)
    meni_posle_izvestaja(tip_izvestaja, odgovarajuce_karte, prodavci=[])


def izvestaj_broj_cena_dan_projekcije():
    tip_izvestaja = "5"
    odgovarajuce_karte = []
    odgovarajuce_sifre = []
    izabran_dan = input("Unesite željeni dan u nedelji: ")
    if izabran_dan == "":
        meni.meni_izvestaja()
    if provera_unetog_dana(izabran_dan) == False:
        print("Morate uneti jedan od dana u nedelji!\nPokušajte ponovo.")
        izvestaj_broj_cena_dan_projekcije()
    dan = odredjivanje_dana_u_nedelji(izabran_dan.lower())
    for projekcija in projekat.projekcije:
        if izabran_dan in projekcija[4].lower():
            odgovarajuce_sifre.append(projekcija[0])
    for karta in projekat.karte:
        if karta[1][:4] in odgovarajuce_sifre and karta[4][0] == "K":
            odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna karta koja odgovara unetom danu projekcije!\n"
              "Pokušajte ponovo.")
        izvestaj_broj_cena_dan_projekcije()
    else:
        karte_f.ispis_prodatih_karata_menadzer_2(odgovarajuce_karte)
    meni_posle_izvestaja(tip_izvestaja, odgovarajuce_karte, prodavci=[])


def izvestaj_broj_cena_film():
    tip_izvestaja = "6"
    odgovarajuce_karte = []
    odgovarajuce_sifre = []
    izabran_film = input("Unesite ime željenog filma: ")
    if izabran_film == "":
        meni.meni_izvestaja()
    if provera_unetog_filma(izabran_film.lower()) == False:
        print("Morate uneti jedan od postojećih filmova!\nPokušajte ponovo.")
        izvestaj_broj_cena_film()
    for projekcija in projekat.projekcije:
        if projekcija[5].lower() == izabran_film.lower():
            odgovarajuce_sifre.append(projekcija[0])
    for karta in projekat.karte:
        if karta[1][:4] in odgovarajuce_sifre and karta[4][0] == "K":
            odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna odgovarajuća karta!\nPokušajte ponovo.")
        izvestaj_broj_cena_film()
    else:
        karte_f.ispis_prodatih_karata_menadzer_2(odgovarajuce_karte)
    meni_posle_izvestaja(tip_izvestaja, odgovarajuce_karte, prodavci=[])


def izvestaj_broj_cena_dan_prodaje_prodavac():
    tip_izvestaja = "7"
    odgovarajuce_karte = []
    izabran_dan = input("Unesite željeni dan prodaje: ")
    if izabran_dan == "":
        meni.meni_izvestaja()
    if provera_unetog_dana(izabran_dan) == False:
        print("Morate uneti jedan od dana u nedelji!\nPokušajte ponovo.")
        izvestaj_broj_cena_dan_prodaje_prodavac()
    dan = odredjivanje_dana_u_nedelji(izabran_dan)
    prodavac = input("Unesite željenog prodavca: ")
    if prodavac == "":
        meni.meni_izvestaja()
    for karta in projekat.karte:
        if karta[4][0] == "K":
            info_kupovina = karta[4].split(".")
            dan_karta = datetime.datetime.strptime(karta[3], '%d.%m.%Y.')
            if info_kupovina[1] == prodavac and dan == datetime.date.weekday(dan_karta):
                odgovarajuce_karte.append(karta)
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna odgovarajuća karta!\nPokušajte ponovo.")
        izvestaj_broj_cena_dan_prodaje_prodavac()
    else:
        karte_f.ispis_prodatih_karata_menadzer_2(odgovarajuce_karte)
    meni_posle_izvestaja(tip_izvestaja, odgovarajuce_karte, prodavci=[])


def izvestaj_broj_cena_po_prodavcima():
    tip_izvestaja = "8"
    odgovarajuce_karte = []
    prodavci = []
    for karta in projekat.karte:
        datum_karte = datetime.datetime.strptime(karta[3], '%d.%m.%Y.')
        if karta[4][0] == "K" and datum_karte > (datetime.datetime.today() - datetime.timedelta(days=30)):
            info_kupovina = karta[4].split(".")
            if info_kupovina[1] in prodavci:
                odgovarajuce_karte.append(karta)
            else:
                prodavci.append(info_kupovina[1])
                odgovarajuce_karte.append(karta)
    karte_f.ispis_prodatih_karata_menadzer_3(odgovarajuce_karte, prodavci)
    meni_posle_izvestaja(tip_izvestaja, odgovarajuce_karte, prodavci)


def provera_unetog_filma(izabran_film):
    filmovi = []
    for projekcija in projekat.projekcije:
        filmovi.append(projekcija[5].lower())
    for film in filmovi:
        if film == izabran_film:
            return True
        else:
            pass
    return False
def provera_unetog_dana(izabran_dan):
    dani = ["ponedeljak", "utorak", "sreda", "četvrtak", "petak", "subota", "nedelja"]
    for dan in dani:
        if dan == izabran_dan.lower():
            return True
    else:
        pass
    return False


def odredjivanje_dana_u_nedelji(izabran_dan):
    if izabran_dan[:3] == "pon":
        return 0
    elif izabran_dan[:3] == "uto":
        return  1
    elif izabran_dan[:3] == "sre":
        return  2
    elif izabran_dan[:3] == "čet":
        return  3
    elif izabran_dan[:3] == "pet":
        return  4
    elif izabran_dan[:3] == "sub":
        return  5
    elif izabran_dan[:3] == "ned":
        return  6


def meni_posle_izvestaja(tip_izvestaja, odgovarajuce_karte, prodavci):
    opcija = input("Da li želite da sačuvate izveštaj u izvestaj_" + str(tip_izvestaja) + ".txt fajl(da/ne)? ")
    if opcija.lower() == "da":
        if eval(tip_izvestaja) < 4:
            upis_izvestaja_1(tip_izvestaja, odgovarajuce_karte)
            meni.meni_izvestaja()
        elif eval(tip_izvestaja) < 8:
            upis_izvestaja_2(tip_izvestaja, odgovarajuce_karte)
            meni.meni_izvestaja()
        elif eval(tip_izvestaja) == 8:
            upis_izvestaja_3(tip_izvestaja, odgovarajuce_karte, prodavci)
            meni.meni_izvestaja()
    elif opcija.lower() == "ne":
        meni.meni_izvestaja()
    else:
        print("Morate uneti odgovarajuću opciju! Pokušajte ponovo.")
        meni_posle_izvestaja(tip_izvestaja, odgovarajuce_karte, prodavci)

def upis_izvestaja_1(tip_izvestaja, odgovarajuce_karte):
    fajl = open("izvestaj_" + str(tip_izvestaja) + ".txt", "w", encoding="utf-8")
    fajl.write("{0:^15}|{1:^19}|{2:^30}|{3:^15}|{4:^16}|{5:^8}|{6:^10}\n".format("Šifra termina", "Kupac",
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
                fajl.write("{0:^15}|{1:^19}|{2:^30}|{3:^15}|{4:^16}|{5:^8}|{6:^10}\n".format(sifra, kupac, naziv_filma,
                                                                                     datum_prodaje,
                                                                                     prodavac, cena,
                                                                                     sediste))
    fajl.close()
    print("Uspešno ste sačuvali izveštaj!")
    return None

def upis_izvestaja_2(tip_izvestaja, odgovarajuce_karte):
    fajl = open("izvestaj_" + str(tip_izvestaja) + ".txt", "w", encoding="utf-8")
    fajl.write("{0:^29}|{1:^13}\n".format("Ukupan broj prodatih karata", "Ukupna cena"))
    ukupan_broj_prodatih = len(odgovarajuce_karte)
    ukupna_cena = 0
    for karta in odgovarajuce_karte:
        info_kupovine = karta[4].split(".")
        ukupna_cena += eval(info_kupovine[2])
    fajl.write("{0:^29}|{1:^13}\n".format(ukupan_broj_prodatih, str(ukupna_cena)))
    fajl.close()
    print("Uspešno ste sačuvali izveštaj!")
    return None

def upis_izvestaja_3(tip_izvestaja, odgovarajuce_karte, prodavci):
    fajl = open("izvestaj_" + str(tip_izvestaja) + ".txt", "w", encoding="utf-8")
    fajl.write("{0:^16}|{1:^29}|{2:^13}\n".format("Prodavac", "Ukupan broj prodatih karata", "Ukupna cena"))
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
        fajl.write("{0:^16}|{1:^29}|{2:^13}\n".format(prodavac, ukupan_broj, str(ukupna_cena)))
    print("Uspešno ste sačuvali izveštaj!")
    return None