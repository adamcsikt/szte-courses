/*
   Készítsd el a toronypar függvényt, amely paraméterben a rossz téglák gyakoriságát, illetve a téglák darabszámát várja (mindkettő egész szám). A függvény visszajelez mindegyik tégla lerakásáról, de a rossz téglákat kihagyja.
      [Input]: 3, 13

      [Output]:
      1. tégla
      2. tégla
      4. tégla
      5. tégla
      7. tégla
      8. tégla
      10. tégla
      11. tégla
      13. tégla

   A fenti példa esetén minden 3. tégla rossz (3, 6, 9, 12). És összesen 13 téglánk van, szóval a megadott formátumban kiírjuk a téglákat, de azokat kihagyjuk, amiknek a száma osztható 3-mal.
*/

function toronypar(rossz_tegla, ossz_tegla) {
   if (typeof rossz_tegla !== "number" || typeof ossz_tegla !== "number")
      return;
   for (let i = 1; i <= ossz_tegla; i++) {
      if (i % rossz_tegla === 0) continue;
      console.log(`${i}. tégla`);
   }
}
