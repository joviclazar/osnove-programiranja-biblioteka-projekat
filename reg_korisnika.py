import korisnici_fajl
import meni
import dodatno_f

def registracija_kupaca():
    ime = input("Unesite Vaše ime: ")
    if ime == "":
        meni.meni1()
    prezime = input("Unesite Vaše prezime: ")
    if prezime == "":
        meni.meni1()
    kor_ime = input("Unesite željeno korisničko ime: ")
    if kor_ime == "":
        meni.meni1()
    lozinka = input("Unesite željenu lozinku(barem 6 karatkera i barem 1 cifra): ")
    if lozinka == "":
        meni.meni1()
    provera_broja = False
    for i in lozinka:
        if i.isdigit():
            provera_broja = True
            break

    while len(lozinka) < 7 or provera_broja == False:
        if len(lozinka) < 7:
            lozinka = input("Uneta lozinka je prekratka! Pokušajte ponovo: ")
            if lozinka == "":
                meni.meni1()
        elif provera_broja == False:
            lozinka = input("Uneta lozinka ne sadrži cifru! Pokušajte ponovo: ")
            if lozinka == "":
                meni.meni1()
            provera_broja = any(map(str.isdigit, lozinka))

    for korisnik in korisnici_fajl.korisnici:
        if korisnik[2] == kor_ime:
            print("Izabrano korisničko ime je već zauzeto! Pokušajte ponovo.")
            registracija_kupaca()
        else:
            pass

    korisnik_dodat = (ime + "|" + prezime + "|" + kor_ime + "|" + lozinka + "|" + "k" + "\n")
    korisnici_fajl.upis_korisnika(korisnik_dodat)
    korisnik_dodat_za_listu = []
    korisnik_dodat_za_listu.append(ime)
    korisnik_dodat_za_listu.append(prezime)
    korisnik_dodat_za_listu.append(kor_ime)
    korisnik_dodat_za_listu.append(lozinka)
    korisnik_dodat_za_listu.append("k\n")
    korisnici_fajl.korisnici.append(korisnik_dodat_za_listu)
    print("Uspešno ste se registrovali!")
    prijava()

global trenutni_korisnik
trenutni_korisnik = []
global reg_oznaka

def prijava():
    x = False
    global reg_oznaka
    kor_ime = input("Unesite Vaše korisničko ime(prazan unos za izlaz): ")
    if kor_ime == "":
        meni.meni1()
    lozinka = input("Unesite Vašu lozinku(prazan unos za izlaz): ")
    if lozinka == "":
        meni.meni1()
    for korisnik in korisnici_fajl.korisnici:
        global trenutni_korisnik
        trenutni_korisnik = korisnik
        if korisnik[2] == kor_ime:
            if korisnik[3] == lozinka:
                x = True
                reg_oznaka = korisnik[4]
                if reg_oznaka[0] == "k":
                    print("Uspešno ste se ulogovali kao kupac.")
                    meni.meni_kupca()
                elif reg_oznaka[0] == "p":
                    dodatno_f.ponistavanje_rezervacija_30min()
                    print("Uspešno ste se ulogovali kao prodavac.")
                    meni.meni_prodavca()
                elif reg_oznaka[0] == "m":
                    print("Uspešno ste se ulogovali kao menadžer.")
                    meni.meni_menadzera()
    if x == False:
        print("Uneli ste nepravilno korisničko ime ili lozinku!")
        print("Pokušajte ponovo.")
        prijava()

def izmena_licnih_podataka():
    print("Koji podatak želite da promenite?\n"
          "(korisničko ime nije moguće promeniti!)\n"
          "[1] Ime\n"
          "[2] Prezime\n"
          "[3] Lozinku\n"
          "[0] Natrag")
    opcija = input("Unesite opciju: ")

    if opcija == "1":
        ime = input("Unesite novo ime: ")
        for korisnik in korisnici_fajl.korisnici:
            if korisnik == trenutni_korisnik:
                trenutni_korisnik[0] = ime
                korisnik = trenutni_korisnik
                korisnici_fajl.upis_korisnika("")
        print("Uspešno ste promenili ime.")
        izmena_licnih_podataka()

    elif opcija == "2":
        prezime = input("Unesite novo prezime: ")
        for korisnik in korisnici_fajl.korisnici:
            if korisnik == trenutni_korisnik:
                trenutni_korisnik[1] = prezime
                korisnik = trenutni_korisnik
                korisnici_fajl.upis_korisnika("")
        print("Uspešno ste promenili prezime.")
        izmena_licnih_podataka()
    elif opcija == "3":
        lozinka = input("Unesite novu lozinku: ")
        provera_broja = False
        for i in lozinka:
            if i.isdigit():
                provera_broja = True
                break

        while len(lozinka) < 7 or provera_broja == False:
            if len(lozinka) < 7:
                lozinka = input("Uneta lozinka je prekratka! Pokušajte ponovo: ")
            elif provera_broja == False:
                lozinka = input("Uneta lozinka ne sadrži cifru! Pokušajte ponovo: ")
                for i in lozinka:
                    if i.isdigit():
                        provera_broja = True
                        break

        for korisnik in korisnici_fajl.korisnici:
            if korisnik == trenutni_korisnik:
                trenutni_korisnik[3] = lozinka
                korisnik = trenutni_korisnik
                korisnici_fajl.upis_korisnika("")
        print("Uspešno ste promenili lozinku.")
        izmena_licnih_podataka()
    elif opcija == "0":
        if reg_oznaka[0] == "k":
            meni.meni_kupca()
        elif reg_oznaka[0] == "m":
            meni.meni_menadzera()
        elif reg_oznaka[0] == "p":
            meni.meni_prodavca()
    else:
        print("Unesite odgovorajuću opciju!")
        izmena_licnih_podataka()

def registracija_menadzera():
    ime = input("Unesite ime novog menadžera: ")
    while ime == "":
        ime = input("Morate uneti ime menadžera! Pokušajte ponovo: ")
    prezime = input("Unesite prezime novog menadžera: ")
    while prezime == "":
        prezime = input("Morate uneti prezime menadžera! Pokušajte ponovo: ")
    kor_ime = input("Unesite željeno korisničko ime novog menadžera: ")
    while kor_ime == "":
        kor_ime = input("Morate uneti korisničko ime! Pokušajte ponovo: ")
    lozinka = input("Unesite željenu lozinku novog menadžera \n"
                    "(barem 6 karatkera i barem 1 cifra): ")
    provera_broja = any(map(str.isdigit, lozinka))

    while len(lozinka) < 7 or provera_broja == False:
        if len(lozinka) < 7:
            lozinka = input("Uneta lozinka je prekratka! Pokušajte ponovo: ")
        elif provera_broja == False:
            lozinka = input("Uneta lozinka ne sadrži cifru! Pokušajte ponovo: ")
            provera_broja = any(map(str.isdigit, lozinka))

    for korisnik in korisnici_fajl.korisnici:
        if korisnik[2] == kor_ime:
            print("Izabrano korisničko ime je već zauzeto! Pokušajte ponovo.")
            registracija_menadzera()
        else:
            pass

    korisnik_dodat = (ime + "|" + prezime + "|" + kor_ime + "|" + lozinka + "|" + "m" + "\n")
    korisnici_fajl.upis_korisnika(korisnik_dodat)
    korisnik_dodat_za_listu = []
    korisnik_dodat_za_listu.append(ime)
    korisnik_dodat_za_listu.append(prezime)
    korisnik_dodat_za_listu.append(kor_ime)
    korisnik_dodat_za_listu.append(lozinka)
    korisnik_dodat_za_listu.append("m\n")
    korisnici_fajl.korisnici.append(korisnik_dodat_za_listu)
    print("Uspešno ste registrovali novog menadžera!")
    meni.meni_menadzera()

def registracija_prodavaca():
    ime = input("Unesite ime novog prodavca: ")
    while ime == "":
        ime = input("Morate uneti ime prodavca! Pokušajte ponovo: ")
    prezime = input("Unesite prezime novog prodavca: ")
    while prezime == "":
        prezime = input("Morate uneti prezime prodavca! Pokušajte ponovo: ")
    kor_ime = input("Unesite željeno korisničko ime novog prodavca: ")
    while kor_ime == "":
        kor_ime = input("Morate uneti korisničko ime prodavca! Pokušajte ponovo: ")
    lozinka = input("Unesite željenu lozinku novog prodavca \n"
                    "(barem 6 karatkera i barem 1 cifra): ")
    provera_broja = any(map(str.isdigit, lozinka))

    while len(lozinka) < 7 or provera_broja == False:
        if len(lozinka) < 7:
            lozinka = input("Uneta lozinka je prekratka! Pokušajte ponovo: ")
        elif provera_broja == False:
            lozinka = input("Uneta lozinka ne sadrži cifru! Pokušajte ponovo: ")
            provera_broja = any(map(str.isdigit, lozinka))

    for korisnik in korisnici_fajl.korisnici:
        if korisnik[2] == kor_ime:
            print("Izabrano korisničko ime je već zauzeto! Pokušajte ponovo.")
            registracija_prodavaca()
        else:
            pass

    korisnik_dodat = (ime + "|" + prezime + "|" + kor_ime + "|" + lozinka + "|" + "p" + "\n")
    korisnici_fajl.upis_korisnika(korisnik_dodat)
    korisnik_dodat_za_listu = []
    korisnik_dodat_za_listu.append(ime)
    korisnik_dodat_za_listu.append(prezime)
    korisnik_dodat_za_listu.append(kor_ime)
    korisnik_dodat_za_listu.append(lozinka)
    korisnik_dodat_za_listu.append("p\n")
    korisnici_fajl.korisnici.append(korisnik_dodat_za_listu)
    print("Uspešno ste registrovali novog prodavca!!")
    meni.meni_menadzera()