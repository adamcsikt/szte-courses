def sikeres_betores(tolvaj_tipus, eszkozok, vedelmek):
    """Eldönti, hogy a tolvaj be tud-e jutni a múzeumba.
    Az eszközöket felhasználjuk (kivéve a hacker eszközt), és ha valamely védelemre nincs megfelelő eszköz, a betörés meghiúsul.
    Paraméterek: tolvaj_tipus (sztring), eszkozok (sztringekből álló lista), vedelmek (sztringekből álló lista)"""

    eszkoz_keszlet = eszkozok.copy()

    for vedelem in vedelmek:
        # őrkutya
        if vedelem == "őrkutya":
            if "hús" in eszkoz_keszlet:
                eszkoz_keszlet.remove("hús")
            else:
                return False
        # lézer
        elif vedelem == "lézer":
            if "spray" not in eszkoz_keszlet:
                return False
            if tolvaj_tipus != "akrobata" and "hacker eszköz" not in eszkoz_keszlet:
                return False
            # spray fogy, hacker eszköz nem
            eszkoz_keszlet.remove("spray")
        # őr
        elif vedelem == "őr":
            if tolvaj_tipus == "settenkedő":
                continue
            if "altató" in eszkoz_keszlet:
                eszkoz_keszlet.remove("altató")
            else:
                return False

    return True


def mukincsek_atpakolasa(muzeum, taska):
    """A múzeum értékes műkincseit (érték 1000 és 1400 közötti) átrakja a táskába.
    Értékszámítás: a=200, e=100, i=300, q=500
    Paraméterek: muzeum (sztringekből álló lista), taska (sztringekből álló lista)"""

    ertekek = {"a": 200, "e": 100, "i": 300, "q": 500}

    for mu in muzeum:
        ertek = sum(ertekek.get(c, 0) for c in mu.lower())
        if ertek >= 1000 and ertek <= 1400:
            taska.append(mu)

    return taska
