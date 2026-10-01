# Szoftverfejlesztési folyamatok projektmunka

## Hallgató adatai

- Név: Adamcsik Tamás
- Neptun kód: EZZLUX
- h-s azonosító: h446358

## Választott alap projekt:

Színözön

## Megvalósítandó feature-ök

### I. Mentés/Betöltés

Valósítsd meg a mentés-betöltés funkciót!

A mentéstől elvárt, hogy a lemezen, tetszőleges fájlformátumban tárolja el a játék aktuális állását (titkos kód, eddigi tippek és visszajelzések, hátralévő kísérletszám). A betöltés funkció legyen képes a fájlt beolvasni és az alapján folytatni a játékot a megfelelő _game state_-tel.

### IV. Lépésenkénti tippbevitel visszavonással

Az alapjátékban a játékos egyszerre adja meg a teljes tippet. Valósítsd meg azt a módot, amelyben a színeket egyesével kell bevinni, és minden lépésnél lehetőség van visszavonásra!

A bevitel szabályai:
- A játék minden lépésben bekér egy bemenetet, és a szín megadása után megmutatja az eddig összeállított tippet
- Érvényes bemenet egy szín betűjele (`R`, `G`, `B`, `Y`, `M`, `C`), a `mégse` parancs vagy – ha már mind a `CODE_LENGTH` szín meg van adva – a `rendben` parancs
- Ha a játékos `mégse`-t ír, az utoljára hozzáadott szín törlődik; ha még nincs megadott szín, az egész tipp bevitele megszakad és az adott kör újrakezdődik
- Ha már `CODE_LENGTH` szín van megadva, a játék a `rendben` parancsra véglegesíti a tippet; újabb szín megadására a `Nincs több` választ adja
- Érvénytelen bemenet esetén a játék `Tessék?`-kel reagál

#### Példa beviteli folyamat (3 eltalálandó színre):

```
  Tipp összeállítása (mégse = visszavon, rendben = jóváhagy):
  [     ] > R
  [R    ] > G
  [R G  ] > mégse
  [R    ] > B
  [R B  ] > Y
  [R B Y] > rendben
```
