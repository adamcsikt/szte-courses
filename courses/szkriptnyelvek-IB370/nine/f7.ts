enum Szemely {
   KRINTEE,
   MARIA,
   BLOTEI,
   TUVUS
}

enum Felelem {
   SOTETSEG,
   POKOK,
   VAMPIROK,
   SZELLEMEK,
   BEZARTSAG
}

function legbatrabb(k: Felelem[], m: Felelem[], b: Felelem[], t: Felelem[]): Szemely | Szemely[] {
   const persons = [
      { p: Szemely.KRINTEE, f: k },
      { p: Szemely.MARIA, f: m },
      { p: Szemely.BLOTEI, f: b },
      { p: Szemely.TUVUS, f: t }
   ]

   const bravest = persons.filter(e => e.f.length === Math.min(...persons.map(p => p.f.length))).map(e => e.p)

   return bravest.length === 1 ? bravest[0] : bravest
}
