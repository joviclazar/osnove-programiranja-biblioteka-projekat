import meni
import reg_korisnika
import projekat

def ispis_filmova():
    print("   |{0:^30}|{1:^10}|{2:^12}|{3:^20}|{4:^16}|{5:^10}"
          .format("Naziv filma","Žanr", "Trajanje(min)", "Režiser",
                  "Zemlja porekla", "Godina proizvodnje"))
    for linija in projekat.linije_filmova:
        redni_broj = linija[0]
        naziv = linija[1]
        zanr = linija[2]
        trajanje = linija[3]
        reziser = linija[4]
        zemlja = linija[6]
        godina = linija[7]
        print("{0:3}|{1:^30}|{2:^10}|{3:^13}|{4:^20}|{5:^16}|{6:^18}"
              .format(redni_broj,naziv,zanr,trajanje,reziser,zemlja,godina))
    meni_nakon_ispisa()
    meni.povratak_na_pocetni_meni()

def ispis_filmova_po_kriterijumima(odgovarajuci_filmovi):
    print("   |{0:^30}|{1:^10}|{2:^12}|{3:^20}|{4:^16}|{5:^10}"
          .format("Naziv filma","Žanr", "Trajanje(min)", "Režiser",
                  "Zemlja porekla", "Godina proizvodnje"))
    for linija in odgovarajuci_filmovi:
        redni_broj = linija[0]
        naziv = linija[1]
        zanr = linija[2]
        trajanje = linija[3]
        reziser = linija[4]
        zemlja = linija[6]
        godina = linija[7]
        print("{0:3}|{1:^30}|{2:^10}|{3:^13}|{4:^20}|{5:^16}|{6:^18}"
              .format(redni_broj,naziv,zanr,trajanje,reziser,zemlja,godina))
    meni_nakon_ispisa()
    pretraga_filmova()

def meni_nakon_ispisa():
    opcija = input("[1] Pregled opisa filma\n"
                   "[0] Natrag\n"
                   "Unesite željenu opciju: ")
    if opcija == "1":
        while True:
            indeks = input("Unesite redni broj željenog filma: ")
            if indeks == "":
                meni_nakon_ispisa()
            try:
                if eval(indeks) < 1:
                    print("Morate uneti jedan od rednih brojeva filmova.")
                else:
                    ispis_osobina_filma(eval(indeks))
            except NameError:
                print("Morate uneti jedan od rednih brojeva filmova.")
    elif opcija == "0":
        return None
    else:
        print("Unesite odgovarajuć unos!")
        meni_nakon_ispisa()

def pretraga_filmova():
    naziv = ""
    zanr = ""
    min_trajanje = 0
    max_trajanje = 0
    reziser = 0
    zemlja_porekla = ""
    god = ""
    odgovarajuci_filmovi = []
    print("Izaberite kriterijum prema kom želite\n"
          "da pretražujete filmove:\n"
          "[1] Naziv\n"
          "[2] Zanr\n"
          "[3] Duzina trajanja filma\n"
          "[4] Režiser\n"
          "[5] Zemlja porekla\n"
          "[6] Godina proizvodnje\n"
          "[7] Višekriterijumska pretraga\n"
          "[0] Povratak na početni meni")
    opcija = input("Unesite željenu opciju: ")
    if opcija == "1":
        pretraga_filma_po_nazivu()
    elif opcija == "2":
        pretraga_filma_po_zanru()
    elif opcija == "3":
        pretraga_filma_po_trajanju()
    elif opcija == "4":
        pretraga_filma_po_reziseru()
    elif opcija == "5":
        pretraga_filma_po_zemlji()
    elif opcija == "6":
        pretraga_filma_po_godini()
    elif opcija == "7":
        visekriterijumska_pretraga()
    elif opcija == "0":
        meni.povratak_na_pocetni_meni()
    else:
        print("Unesite odgovarajuću opciju!")
        pretraga_filmova()


def pretraga_filma_po_nazivu():
    odgovarajuci_filmovi = []
    naziv = input("Unesite naziv filma: ")
    if naziv == "":
        pretraga_filmova()
    naziv = naziv.lower()
    for film in projekat.linije_filmova:
        if naziv in film[1].lower():
            odgovarajuci_filmovi.append(film)
        else:
            pass
    if odgovarajuci_filmovi == []:
        print("Nije pronađen nijedan film koji odgovara Vašoj pretrazi!\nPokušajte ponovo.")
        pretraga_filma_po_nazivu()
    else:
        ispis_filmova_po_kriterijumima(odgovarajuci_filmovi)

def pretraga_filma_po_zanru():
    odgovarajuci_filmovi = []
    print("Dostupni žanrovi:\n"
          "[1] Komedija\n"
          "[2] Ljubavni\n"
          "[3] Triler\n"
          "[4] Akcioni\n"
          "[0] Natrag")
    opcija = input("Unesite željenu opciju: ")
    if opcija == "1":
        zanr = "Komedija"
    elif opcija == "2":
        zanr = "Ljubavni"
    elif opcija == "3":
        zanr = "Triler"
    elif opcija == "4":
        zanr = "Akcioni"
    elif opcija == "0" or opcija == "":
        pretraga_filmova()
    else:
        print("Unesite odgovarajuću opciju!")
        pretraga_filma_po_zanru()
    for film in projekat.linije_filmova:
        if film[2] == zanr:
            odgovarajuci_filmovi.append(film)
    if odgovarajuci_filmovi == []:
        print("Nije pronađen nijedan film koji odgovara Vašoj pretrazi!\nPokušajte ponovo.")
        pretraga_filma_po_zanru()
    else:
        ispis_filmova_po_kriterijumima(odgovarajuci_filmovi)


def pretraga_filma_po_trajanju():
    odgovarajuci_filmovi = []
    min_trajanje = input("Unesite minimalno trajanje filma u minutima: ")
    if min_trajanje == "":
        pretraga_filmova()
    else:
        try:
            min_trajanje = eval(min_trajanje)
        except NameError:
            print("Morate uneti broj! Pokušajte ponovo.")
            pretraga_filma_po_trajanju()
    max_trajanje = input("Unesite maksimalno trajanje filma u minuzima: ")
    if max_trajanje == "":
        pretraga_filmova()
    else:
        try:
            max_trajanje = eval(max_trajanje)
        except NameError:
            print("Morate uneti broj! Pokušajte ponovo.")
            pretraga_filma_po_trajanju()
    for film in projekat.linije_filmova:
        if eval(film[3]) >= min_trajanje and eval(film[3]) <= max_trajanje:
            odgovarajuci_filmovi.append(film)
        else:
            pass
    if odgovarajuci_filmovi == []:
        print("Nije pronađen nijedan film koji odgovara Vašoj pretrazi!\nPokušajte ponovo.")
        pretraga_filma_po_trajanju()
    else:
        ispis_filmova_po_kriterijumima(odgovarajuci_filmovi)

def pretraga_filma_po_reziseru():
    odgovarajuci_filmovi = []
    reziser = input("Unesite ime i prezime režisera: ")
    if reziser == "":
        pretraga_filmova()
    reziser = reziser.lower()
    for film in projekat.linije_filmova:
        if reziser in film[4].lower():
            odgovarajuci_filmovi.append(film)
        else:
            pass
    if odgovarajuci_filmovi == []:
        print("Nije pronađen nijedan film koji odgovara Vašoj pretrazi!\nPokušajte ponovo.")
        pretraga_filmova()
    else:
        ispis_filmova_po_kriterijumima(odgovarajuci_filmovi)


def pretraga_filma_po_zemlji():
    odgovarajuci_filmovi = []
    zemlja_porekla = input("Unesite zemlju porekla: ")
    if zemlja_porekla == "":
        pretraga_filmova()
    zemlja_porekla = zemlja_porekla.lower()
    for film in projekat.linije_filmova:
        if zemlja_porekla in film[6].lower():
            odgovarajuci_filmovi.append(film)
        else:
            pass
    if odgovarajuci_filmovi == []:
        print("Nije pronađen nijedan film koji odgovara Vašoj pretrazi!\nPokušajte ponovo.")
        pretraga_filma_po_zemlji()
    else:
        ispis_filmova_po_kriterijumima(odgovarajuci_filmovi)

def pretraga_filma_po_godini():
    odgovarajuci_filmovi = []
    godina = input("Unesite željenu godinu proizvodnje filma: ")
    if godina == "":
        pretraga_filmova()
    try:
        int(godina)
    except ValueError:
        print("Morate uneti broj kao godinu!")
        pretraga_filma_po_godini()
    for film in projekat.linije_filmova:
        if godina in film[7]:
            odgovarajuci_filmovi.append(film)
        else:
            pass
    if odgovarajuci_filmovi == []:
        print("Nije pronađen nijedan film koji odgovara Vašoj pretrazi!\nPokušajte ponovo.")
        pretraga_filma_po_godini()
    else:
        ispis_filmova_po_kriterijumima(odgovarajuci_filmovi)


def ispis_osobina_filma(indeks):
    indeks -= 1
    try:
        trazeni_film = projekat.linije_filmova[indeks]
    except IndexError:
        print("Morate uneti jedan od rednih brojeva filmova.")
        meni_nakon_ispisa()
    print("Naziv filma:", trazeni_film[1], "\n" +
          "Žanr:", trazeni_film[2], "\n" +
          "Trajanje:", trazeni_film[3], "min\n" +
          "Režiser:", trazeni_film[4], "\n" +
          "Glavne uloge:", trazeni_film[5], "\n" +
          "Zemlja porekla:", trazeni_film[6], "\n" +
          "Godina proizvodnje filma:", trazeni_film[7] + ".\n"
          "Kratak opis filma:")

    for i in projekat.opisi_filmova[indeks].split("|"):
        print(i)

    while True:
        opcija = input("[1] Pretraga filmova\n"
                       "[2] Višekriterijumska pretraga filmova\n"
                       "[0] Početni meni\n"
                       "Izaberije opciju: ")
        if opcija == "1":
            pretraga_filmova()
        elif opcija == "2":
            visekriterijumska_pretraga()
        elif opcija == "0":
            meni.povratak_na_pocetni_meni()
        else:
            print("Morate uneti jednu od ponuđenih opcija!")


def visekriterijumska_pretraga():
    naziv = ""
    zanr = ""
    min_trajanje = 0
    max_trajanje = 0
    reziser = 0
    zemlja_porekla = ""
    god = ""
    odgovarajuci_filmovi = []
    print("Ušli ste u višekriterijumsku pretragu filmova.\n"
          "Ako želite da preskočite unos određenog krite-\n"
          "rijuma, ostavite prazan unos.")
    naziv = input("Unesite naziv filma: ")
    while True:
        print("Dostupni žanrovi:\n"
              "[1] Komedija\n"
              "[2] Ljubavni\n"
              "[3] Triler")
        opcija = input("Unesite željenu opciju: ")
        if opcija == "1":
            zanr = "Komedija"
            break
        elif opcija == "2":
            zanr = "Ljubavni"
            break
        elif opcija == "3":
            zanr = "Triler"
            break
        elif opcija == "":
            zanr = ""
            break
        else:
            print("Morate uneti odgovarajuću opciju! Pokušajte ponovo.")
    min_trajanje = input("Unesite minimalno trajanje filma u minutima: ")
    if min_trajanje == "":
        min_trajanje = 0
    else:
        min_trajanje = eval(min_trajanje)
    max_trajanje = input("Unesite maksimalno trajanje filma u minutima: ")
    if max_trajanje == "":
        max_trajanje = 999
    else:
        max_trajanje = eval(max_trajanje)
    reziser = input("Unesite ime režisera filma: ")
    zemlja_porekla = input("Unesite zemlju porekla filma: ")
    god = input("Unesite godinu proizvodnje: ")
    for film in projekat.linije_filmova:
        if (naziv in film[1] and zanr in film[2] and eval(film[3]) <= max_trajanje and eval(film[3]) >= min_trajanje and reziser in film[4] and zemlja_porekla in film[5] and god in film[6]):
            odgovarajuci_filmovi.append(film)
    if odgovarajuci_filmovi == []:
        print("Nije pronađen nijedan film koji odgovara Vašoj pretrazi!")
        pretraga_filmova()
    else:
        ispis_filmova_po_kriterijumima(odgovarajuci_filmovi)

def dodavanje_filmova():
    print("Odabrali ste opciju dodavanja filmova.\n"
          "Prazan unos u bilo kom trenutku će Vas\n"
          "vratiti na početni meni.")
    naziv = input("Unesite naziv filma: ")
    if naziv == "":
        meni.meni_menadzera()
    while True:
        print("Odabir žanra:\n"
              "[1] Komedija\n"
              "[2] Ljubavni\n"
              "[3] Triler\n"
              "[4] Akcioni")
        opcija = input("Unesite željenu opciju: ")
        if opcija == "1":
            zanr = "Komedija"
            break
        elif opcija == "2":
            zanr = "Ljubavni"
            break
        elif opcija == "3":
            zanr = "Triler"
            break
        elif opcija == "4":
            zanr = "Akcioni"
            break
        elif opcija == "":
            meni.meni_menadzera()
            break
        else:
            print("Unesite odgovarajuću opciju!")
    duzina = input("Unesite trajanje filma u minutima: ")
    while True:
        if duzina == "":
            meni.meni_menadzera()
            break
        try:
            int(duzina)
            break
        except ValueError:
            duzina = input("Morate uneti ceo broj! Pokušajte ponovo: ")
    reziser = input("Unesite ime režisera filma: ")
    if reziser == "":
        meni.meni_menadzera()
    glavne_uloge = input("Unesite imena glavnih glumaca: ")
    if glavne_uloge == "":
        meni.meni_menadzera()
    zemlja_porekla = input("Unesite zemlju porekla filma: ")
    if zemlja_porekla == "":
        meni.meni_menadzera()
    god = input("Unesite godinu proizvodnje filma: ")
    while True:
        if god == "":
            meni.meni_menadzera()
            break
        try:
            int(god)
            break
        except ValueError:
            god = input("Morate uneti ceo broj! Pokušajte ponovo: ")
    opis_filma = input("Unesite kratak opis filma: ")
    if opis_filma == "":
        meni.meni_menadzera()
    indeks = str(int(projekat.linije_filmova[-1][0]) + 1)   #automatsko dodavanje id filma, poslednji id + 1
    linija_novog_filma = [str(indeks), naziv, zanr, duzina, reziser, glavne_uloge, zemlja_porekla, god]
    projekat.linije_filmova.append(linija_novog_filma)
    opis_filma = opis_filma + "\n"
    projekat.opisi_filmova.append(opis_filma)
    fajl_opisa = open("opisi_filmova.txt", "w", encoding="utf-8")
    for opis in projekat.opisi_filmova:
        fajl_opisa.write(opis)
    fajl_opisa.close()
    filmovi_fajl = open("filmovi.txt", "w", encoding="utf-8")
    for film in projekat.linije_filmova:
        film_upis = "|".join(film) + "\n"
        filmovi_fajl.write(film_upis)
    filmovi_fajl.close()
    print("Uspešno ste dodali film!")
    meni_posle_dodavanja()


def meni_posle_dodavanja():
    opcija = input("Da li želite da dodate još filmova[da/ne]? ")
    opcija.lower()
    if opcija == "da":
        dodavanje_filmova()
    elif opcija == "ne":
        meni.meni_menadzera()
    else:
        print("Morate uneti odgovarajuću opciju! Pokušajte ponovo.")
        meni_posle_dodavanja()

def izmena_filmova():
    indeks = input("Unesite redni broj filma čije\n"
                   "podatke želite da izmenite\n"
                   "(prazan unos za povratak): ")
    if indeks == "":
        meni.meni_menadzera()
    try:
        int(indeks)
        if int(indeks) < 1:
            print("Morate uneti jedan od rednih brojeva filmova!")
            izmena_filmova()
    except ValueError:
        print("Morate uneti jedan od rednih brojeva filmova!")
        izmena_filmova()
    str(indeks)
    for film in projekat.linije_filmova:
        if film[0] == indeks:
            print("Odlučili ste da izmenite film:\n"
                  + film[1] + "|" + film[2] + "|" + film[3] + "|" + film[4] + "|" + film[5] + "|" + film[6] + "|" + film[7],
            "\nPraznim unosom u bilo kom trenutku ćete preskočiti osobinu filma:")
            naziv = input("Unesite novi naziv filma: ")
            if naziv != "":
                film[1] = naziv
            while True:
                opcija = input("[1] Komedija\n"
                                "[2] Triler\n"
                                "[3] Ljubavni\n"
                                "[4] Akcioni\n"
                                "Unesite odgovarajuću opciju: ")
                if opcija == "1":
                    zanr = "Komedija"
                    break
                elif opcija == "2":
                    zanr = "Triler"
                    break
                elif opcija == "3":
                    zanr = "Ljubavni"
                    break
                elif opcija == "4":
                    zanr = "Akcioni"
                    break
                elif opcija == "":
                    zanr = ""
                    break
                else:
                    print("Morate uneti odgovarajuću opciju ili prazan unos za preskakanje!\nPokušajte ponovo.")
            if zanr != "":
                film[2] = zanr
            while True:
                trajanje = input("Unesite novo trajanje filma u minutima: ")
                if trajanje == "":
                    break
                try:
                    int(trajanje)
                    break
                except ValueError:
                    print("Morate uneti ceo broj! Pokušajte ponovo.")
            if trajanje != "":
                film[3] = str(trajanje)
            reziser = input("Unesite novog režisera: ")
            if reziser != "":
                film[4] = reziser
            glavne_uloge = input("Unesite nove glavne uloge: ")
            if glavne_uloge != "":
                film[5] = glavne_uloge
            drzava = input("Unesite novu zemlju porekla filma: ")
            if drzava != "":
                film[6] = drzava
            while True:
                god = input("Unesite novu godinu proizvodnje filma: ")
                if god == "":
                    break
                try:
                    int(god)
                    break
                except ValueError:
                    print("Morate uneti ceo broj! Pokušajte ponovo.")
            if god != "":
                film[7] = str(god) + "\n"
            fajl_filmova = open("filmovi.txt", "w", encoding="utf-8")
            for film in projekat.linije_filmova:
                fajl_filmova.write("|".join(film) + "\n")
            fajl_filmova.close()
            print("Uspešno ste izmenili osobine filma!")
            meni.meni_menadzera()
        else:
            continue
        print("Nije pronađen nijedan film sa unetim rednim brojem! Pokušajte ponovo.")
        izmena_filmova()

def brisanje_filmova():
    indeks = input("Unesite redni broj filma koji\n"
                   "želite da obrišete\n"
                   "(prazan unos za povratak): ")
    if indeks == "":
        meni.meni_menadzera()
    try:
        int(indeks)
    except ValueError:
        print("Morate uneti redni broj filma!")
        brisanje_filmova()
    str(indeks)
    global brojac_linija
    brojac_linija = -1
    for film in projekat.linije_filmova:
        brojac_linija += 1
        if film[0] == indeks:
            global film_promenjiva
            film_promenjiva = film
            print("Odlučili ste da obrišete film:\n"
                + film[1] + "|" + film[2] + "|" + film[3] + "|" + film[4] + "|" + film[5] + "|" + film[6] + "|" + film[7])
            def pod_brisanje_filmova():
                opcija = input("Da li ste sigurni da želite da obrišete ovaj film(da/ne)? ")
                opcija.lower()
                if opcija == "ne":
                    print("Film nije obrisan.")
                    brisanje_filmova()
                elif opcija == "da":
                    projekat.linije_filmova.remove(film_promenjiva)
                    fajl_filmova = open("filmovi.txt", "w", encoding="utf-8")
                    for film in projekat.linije_filmova:
                        fajl_filmova.write("|".join(film) + "\n")
                    fajl_filmova.close()
                    fajl_opisa = open("opisi_filmova.txt", "w", encoding="utf-8")
                    del projekat.opisi_filmova[brojac_linija]
                    for opis in projekat.opisi_filmova:
                        fajl_opisa.write(opis)
                    fajl_opisa.close()
                    print("Film je uspešno obrisan!")
                    meni.rukovanje_filmovima()
                else:
                    print("Morate uneti odgovarajuć unos!")
                    pod_brisanje_filmova()
            pod_brisanje_filmova()
    print("Nije pronađen nijedan film sa unetim indeksom!")
    brisanje_filmova()