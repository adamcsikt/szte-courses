class Jarmu {
   tipus;
   ero;
   suly;

   constructor(tipus, ero, suly) {
      this.tipus = tipus;
      this.ero = ero;
      this.suly = suly;
   }

   segitseg(jarmu) {
      return this.ero >= jarmu.suly;
   }
}
