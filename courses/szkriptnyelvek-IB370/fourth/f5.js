function fegyverek(arr_of_obj) {
   return arr_of_obj.find(
      (e) => e.erosseg === Math.max(...arr_of_obj.map((n) => n.erosseg)),
   ).nev;
}
