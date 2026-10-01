/*
   Készítsd el a karbecsles függvényt, amely paraméterben egy stringet vár, amelynek karakterei az egyes építőelemek sérültségét jelzik: 0, ha nem sérült az elem, 1, ha igen.

   A függvény adja vissza, hogy összesen hány építőelem sérült meg.
      [Input]: "001100010"
      [Output]: 3
      [Magyarázat]: összesen 3 db 1-es szerepel a stringben, azaz 3 építőelem sérült meg.
*/

function karbecsles(epito_elemek) {
   if (typeof epito_elemek !== "string") return;
   return [...epito_elemek].filter((e) => e === "1").length;
}
