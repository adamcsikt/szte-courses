enum MunkaTipus {
   ALLAT_TENYESZTES,
   NOVENY_TERMESZTES,
   LAKHELY_ORZES,
}

class Munka {
   private tipus: MunkaTipus;
   private ido: number;
   private _szemely: string;

   constructor(tipus: MunkaTipus, ido: number, _szemely: string) {
      this.tipus = tipus;
      this.ido = ido;
      this._szemely = _szemely;
   }

   get szemely(): string {
      return this._szemely;
   }

   set szemely(new_person: string) {
      this._szemely = new_person;
   }

   nehez(): boolean {
      return this.ido > 30;
   }
}
