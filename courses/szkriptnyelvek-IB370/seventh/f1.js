class Mikulas {
   constructor(len, name = "Miklos") {
      this.szakallhossz = len;

      this.nev = name;
      this.ajandekok = [];
   }

   get szakallhossz() {
      return `${this._szakallhossz} cm`;
   }

   set szakallhossz(len) {
      if (typeof len !== "number") {
         this._szakallhossz = 10;
         return;
      }

      this._szakallhossz = Math.max(10, len);
      return;
   }

   beszerez(presents) {
      Array.isArray(presents)
         ? this.ajandekok.push(...presents)
         : this.ajandekok.push(presents);
   }

   borotvalkozik() {
      this._szakallhossz = Math.sqrt(this._szakallhossz);
   }

   info() {
      return `${this.nev} a mikulas ${this.szakallhossz} hosszu szakallal rendelkezik, es ${this.ajandekok.length} ajandekkal`;
   }

   csomagol(callback) {
      const packaged = this.ajandekok.map((present) => {
         return {
            felado: this.nev,
            tartalom: present,
         };
      });

      if (typeof callback === "function") {
         callback(packaged);
      }

      return packaged;
   }
}
