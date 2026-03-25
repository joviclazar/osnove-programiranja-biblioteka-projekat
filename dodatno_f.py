import karte_f
import projekat
import datetime

import termini_f


def provera_lojalnosti(kupac):
    datum_pre_god_dana = datetime.datetime.today() - datetime.timedelta(days=365)
    karte_kupca = []
    potroseno = 0
    for karta in projekat.karte:
        datum_karte = datetime.datetime.strptime(karta[3], '%d.%m.%Y.')
        if karta[0] == kupac and datum_karte > datum_pre_god_dana and karta[4][0] == "K":
            karte_kupca.append(karta)
    for karta in karte_kupca:
        info_kupovina = karta[4].split(".")
        potroseno += eval(info_kupovina[2])
    if potroseno > 5000:
        return True
    else:
        return False

def ponistavanje_rezervacija_30min():
    karte_za_ponistavanje = []
    trenutno_vreme = datetime.datetime.today()
    for karta in projekat.karte:
        if karta[4][0] == "K":
            pass
        else:
            for termin in termini_f.postojeci_termini:
                if (termin[0] + termin[1]) == karta[1]:
                    odgovarajuci_termin = termin
            for projekcija in projekat.projekcije:
                if projekcija[0] == karta[1][:4]:
                    odgovarajuca_projekcija = projekcija
            vreme_projekcije_str = odgovarajuci_termin[2] + odgovarajuca_projekcija[2]
            vreme_projekcije = datetime.datetime.strptime(vreme_projekcije_str, '%d.%m.%Y.%H:%M')
            dozvoljeno_vreme = vreme_projekcije - datetime.timedelta(minutes=30)
            if trenutno_vreme > dozvoljeno_vreme:
                karte_za_ponistavanje.append(karta)
            else:
                pass
    ponistavanje_karata(karte_za_ponistavanje)
    return None

def ponistavanje_karata(karte_za_ponistavanje):
    for karta in karte_za_ponistavanje:
        for termin in termini_f.postojeci_termini:
            if karta[1] == (termin[0] + termin[1]):
                redovi = termin[4].split("|")
                redovi_za_upis = []
                for red in redovi:
                    if red[0] == karta[2][0]:
                        red = [*red]
                        red[ord(karta[2][1]) - ord('A') + 2] = karta[2][1]
                        red = "".join(red)
                        redovi_za_upis.append(red)
                    else:
                        redovi_za_upis.append(red)
                    termin[4] = "|".join(redovi_za_upis)
    termini_f.upis_termina()
    for karta in projekat.karte:
        if karta in karte_za_ponistavanje:
            projekat.karte.remove(karta)
    karte_f.upisivanje_karata()
    return None

def ispis_sedista_matrica(redovi):
    for red in redovi:
        lista_sedista = []
        for sediste in red[1]:
            lista_sedista.append(sediste)
        print("Red " + red[0] + ": " + " ".join(lista_sedista))
    return None