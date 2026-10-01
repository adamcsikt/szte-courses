class Uldozes {
   _datum;
   _veszelyesseg;
   _uldozok = [];

   constructor(datum, veszelyesseg) {
      this._datum = datum;
      this._veszelyesseg = veszelyesseg;
   }

   get datum() {
      return this._datum;
   }

   get veszelyesseg() {
      return this._veszelyesseg;
   }

   uj_uldozo(nev) {
      this._uldozok.push(nev);
   }

   uj_uldozo_csapat(nevek) {
      this._uldozok.push(...nevek);
   }
}
