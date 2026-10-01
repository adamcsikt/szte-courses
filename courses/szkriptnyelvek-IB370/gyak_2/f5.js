/*
   Készítsd el a celpont függvényt, amely paraméterben várja az embernél lévő tárgyakat (egy stringként). Amennyiben az embernél van acelcipo, boxkesztyu vagy hegedu, akkor ő egy gyanús embernek számít. Végülis boxolás közben ki akar hegedülni?

   A függvény adjon vissza igazat, ha az ember gyanús, hamisat egyébként.
      [Input]: "kes-szablya-pisztoly-atombomba-granat"
      [Output]: false
      [Magyarázat]: miért lenne gyanús az ember? nincs nála se acélcipő, se boxkesztyű, se hegedű.

      [Input]: "hegedutok es autogumi es ragaszto es ollo"
      [Output]: true
      [Magyarázat]: bár az emberke megpróbálja a hegedűt álcázni, de valójában ott van nála a hegedű, ezért     gyanús.

      [Input]: "viragcserepautogumihangszerfenyezoboxkesztyualma"
      [Output]: true
      [Magyarázat]: az emberünknél boxkesztyű található.
*/

function celpont(objects_string) {
   if (typeof objects_string !== "string") return;
   if (
      objects_string.includes("acelcipo") ||
      objects_string.includes("boxkesztyu") ||
      objects_string.includes("hegedu")
   )
      return true;

   return false;
}
