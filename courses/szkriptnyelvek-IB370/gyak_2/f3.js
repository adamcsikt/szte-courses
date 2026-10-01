/*
   Készítsd el a szemuvegek függvényt, amely paraméterben egy logikai értéket és egy 0 paraméteres callback függvényt vár. A logikai érték igaz, ha a járókelő észreveszi a tornyot, hamis egyébként. A függvény feladata, hogy meghívja a callback függvényt, ha a járókelő nem vette észre a tornyot.
*/

function szemuvegek(boolean, callback) {
   if (typeof callback !== "function") return;
   if (!boolean) callback();
}
