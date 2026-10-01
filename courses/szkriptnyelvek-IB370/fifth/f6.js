class Fa {
   tipus;
   szin;
   kor;
   erosseg;
   fold_minoseg;

   constructor(tipus, szin, kor, erosseg, fold_minoseg) {
      this.tipus = tipus;
      this.szin = szin;
      this.kor = kor;
      this.erosseg = erosseg;
      this.fold_minoseg = fold_minoseg;
   }

   ido() {
      this.kor++;
   }

   termes() {
      return (
         Math.pow(this.erosseg, 1.3) +
         this.erosseg * this.fold_minoseg -
         this.kor
      );
   }
}

class KekFa extends Fa {
   constructor(tipus, kor, erosseg, fold_minoseg) {
      super(tipus, "kek", kor, erosseg, fold_minoseg);
   }

   termes() {
      return (
         (Math.pow(this.erosseg, 1.3) +
            this.erosseg * this.fold_minoseg -
            this.kor) *
         2
      );
   }
}
