class Cselekves {
   constructor(
      private _nev: string,
      private _gonosz: boolean,
      private _hatasfok: number,
   ) {}

   get nev(): string {
      return this._nev;
   }

   get gonosz(): boolean {
      return this._gonosz;
   }

   get hatasfok(): number {
      return this._hatasfok;
   }
}

class Haditerv {
   readonly nev: string;
   private cselekvesek: Cselekves[];

   constructor(nev: string) {
      this.nev = nev;
      this.cselekvesek = [];
   }

   uj_terv(cselekves: Cselekves): void {
      if (cselekves.gonosz) {
         this.cselekvesek.push(cselekves);
      }
   }

   osszero(): number {
      return [...this.cselekvesek.map((e) => e.hatasfok)].reduce(
         (acc, curr) => (acc += curr),
      );
   }
}
