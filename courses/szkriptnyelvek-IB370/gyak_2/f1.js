/*
   Készítsd el az epites függvényt, amely paraméterben egy számot vár, ami megmondja, hogy mennyi ideig tartott az építés. A függvény írja ki ennyi alkalommal a képernyőre, hogy *epit*.

   Előfordulhat, hogy a függvény nem számot kap paraméterként. Ilyen esetben a függvény ne csináljon semmit.
*/

function epites(number) {
   if (typeof number !== "number") return;
   for (let i = 0; i < number; i++) {
      console.log("*epit*");
   }
}
