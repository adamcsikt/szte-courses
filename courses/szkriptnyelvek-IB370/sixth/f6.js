class Vampir {
   _nev;
   _szomjassag = 0;
   _aldozatok = [];

   constructor(nev) {
      this._nev = nev;
   }

   nap_vege(arr_of_obj) {
      if (this._szomjassag >= 10) return;
      if (arr_of_obj.length == 0) {
         this._szomjassag += 2;

         if (this._szomjassag >= 10) {
            this._szomjassag = 10;
         }

         return;
      }

      this._aldozatok.push(...arr_of_obj);
      this._szomjassag -= Math.max(
         arr_of_obj.map((e) => e.suly).reduce((acc, curr) => acc + curr / 20),
         0,
      );
   }

   aldozatok() {
      return [
         ...this._aldozatok.sort((a, b) => b.suly - a.suly).map((e) => e.nev),
      ];
   }
}
