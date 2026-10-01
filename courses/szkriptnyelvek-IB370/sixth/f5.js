class Kisertetkastely {
   _nev;
   _veszelyesseg;
   _tulelok;

   constructor(nev, veszelyesseg) {
      this._nev = nev;
      this._veszelyesseg = veszelyesseg;
      this._tulelok = [];
   }

   uj_tulelo(nev, ido) {
      this._tulelok.push({ nev, ido });
   }

   legbatrabb() {
      return this._tulelok.find(
         (e) => e.ido === Math.max(...this._tulelok.map((e) => e.ido)),
      ).nev;
   }

   gyavak() {
      return [
         ...this._tulelok
            .filter((e) => e.ido < 2)
            .map((e) => e.nev)
            .sort(),
      ];
   }
}
