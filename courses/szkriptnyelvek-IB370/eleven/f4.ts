class Szemely {
   private nev: string;
   private titulus: string;
   private ero: number;

   constructor(nev: string, titulus: string, ero: number) {
      this.nev = nev;
      this.titulus = titulus;
      this.ero = ero;
   }

   public varazsol() {
      return this.ero > 10;
   }
}

class Saman extends Szemely {
   private sotetSaman: boolean;

   constructor(name: string, ero: number, dark: boolean) {
      super(name, "saman", ero);
      this.sotetSaman = dark;
   }

   varazsol(): boolean {
      return true;
   }
}
