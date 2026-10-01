enum Hangulat {
   DUH = "Düh",
   HARAG = "Harag",
   IZGATOTTSAG = "Izgatottság",
   OROM = "Öröm",
   LELKESEDES = "Lelkesedés"
}


function hangulatCsillapitas(h: Hangulat): void {
   if (h === Hangulat.DUH || h === Hangulat.HARAG) console.log('CSEND LEGYEN!')
}
