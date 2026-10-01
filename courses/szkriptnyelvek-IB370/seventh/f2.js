function utazas(arr_of_obj) {
   return arr_of_obj.reduce(
      (acc, uticel) => {
         const mod = uticel.mod;
         const max = acc[mod];
         if (
            acc.hasOwnProperty(mod) &&
            (!max || uticel.tavolsag > max.tavolsag)
         ) {
            acc[mod] = uticel;
         }

         return acc;
      },
      { viz: undefined, fold: undefined, levego: undefined },
   );
}

console.log(
   utazas([
      { nev: "Budapest", tavolsag: 42, mod: "viz" },
      { nev: "Szeged", tavolsag: 64, mod: "fold" },
      { nev: "Gyor", tavolsag: 32, mod: "viz" },
      { nev: "Bekescsaba", tavolsag: 44, mod: "fold" },
      { nev: "Harcoscsaba", tavolsag: 73, mod: "levego" },
      { nev: "Mezokovesd", tavolsag: 101, mod: "fold" },
   ]),
);
