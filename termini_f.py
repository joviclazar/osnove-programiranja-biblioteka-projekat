import projekat
import datetime


global postojeci_termini
def kreiranje_termina():
    termini_fajl = open("termini_projekcija.txt", "r", encoding="utf-8")
    global postojeci_termini
    postojeci_termini = []
    for linija in termini_fajl.readlines():
        zaseban_termin = []
        zaseban_termin.append(linija[0:4])
        zaseban_termin.append(linija[4:6])
        zaseban_termin.append(linija[7:18])
        zaseban_termin.append(linija[19:20])
        zaseban_termin.append(linija[21:-1])
        postojeci_termini.append(zaseban_termin)
    termini_fajl.close()
    global termini
    termini = []
    for termin in postojeci_termini:
        for projekcija in projekat.projekcije:
            if termin[0] == projekcija[0]:
                datum_vreme_pocetka_str = termin[2] + projekcija[2]
                datum_vreme_pocetka = datetime.datetime.strptime(datum_vreme_pocetka_str, '%d.%m.%Y.%H:%M')
                if datum_vreme_pocetka < datetime.datetime.today():
                    termin[3] = "I"
    try:
        prvo_slovo = ord(postojeci_termini[-1][1][0])
        drugo_slovo = ord(postojeci_termini[-1][1][1])
    except IndexError:
        prvo_slovo = ord('A')
        drugo_slovo = ord('A') - 1
    postojeci_datumi = []
    for i in postojeci_termini:
        postojeci_datumi.append(i[2])
    for projekcija in projekat.projekcije:
        danasnji_datum = datetime.date.today() - datetime.timedelta(days=1)     #zbog petlje
        termin = []
        for i in range(15):
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
            if dan.title() in projekcija[4].title():
                sifra = projekcija[0]
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
                a = "V"
                termin.append(a)
                for sala in projekat.sale:
                    if sala[0] == projekcija[1]:
                        redovi = sala[1]
                    else:
                        pass
                termin.append(redovi)
                if termin[2] in postojeci_datumi:
                    drugo_slovo -= 1
                    pass
                else:
                    postojeci_termini.append(termin)
            termin = []

    upis_termina()

def upis_termina():
    termini_fajl = open("termini_projekcija.txt", "w", encoding="utf-8")
    termini_za_upis = []
    for termin in postojeci_termini:
        termini_za_upis.append(termin[0] + termin[1] + "|" + termin[2] + "|" + termin[3] + "|" + termin[4] + "\n")
    for termin in termini_za_upis:
        termini_fajl.write(termin)
    termini_fajl.close()
    return None