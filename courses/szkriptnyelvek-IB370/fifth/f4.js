class Mokus {
   _szin = "piros";

   get szin() {
      return this._szin;
   }

   set szin(szin) {
      if (szin == "lila") return;
      this._szin = szin;
   }
}
