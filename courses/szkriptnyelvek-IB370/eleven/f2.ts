enum Tipus {
   LANDZSA = "k0",
   KARD = "k1",
   IJ = "t0",
   PISZTOLY = "t1",
}

interface Fegyver {
   readonly nev: string;
   tipus: Tipus;
   allapot: number;
   tulajdonos?: string;
}
