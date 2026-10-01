# Alapfeladat

A repozitóriumban találhatsz egy Python nyelven írt programot. Ezt kellene magadnak letölteni, tesztelni, és a tesztek eredménye alapján javítani. A program egy játék, amelyben műkincsrablót alakítunk. A játéknak csak egy része van most a fájlban az egyértelműség miatt, két függvény, ezek igen egyszerűek, és önálló kimenetük nem függ a véletlentől. 

# GitLab dokumentáció - tesztelés:

Hozz létre egy `Mukincs` mérföldkövet a projekthez, amelynek határideje legyen idén július 20.! A projektben készíts egy `bug` címkét is, tetszőleges színnel!

Hozz létre egy új issue-t `hxxxxxx_test` néven, ahol a hxxxxxx a saját h-s azonosítódat jelöli. A projektben már létezik egy Mukincs mérföldkő, ehhez rendeld hozzá az issue-t, és rendeld magadhoz is!
Az issue határideje legyen idén július 20.!

Ehhez az issue-hoz hozz létre egy új merge requestet is, amely automatikusan létrehoz egy branch-et! Ezeket ne nevezd át! A merge request is tartozzon a Mukincs mérföldkőhöz.

# Klónozás és előkészítés

Klónozd a projektet a számítógépre, és válts a korábban létrehozott test branch-re!
Érd el git konfigurációs parancsokkal, hogy a saját neveden és saját e-mail címeddel (teljes név, egyetemi e-mail) történjenek a későbbi kommitjaid!

# Gitignore és virtuális környezet

Készítsd el a .gitignore fájlt, ami szűri a `.`-al kezdődő fájlnevek feltöltését, a gitignore-t a kezdő `.` ellenére viszont fel kell tenni! Ezen kívül a `__pycache__` mappát is szűrje ki.

Készítsd el a `requirements.txt` fájl, ami a `pytest` csomagot köti ki feltételnek! Érd el, hogy ez igen, de a viruális környezet maga ne kerüljön fel git-re!

# Tesztelési feladat – Két függvény vizsgálata `pytest`-tel

A teszteket a fájl mellé (az importoknak működniük kell), egy `test_mukincs.py` fájlba hozd létre! A teszteket érdemes lehet rendszeresen kommitálnod és pusholnunk a saját branchedre, de ez nem kötelező. Pont viszont csak a giten fent lévő tesztekért kapható.

Az alábbi két függvényt kell `pytest` segítségével tesztelni. Ha a bemenetek általánosan vannak megadva, neked kell kitalálni a konkrét értékeket, amelyek megfelelnek az egyes helyzeteknek. A kimenetek viszont pontosan meg vannak határozva mindenhol. Ha ez nem így van a kódban, a specifikációt kell helyesnek tekinteni.

---

## 1. `sikeres_betores()` – Megvizsgálja, hogy sikerül-e a tolvajnak betörni a múzeumba.

Ez a függvény egy sztringet kap a tolvaj típusával ("settenkedő" vagy "akrobata"). Emellett kap két listát, amik
sztringekből állnak. Az elsőben a tolvaj felszerelése van (pl. "hús", "hacker eszköz"). A második listában akadályok
vannak, amiket le kell küzdeni (pl. "őrkutya", "őr"). A függvény egy igaz/hamis értéket ad vissza attól függően,
hogy a tolvaj be tud-e jutni a múzeumba. A különböző akadályokhoz más-más eszköz kell. Minden akadály felhasználja
az eszközét, kivéve a hacker eszköznél, amely megmarad.

Az őrkutyához hús szükséges, a lézerhez spray (amitől látható lesz a lézer) és hacker eszköz, az őrhöz pedig altató.
A tolvaj típusa adhat könnyítést: a settenkedőnek nem kell az őrökkel törődnie, nem kell altató a leszerelésükhöz.
Az akrobatának nem kell hacker eszköz a lézerekhez, elég csupán egy spray.

Példa hívás (az akrobata visz két húst, amiből egyet fog felhasználni az őrkutyára, és van nála két spray a két lézerre, így sikeresen be fog jutni, mert minden akadályt lekezelt. Az eredmény tehát True.): 

`sikeres_betores("akrobata",["hús","spray","hús","spray"],["lézer","őrkutya","lézer"])`

### Tesztelendő esetek (összesen 4 db):

1. A tolvajunk settenkedő, 1 hús van nála, és 2 őrkutya az akadály.
* **Elvárt visszatérési érték:** `False`
2. A tolvajunk settenkedő, 2 hús van nála, és 1 őrkutya és 1 őr az akadály.
* **Elvárt visszatérési érték:** `True`
3. A tolvajunk akrobata, 2 hús és 2 spray van nála, és 1 őrkutya és 2 lézer az akadály.
* **Elvárt visszatérési érték:** `True`
4. A tolvajunk settenkedő, 2 hús és 2 spray van nála, és 1 őrkutya és 2 lézer az akadály.
* **Elvárt visszatérési érték:** `False`

---

## 2. `mukincsek_atpakolasa()` – Megmondja, hogy miket rabol el a tolvaj.

Ez a függvény két listát vár. Az egyikben sztringek vannak, ezek a múzeum tárgyai. A másik lista a tolvaj táskája. A múzeum tárgyai közül azokat viszi el a tolvaj, amelyek értéke legalább 1000, de nem nagyobb, mint 1400 (mert túl nagy hírverést okozna).
Egy tárgy (sztring) értéke a következőképp alakul:
* Minden (kis vagy nagy) `a` betű 200-at ad hozzá,
* Minden (kis vagy nagy) `e` betű 100-at ad hozzá,
* Minden (kis vagy nagy) `i` betű 300-at ad hozzá,
* Minden (kis vagy nagy) `q` betű 500-at ad hozzá.

A függvény eredménye a táska lista, amit bemenetben kaptunk, bővítve az új ellopott
tárgyakkal, a tárgyak a korábbi lista előfordulási sorrendjében vannak felsorolva.

Példa hívás: 
`mukincsek_atpakolasa(["Painting: Mona Lisa","Faberget Egg","Queen Diadem","Old Pot"],[])`

Az eredmény a következő lesz: `["Queen Diadem"]`

Magyarázat: A "Faberget Egg" összesen 500-at (1\*200+3\*100), az "Old Pot" 0-t ér, így ezek nem elég értékesek. A "Painting: Mona Lisa" összesen 1500-at (3\*200+3\*300) ér, ami túl nagy érték. A "Queen Diadem" értéke 1300 (1\*500+3\*100+1\*300+1\*200), így ezt lopja el csak.

### Tesztelendő esetek (összesen 5 db):

1. A múzeum tartalma ["Old Painting","Faberget Egg","Queen Diadem","Old Pot"], a tolvaj táska
kezdetben üres.
* **Elvárt visszatérési érték:** ["Queen Diadem"]
2. A múzeum tartalma ["Old Painting","Faberget Egg","Old Pot"], a tolvaj táska
kezdetben üres.
* **Elvárt visszatérési érték:** []
3. A múzeum tartalma ["Old Painting","Faberget Egg","Queen Diadem","Old Pot"], a tolvaj táska
kezdetben ["Old Pot"].
* **Elvárt visszatérési érték:** ["Old Pot","Queen Diadem"]
4. A múzeum tartalma ["Painting: Mona Lisa","Faberget Egg","Queen Diadem"], a tolvaj táska
kezdetben üres.
* **Elvárt visszatérési érték:** ["Queen Diadem"]
5. A múzeum tartalma ["Queen Diadem","Old Pot"], a tolvaj táska
kezdetben üres.
* **Elvárt visszatérési érték:** ["Queen Diadem"]

---

# Tesztek feltöltése

Ha megvannak a tesztek, push-old fel őket a branch-edbe! Ezután merge-eld is bele a main-be, a branch-et viszon ne töröld ezzel! A bukó teszt itt nem jelent gondot, sőt, ezen a ponton elvárt, hogy lesz egy bukó teszteseted, ezt fogod ezután kezelni.

# GitLab dokumentáció - javítás:

Ha találsz nem futó esetet, akkor ehhez vegyél fel egy új issue-t hxxxxxx_1 néven a saját h-s azonosítóddal! Egynél több hiba nem kellene, hogy legyen a fenti teszteknél, ha mégis van, mindet ehhez az issue-hoz dokumentáld most, és itt javítsd! Az új issue-hoz rendeld hozzá a bug címkét! A projektben már csináltál egy Mukincs mérföldkövet, ehhez rendeld hozzá az issue-t, és rendeld magadhoz is. Az issue határideje legyen idén július 20.!

Az issue leírásában markdown formátumban add meg, hogy:

- melyik függvénynél jött elő (ez markdown-os főcím legyen, elég a függvény neve)
- majd bullet point felsorolásban 3 elemet:

  ```
	- input: [a hibát okozó input]
	
	- output: [a hibás output]
	
	- leírás: magyar nyelven megfogalmazott hibaleírás
  ```

Ehhez az issue-hoz is hozz létre egy új merge requestet is, amely automatikusan létrehoz egy branch-et. Ezeket ne nevezd át!
Ez a merge request is tartozzon a Mukincs mérföldkőhöz!

# Javítási feladat – a talált hiba kijavítása

Ezután ezt az új branch-et is töltsd le a számítógépedre, ezen folytasd a munkát. Ehhez szükséged lesz a számítógépen lévő adatok frissítésére. Ne felejts el átváltani erre az új branch-re!

Kezeld a hibákat, hogy a korábban megírt tesztek most már hiba nélkül le tudjanak futni. Ez valószínűleg néhány sor átírását jelentheti csak a kódban! A javítás után dokumentáld a fent elkészített issue-ba a megoldásunkat röviden, ha eddig nem tetted!

Ha a tesztelésedben találtál hibát, akkor is itt tudod ezt javítani, a specifikáció (azaz ez a README) írja le, mi a helyes elvárt működés.

# Javítás feltölése

Push-old fel a hxxxxxx_1 issue branch-ébe a javított kódot! Ha sikeresen feltetted a javítást, merge-eld be ezt a branch-et is a main-be! Itt is hagyd meg a branch-et!

# Végső dokumentáció

Bizonyosodj meg róla, hogy lezárultak az issue-k, ha nem, zárd le őket! Zárd le ezután a mérföldkövet is!
