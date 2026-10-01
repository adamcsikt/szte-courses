/*
   Készítsd el a templomot_megved függvényt. A függvény feladata, hogy meghatározza, hogy a templom veszélyben van-e a lökdösődő látványromboló lányok miatt, riasztani kell-e a veszélyes pókot, aki egy pillantás alatt megállítja őket, akár a rúgásuk közben is. Így elkezdik lendíteni a lábukat, de meglátják a pókot, és sikítva elmenekülnek, mint bárki gyakorlatról ezen nehéz feladatok miatt. Jaj bocsánat, elkalandoztam.

   Szóval a függvénynek két paramétere van.
      - a templom közelébe érkezők adatai string formában (pl. egy kamera képének az eredmény valamilyen formátumban, stringként).
      - egy függvény, amely egy AI modell alapú számítást végez a bemeneti stringen, és visszaad egy másik stringet (az eredményt).

   Tehát a függvény feladata összefoglalva:
      - hogy az 1. paraméterben kapott stringet átalakítsa olyan formátumra, amit az AI modell megért.
      - meghívja az AI modellt az átalakított paraméterrel
      - feldolgozza az AI modell eredményét, ami alapján visszaad egy logikai értéket, hogy kell-e riasztani a pókot.

   Tudnivalók:
      - Az AI modellnek olyan stringet kell átadni, aminek se az elején, se a végén nincs felesleges whitespace karakter
      - Az AI modell egy stringet ad vissza. Akkor kell riasztani a pókot, ha az alábbiak (legalább) egyike teljesül:
         - a szöveg L betűvel kezdődik vagy L betűvel végződik (csak nagy L)
         - a szöveg tartalmazza a L4N70K részstringet, esetleg úgy, hogy a végén kezdődik és az elején fejeződik be (pl. 0KBBBBBBL4N7), itt az L4N70K eleje L4N7 a string végén található, majd folytatódik a string elején (0K)
*/

function templomot_megved(str, callback) {
   if (typeof str !== "string") return false;
   if (typeof callback !== "function") return false;

   let res = callback(str.trim());
   if (res.startsWith("L") || res.endsWith("L")) return true;
   if ((res + res).includes("L4N70K")) return true;

   return false;
}
