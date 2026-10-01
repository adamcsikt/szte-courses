/*
   Készítsd el a templomEpites függvényt, amely a tervek (a függvény paraméterei) alapján eldönti, hogy a templom megépíthető-e, vagy esetleg még csiszolni kell a terveken. A függvény paraméterei (ebben a sorrendben):
      - a rendelkezésre álló hosszútéglák száma
      - a rendelkezésre álló tömörtéglák száma
      - a templom tervrajza (szöveg)

   Szabályok:
      - A templomnak legalább 10 egységnyi nagyságúnak kell lennie, azaz a tervrajz legalább ennyi karakterből álljon
      - A tervrajz tartalmazza a felhasználni tervezett hosszútéglákat (H) és tömörtéglákat (T). A stringben lehetnek egyéb karakterek is, azok egyéb építőelemeket tartalmaznak (azt be tudjuk szerezni, azzal nem kell foglalkoznunk most).

   Figyelem! A string kisbetűket és nagybetűket is tartalmazhat, mind a kettő érvényes, ráadásul akár vegyesen is jöhetnek!

   A függvény adjon vissza igazat, ha a templom megépítését elkezdhetjük (elég nagy a templom alapterülete és van elég hosszútéglánk és van elég tömörtéglánk), hamisat egyébként.

   A híres régész néha picit figyelmetlen, és elhagyja a tervrajzot (nem kapunk ilyen paramétert). Ilyen esetben a függvény térjen vissza undefined-dal.

      [Input]: 9, 4, "HHTHtQtHhhPTHH"
      [Output]: true
      [Magyarázat]: a tervrajz alapján összesen 8 hosszútégla (H) és 4 tömörtégla (T) kell. Hosszútéglából 9, míg tömörtéglából 4 áll rendelkezésre (első két paraméter), szóval a templom megépíthető. (a szövegben a Q-t és a P-t figyelmen kívül hagytuk).
*/

function templomEpites(num_hosszuTegla, num_tomorTegla, tervrajz) {
   if (!tervrajz) return undefined;
   if (typeof tervrajz !== "string" || tervrajz.length < 10) return false;
   if (
      typeof num_hosszuTegla !== "number" ||
      typeof num_tomorTegla !== "number"
   )
      return false;

   const { h, t } = [...tervrajz.toLowerCase()].reduce(
      (acc, ch) => {
         if (ch === "h") acc.h++;
         else if (ch === "t") acc.t++;
         return acc;
      },
      { h: 0, t: 0 },
   );

   return num_hosszuTegla >= h && num_tomorTegla >= t;
}
