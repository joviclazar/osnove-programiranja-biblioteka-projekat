import karte_f
import meni
import projekat
import termini_f
import dodatno_f

def biranje_karte():
    odgovarajuce_karte = []
    print("Unesite neophodne atribute karte koju\n"
          "želite da izmenite.")
    sifra_termina = input("Unesite šifru termina karte: ")
    if sifra_termina == "":
        meni.meni_karte_prodavac()
    kupac = input("Unesite korisničko ime registrovanog ili\n"
                  "ime i prezime neregistrovanog kupca karte: ")
    if kupac == "":
        meni.meni_karte_prodavac()
    sediste = input("Unesite sedište koje je rezervisano kartom: ")
    if sediste == "":
        meni.meni_karte_prodavac()
    zeljena_karta = ""
    for karta in projekat.karte:
        if karta[0] == kupac and karta[1] == sifra_termina.upper() and karta[2] == sediste.upper():
            zeljena_karta = karta
            odgovarajuce_karte.append(zeljena_karta)
            break
    if odgovarajuce_karte == []:
        print("Nije pronađena nijedna karta sa unetim atributima!\n"
              "Pokušajte ponovo.")
        biranje_karte()
    else:
        karte_f.ispis_rezervisanih_karata_prodavac(odgovarajuce_karte)
        meni_odabira_promene(zeljena_karta)

def meni_odabira_promene(zeljena_karta):
    opcija = input("[1] Izmena imena kupca\n"
                   "[2] Izmena sedišta\n"
                   "[3] Izmena termina\n"
                   "[0] Natrag\n"
                   "Unesite odgovarajuću opciju: ")
    if opcija == "1":
        izmena_imena_kupca(zeljena_karta)
    elif opcija == "2":
        izmena_sedista(zeljena_karta)
    elif opcija == "3":
        izmena_termina(zeljena_karta)
    elif opcija == "0":
        meni.meni_karte_prodavac()
    else:
        print("Morate uneti odgovarajuću opciju!\nPokušajte ponovo.")
        meni_odabira_promene(zeljena_karta)

def izmena_imena_kupca(zeljena_karta):
    novo_ime = input("Unesite novo ime kupca date karte: ")
    if novo_ime == "":
        meni_odabira_promene(zeljena_karta)
    for karta in projekat.karte:
        if karta == zeljena_karta:
            karta[0] = novo_ime
            break
    karte_f.upisivanje_karata()
    print("Uspešno ste promenili ime kupca date karte!")
    meni.meni_karte_prodavac()

def izmena_sedista(zeljena_karta):
    pred_redovi = []
    redovi = []
    for termin in termini_f.postojeci_termini:
        if (termin[0] + termin[1]) == zeljena_karta[1]:
            pred_redovi = termin[4].split("|")
            break
    for red in pred_redovi:
        red = red.split(".")
        redovi.append(red)
    dodatno_f.ispis_sedista_matrica(redovi)
    novo_sediste = input("Unesite novo sedište za datu kartu: ")
    if novo_sediste == "":
        meni_odabira_promene(zeljena_karta)
    novo_sediste = novo_sediste.upper()
    for termin in termini_f.postojeci_termini:
        if (termin[0] + termin[1]) == zeljena_karta[1]:
            redovi = termin[4].split("|")
            redovi_za_upis = []
            for red in redovi:
                if red[0] == zeljena_karta[2][0]:
                    red = [*red]
                    red[ord(zeljena_karta[2][1]) - ord('A') + 2] = zeljena_karta[2][1]
                    red = "".join(red)
                    redovi_za_upis.append(red)
                else:
                    redovi_za_upis.append(red)
            termin[4] = "|".join(redovi_za_upis)
            redovi = termin[4].split("|")
            redovi_za_upis = []
            for red in redovi:
                if red[0] == novo_sediste[0]:
                    red = [*red]
                    red[ord(novo_sediste[1]) - ord('A') + 2] = "X"
                    red = "".join(red)
                    redovi_za_upis.append(red)
                else:
                    redovi_za_upis.append(red)
            termin[4] = "|".join(redovi_za_upis)
    termini_f.upis_termina()
    izmena_sedista_u_karti(zeljena_karta, novo_sediste)
    print("Uspešno ste promenili sedište za datu kartu!")
    meni.meni_karte_prodavac()

def izmena_sedista_u_karti(zeljena_karta, novo_sediste):
    for karta in projekat.karte:
        if karta == zeljena_karta:
            karta[2] = novo_sediste
            break
    karte_f.upisivanje_karata()
    return None

def izmena_termina_u_karti(zeljena_karta, novi_termin):
    for karta in projekat.karte:
        if karta == zeljena_karta:
            karta[1] = novi_termin
            break
    karte_f.upisivanje_karata()
    return None

def provera_postojanja_termina(novi_termin):
    for termin in termini_f.postojeci_termini:
        if (termin[0] + termin[1]) == novi_termin:
            return True
    return False

def izmena_termina(zeljena_karta):
    novi_termin = input("Unesite novu šifru termina: ")
    if novi_termin == "":
        meni_odabira_promene(zeljena_karta)
    if provera_postojanja_termina(novi_termin.upper()) == False:
        print("Ne postoji termin sa zadatom šifrom!\nPokušajte ponovo.")
        izmena_termina(zeljena_karta)
    novi_termin = novi_termin.upper()
    redovi = []
    for termin in termini_f.postojeci_termini:
        if (termin[0] + termin[1]) == novi_termin.upper():
            pred_redovi = termin[4].split("|")
            for red in pred_redovi:
                redovi.append(red.split("."))
    dodatno_f.ispis_sedista_matrica(redovi)
    novo_sediste = input("Unesite novo sedište za novi termin: ")
    if novo_sediste == "":
        meni_odabira_promene(zeljena_karta)
    if novo_sediste.upper()[1] == "X":
        print("Ne možete zauzeti zauzeto sedište!")
        izmena_termina(zeljena_karta)
    novo_sediste = novo_sediste.upper()
    kartica_lojalnosti = dodatno_f.provera_lojalnosti(zeljena_karta[0])
    if zeljena_karta[4][0] == "K":
        info_kupovina = zeljena_karta[4].split(".")
        cena = karte_f.odredjivanje_cene_karte(novi_termin, kartica_lojalnosti)
        info_kupovina[2] = str(cena)
        zeljena_karta[4] = ".".join(info_kupovina)
    oslobadjanje_starog_sedista(zeljena_karta)
    zauzimanje_novog_sedista(novi_termin, novo_sediste)
    termini_f.upis_termina()
    izmena_termina_u_karti(zeljena_karta, novi_termin)
    izmena_sedista_u_karti(zeljena_karta, novo_sediste)
    print("Uspešno ste izmenili termin karte!")
    meni.meni_karte_prodavac()

def oslobadjanje_starog_sedista(zeljena_karta):
    for termin in termini_f.postojeci_termini:
        if (termin[0] + termin[1]) == zeljena_karta[1]:
            redovi = termin[4].split("|")
            redovi_za_upis = []
            for red in redovi:
                if red[0] == zeljena_karta[2][0]:
                    red = [*red]
                    red[ord(zeljena_karta[2][1]) - ord('A') + 2] = zeljena_karta[2][1]
                    red = "".join(red)
                    redovi_za_upis.append(red)
                else:
                    redovi_za_upis.append(red)
            termin[4] = "|".join(redovi_za_upis)
            break
    return None

def zauzimanje_novog_sedista(novi_termin, novo_sediste):
    for termin in termini_f.postojeci_termini:
        if (termin[0] + termin[1]) == novi_termin:
            redovi = termin[4].split("|")
            redovi_za_upis = []
            for red in redovi:
                if red[0] == novo_sediste[0]:
                    red = [*red]
                    red[ord(novo_sediste[1]) - ord('A') + 2] = "X"
                    red = "".join(red)
                    redovi_za_upis.append(red)
                else:
                    redovi_za_upis.append(red)
            termin[4] = "|".join(redovi_za_upis)
            break
    return None