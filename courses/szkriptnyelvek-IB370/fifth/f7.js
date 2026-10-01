class EloFa {
   nev;
   tipus;
   mokusok;

   constructor(nev, tipus = "diofa") {
      this.nev = nev;
      this.tipus = tipus;
      this.mokusok = [];
   }

   uj_vedelmezo(mokusok) {
      if (typeof mokusok == "number") {
         this.mokusok.push(mokusok);
      }
      if (Array.isArray(mokusok)) {
         this.mokusok.push(...mokusok);
      }
   }

   csata(arr) {
      return (
         this.mokusok.reduce((acc, curr) => acc + curr) >
         arr.reduce((acc, curr) => acc + curr)
      );
   }
}
