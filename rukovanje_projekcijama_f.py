import izvestaji_f
import meni
import projekat
import projekcije_f
import termini_f
import datetime

def unos_sifre_projekcije(opcija):
    zeljena_projekcija = []
    zeljena_sifra = input("Unesite šifru željene projekcije: ")
    if zeljena_sifra == "":
        meni.rukovanje_projekcijama()
    for projekcija in projekat.projekcije:
        if zeljena_sifra == projekcija[0]:
            zeljena_projekcija = projekcija
    if zeljena_projekcija == []:
        print("Nije pronađena nijedna projekcija sa unetom šifrom!\nPokušajte ponovo.")
        unos_sifre_projekcije(opcija)
    if opcija == "1":
        izmena_filma_projekcije(zeljena_projekcija, zeljena_sifra)
    elif opcija == "2":
        izmena_vremena_pocetka(zeljena_projekcija, zeljena_sifra)
    elif opcija == "3":
        izmena_vremena_kraja(zeljena_projekcija, zeljena_sifra)
    elif opcija == "4":
        izmena_cene(zeljena_projekcija, zeljena_sifra)
    elif opcija == "5":
        izmena_dana(zeljena_projekcija, zeljena_sifra)

def dodavanje_projekcija():
    nova_projekcija = []
    sifra = eval(projekat.projekcije[-1][0]) + 1
    print("Šifra nove projekcije će biti " + str(sifra) + ".")
    film = dodavanje_projekcija_film()
    sala = dodavanje_projekcija_sala()
    vreme_pocetka = dodavanje_projekcija_pocetak()
    vreme_kraja = dodavanje_projekcija_kraj(vreme_pocetka, film)
    dani = dodavanje_projekcija_dani()
    cena = dodavanje_projekcija_cena()
    nova_projekcija.append(str(sifra))
    nova_projekcija.append(sala)
    nova_projekcija.append(vreme_pocetka)
    nova_projekcija.append(vreme_kraja)
    nova_projekcija.append(dani)
    nova_projekcija.append(film)
    nova_projekcija.append(str(cena))
    projekat.projekcije.append(nova_projekcija)
    projekcije_f.upis_projekcija()
    dodavanje_termina_nove_projekcije(nova_projekcija)
    print("Uspešno ste dodali novu projekciju!")
    meni.rukovanje_projekcijama()

def dodavanje_termina_nove_projekcije(nova_projekcija):
    prvo_slovo = ord(termini_f.postojeci_termini[-1][1][0])
    drugo_slovo = ord(termini_f.postojeci_termini[-1][1][1])
    danasnji_datum = datetime.date.today() - datetime.timedelta(days=1)
    for i in range(15):
        termin = []
        dan = ""
        danasnji_datum = danasnji_datum + datetime.timedelta(days=1)
        dan_int = datetime.date.weekday(danasnji_datum)
        if dan_int == 0:
            dan = "ponedeljak"
        elif dan_int == 1:
            dan = "utorak"
        elif dan_int == 2:
            dan = "sreda"
        elif dan_int == 3:
            dan = "četvrtak"
        elif dan_int == 4:
            dan = "petak"
        elif dan_int == 5:
            dan = "subota"
        elif dan_int == 6:
            dan = "nedelja"
        if dan.title() in nova_projekcija[4].title():
            sifra = nova_projekcija[0]
            drugo_slovo += 1
            if drugo_slovo > 90:
                drugo_slovo = ord('A')
                prvo_slovo += 1
            else:
                pass
            sufiks = chr(prvo_slovo) + chr(drugo_slovo)
            termin.append(sifra)
            termin.append(sufiks)
            termin.append(danasnji_datum.strftime('%d.%m.%Y.'))
            termin.append("V")
            for sala in projekat.sale:
                if sala[0] == nova_projekcija[1]:
                    redovi = sala[1]
                else:
                    pass
            termin.append(redovi)
            termini_f.postojeci_termini.append(termin)
    termini_f.upis_termina()
    return None

def dodavanje_projekcija_cena():
    while True:
        cena = input("Unesite cenu za novu projekciju(mora biti ceo broj koji se završava sa nulom): ")
        try:
            eval(cena)
            if eval(cena) % 10 != 0 and type(eval(cena)) == int:
                print("Morate uneti cenu u odgovarajućem formatu!")
            else:
                try:
                    return str(int(cena))
                except ValueError:
                    print("Morate uneti cenu u odgovarajućem formatu!")
        except NameError:
            print("Morate uneti cenu u odgovarajućem formatu")


def dodavanje_projekcija_dani():
    zeljeni_dani = []
    while True:
        zeljeni_dani_str = input("Unesite željene dane(dan1, dan2, dan3...): ")
        if zeljeni_dani_str == "":
            meni.rukovanje_projekcijama()
        zeljeni_dani_str = zeljeni_dani_str.lower()
        zeljeni_dani = zeljeni_dani_str.split(", ")
        dani_odgovarajuci = True
        for dan in zeljeni_dani:
            if izvestaji_f.provera_unetog_dana(dan) == False:
                print("Svi uneti dani moraju biti jedan od dana u nedelji!\nPokušajte ponovo")
                dani_odgovarajuci = False
        if dani_odgovarajuci == True:
            return zeljeni_dani_str.capitalize()

def dodavanje_projekcija_kraj(vreme_pocetka, naziv_filma):
    vreme_trajanja = ""
    for film in projekat.linije_filmova:
        if film[1] == naziv_filma:
            vreme_trajanja = film[3]
            break
    minimalno_vreme_kraja = datetime.datetime.strptime(vreme_pocetka, '%H:%M') + datetime.timedelta(minutes=eval(vreme_trajanja))
    while True:
        vreme_kraja_str = input("Unesite vreme kraja projekcije.\nImajte na umu da je film počeo u "
                            + vreme_pocetka + ", a traje " + vreme_trajanja + " minuta: ")
        try:
            vreme_kraja = datetime.datetime.strptime(vreme_kraja_str, '%H:%M')
            if vreme_kraja > minimalno_vreme_kraja:
                if vreme_kraja_str[3:5] == "30" or vreme_kraja_str[3:5] == "00":
                    return vreme_kraja_str
                else:
                    print("Film se mora završiti u hh:00 ili hh:30!\nPokušajte ponovo.")
            else:
                print("Projekcija se mora završiti kasnije zbog dužine filma!\nPokušajte ponovo.")
        except ValueError:
            print("Morate uneti vreme u odgovarajućem formatu(hh:mm)!\nPokušajte ponovo.")
def dodavanje_projekcija_film():
    while True:
        novi_film = input("Unesite ime filma: ")
        for film in projekat.linije_filmova:
            if film[1] == novi_film:
                return novi_film
        print("Uneti film nije pronađen u našoj bazi filmova!\nPokušajte ponovo.")


def dodavanje_projekcija_pocetak():
    while True:
        vreme_pocetka_str = input("Unesite vreme početka projekcije: ")
        try:
            vreme_pocetka = datetime.datetime.strptime(vreme_pocetka_str, '%H:%M')
            if vreme_pocetka_str[3:5] == "00" or vreme_pocetka_str[3:5] == "30":
                return vreme_pocetka_str
            else:
                print("Film mora početi u hh:00 ili hh:30!\nPokušajte ponovo.")
        except ValueError:
            print("Morate uneti vreme u odgovarajućem formatu(hh:mm)!\nPokušajte ponovo.")

def dodavanje_projekcija_sala():
    print("Izaberite jednu od sala.")
    while True:
        i = 1
        for sala in projekat.sale:
            print("["+ str(i) + "] " + sala[0])
            i += 1
        opcija = input("Unesite odgovarajuću opciju: ")
        for sala in projekat.sale:
            if sala[0][1] == opcija:
                return sala[0]
        print("Morate uneti odgovarajuću opciju!\nPokušajte ponovo.")

def brisanje_projekcija():
    zeljena_projekcija = []
    zeljena_sifra = input("Unesite šifru projekcije koju želite da obrišete: ")
    if zeljena_sifra == "":
        meni.rukovanje_projekcijama()
    for projekcija in projekat.projekcije:
        if zeljena_sifra == projekcija[0]:
            zeljena_projekcija = projekcija
    if zeljena_projekcija == []:
        print("Nije pronađena nijedna projekcija sa unetom šifrom!\nPokušajte ponovo.")
        brisanje_projekcija()
    projekat.projekcije.pop(zeljena_projekcija)
    projekcije_f.upis_projekcija()
    termini_za_brisanje = []
    postojece_karte = []
    for karta in projekat.karte:
        postojece_karte.append(karta[1])
    for termin in termini_f.postojeci_termini:
        if termin[0] == zeljena_sifra and termin[3] == "V" and (termin[0] + termin[1]) not in postojece_karte:
            termini_za_brisanje.append(termin)
    for termin in termini_za_brisanje:
        termini_f.postojeci_termini.pop(termin)
    termini_f.upis_termina()
    print("Uspešno ste obrisali projekciju!")
    meni.rukovanje_projekcijama()

def izmena_projekcija_meni():
    opcija = input("[1] Izmena filma\n"
                   "[2] Izmena vremena početka projekcije\n"
                   "[3] Izmena vremena kraja projekcije\n"
                   "[4] Izmena cene\n"
                   "[5] Izmena dana\n"
                   "[0] Natrag\n"
                   "Unesite odgovarajuću opciju: ")
    if opcija == "1":
        unos_sifre_projekcije("1")
    elif opcija == "2":
        unos_sifre_projekcije("2")
    elif opcija == "3":
        unos_sifre_projekcije("3")
    elif opcija == "4":
        unos_sifre_projekcije("4")
    elif opcija == "5":
        unos_sifre_projekcije("5")
    elif opcija == "0":
        meni.rukovanje_projekcijama()
    else:
        print("Morate uneti odgovarajuću opciju!\nPokušajte ponovo.")
        izmena_projekcija_meni()

def izmena_vremena_kraja(zeljena_projekcija, zeljena_sifra):
    vreme_trajanja_filma = ""
    for film in projekat.linije_filmova:
        if zeljena_projekcija[5] == film[1]:
            vreme_trajanja_filma = film[3]
            break
    minimalno_vreme_kraja = datetime.datetime.strptime(zeljena_projekcija[2], '%H:%M') + datetime.timedelta(minutes=eval(vreme_trajanja_filma))
    novo_vreme = input("Unesite novo vreme kraja projekcije.\nImajte na umu da film traje "
                       + vreme_trajanja_filma + " minuta, a počinje u " + zeljena_projekcija[2] + ": ")
    if novo_vreme == "":
        meni.rukovanje_projekcijama()
    try:
        if datetime.datetime.strptime(novo_vreme, '%H:%M') < minimalno_vreme_kraja:
            print("Projekcija se mora završiti kasnije zbog dužine filma!")
            izmena_vremena_kraja(zeljena_projekcija, zeljena_sifra)
        else:
            if novo_vreme[3:5] == "00" or novo_vreme[3:5] == "30":
                for projekcija in projekat.projekcije:
                    if projekcija == zeljena_projekcija:
                        projekcija[2] = novo_vreme
                        projekcije_f.upis_projekcija()
                        print("Uspešno ste izmenili projekciju!")
                        meni.rukovanje_projekcijama()
            else:
                print("Kraj projekcije mora biti u hh:00 ili hh:30!")
                izmena_vremena_kraja(zeljena_projekcija, zeljena_sifra)
    except ValueError:
        print("Niste uneti vreme u odgovarajućem formatu(hh:mm)!\nPokušajte ponovo.")
        izmena_vremena_pocetka(zeljena_projekcija, zeljena_sifra)
def izmena_dana(zeljena_projekcija, zeljena_sifra):
    zeljeni_dani = []
    zeljeni_dani_str = input("Unesite nove dane(dan1, dan2, dan3...): ")
    if zeljeni_dani_str == "":
        meni.rukovanje_projekcijama()
    zeljeni_dani_str = zeljeni_dani_str.lower()
    zeljeni_dani = zeljeni_dani_str.split(", ")
    for dan in zeljeni_dani:
        if izvestaji_f.provera_unetog_dana(dan) == False:
            izmena_dana(zeljena_projekcija, zeljena_sifra)
    for projekcija in projekat.projekcije:
        if projekcija == zeljena_projekcija:
            projekcija[4] = zeljeni_dani_str.capitalize()
    projekcije_f.upis_projekcija()
    print("Uspešno ste izmenili projekciju!")
    meni.rukovanje_projekcijama()

def izmena_vremena_pocetka(zeljena_projekcija, zeljena_sifra):
    vreme_trajanja_filma = ""
    for film in projekat.linije_filmova:
        if zeljena_projekcija[5] == film[1]:
            vreme_trajanja_filma = film[3]
            break
    minimalno_vreme_pocetka = datetime.datetime.strptime(zeljena_projekcija[3], '%H:%M') - datetime.timedelta(minutes=eval(vreme_trajanja_filma))
    novo_vreme = input("Unesite novo vreme početka projekcije.\nImajte na umu da film traje "
                       + vreme_trajanja_filma + " minuta, a završava se u " + zeljena_projekcija[3] + ": ")
    if novo_vreme == "":
        meni.rukovanje_projekcijama()
    try:
        if datetime.datetime.strptime(novo_vreme, '%H:%M') > minimalno_vreme_pocetka:
            print("Projekcija mora početi ranije zbog dužine filma!")
            izmena_vremena_pocetka(zeljena_projekcija, zeljena_sifra)
        else:
            if novo_vreme[3:5] == "00" or novo_vreme[3:5] == "30":
                for projekcija in projekat.projekcije:
                    if projekcija == zeljena_projekcija:
                        projekcija[2] = novo_vreme
                        projekcije_f.upis_projekcija()
                        print("Uspešno ste izmenili projekciju!")
                        meni.rukovanje_projekcijama()
            else:
                print("Početak projekcije mora biti u hh:00 ili hh:30!")
                izmena_vremena_pocetka(zeljena_projekcija, zeljena_sifra)
    except ValueError:
        print("Niste uneti vreme u odgovarajućem formatu(hh:mm)!\nPokušajte ponovo.")
        izmena_vremena_pocetka(zeljena_projekcija, zeljena_sifra)
def izmena_dana(zeljena_projekcija, zeljena_sifra):
    zeljeni_dani = []
    zeljeni_dani_str = input("Unesite nove dane(dan1, dan2, dan3...): ")
    if zeljeni_dani_str == "":
        meni.rukovanje_projekcijama()
    zeljeni_dani_str = zeljeni_dani_str.lower()
    zeljeni_dani = zeljeni_dani_str.split(", ")
    for dan in zeljeni_dani:
        if izvestaji_f.provera_unetog_dana(dan) == False:
            izmena_dana(zeljena_projekcija, zeljena_sifra)
    for projekcija in projekat.projekcije:
        if projekcija == zeljena_projekcija:
            projekcija[4] = zeljeni_dani_str.capitalize()
    projekcije_f.upis_projekcija()
    print("Uspešno ste izmenili projekciju!")
    meni.rukovanje_projekcijama()


def izmena_cene(zeljena_projekcija, zeljena_sifra):
    cena_odgovarajuca = False
    nova_cena = ""
    while cena_odgovarajuca == False:
        nova_cena = input("Unesite novu cenu(mora biti ceo broj koji se završava sa nulom): ")
        try:
            eval(nova_cena)
            if eval(nova_cena) % 10 != 0  and type(eval(nova_cena)) == int:
                print("Niste uneli cenu u odgovarajućem formatu!")
            else:
                try:
                    int(nova_cena)
                    cena_odgovarajuca = True
                    break
                except ValueError:
                    print("Morate uneti cenu u odgovarajućem formatu!")
        except NameError:
            print("Morate uneti cenu u odgovarajućem formatu!")
    for projekcija in projekat.projekcije:
        if projekcija == zeljena_projekcija:
            projekcija[6] = str(int(nova_cena))
            break
    projekcije_f.upis_projekcija()
    print("Uspešno ste izmenili projekciju!")
    meni.rukovanje_projekcijama()


def izmena_filma_projekcije(zeljena_projekcija, zeljena_sifra):
    film_nadjen = False
    novi_film = ""
    while film_nadjen == False:
        novi_film = input("Unesite ime novog filma: ")
        for film in projekat.linije_filmova:
            if film[1] == novi_film:
                film_nadjen = True
                break
        if film_nadjen == False:
            print("Nije pronađen nijedan film u našoj bazi sa datim imenom!\nPokušajte ponovo.")
    for projekcija in projekat.projekcije:
        if projekcija == zeljena_projekcija:
            projekcija[5] = novi_film
            break
    projekcije_f.upis_projekcija()
    print("Uspešno ste izmenili projekciju!")
    meni.rukovanje_projekcijama()

def ispis_projekcija():
    print("{0:^7}|{1:^6}|{2:^15}|{3:^13}|{4:^30}|{5:^30}|{6:^6}".format("Šifra", "Sala", "Vreme početka", "Vreme kraja",
                                                                        "Dani projekcije", "Film", "Cena"))
    for projekcija in projekat.projekcije:
        sifra = projekcija[0]
        sala = projekcija[1]
        vreme_pocetka = projekcija[2]
        vreme_kraja = projekcija[3]
        dani = projekcija[4]
        film = projekcija[5]
        cena = projekcija[6]
        print("{0:^7}|{1:^6}|{2:^15}|{3:^13}|{4:^30}|{5:^30}|{6:^6}".format(sifra, sala, vreme_pocetka,
                                                                            vreme_kraja,
                                                                            dani, film, cena))
    meni.rukovanje_projekcijama()