function dolgozok(obj_of_arr) {
   return (
      Object.entries(obj_of_arr)
         .map(([key, value]) => Math.min(...value))
         .reduce((acc, curr) => acc + curr, 0) / Object.keys(obj_of_arr).length
   );
}

console.log(
   dolgozok({
      takarito: [47, 23, 61],
      bohoc: [37, 25, 41, 22],
      allatidomar: [29, 31, 27, 33],
      artista: [16, 21],
      epito: [51, 32, 52, 35, 29, 71],
   }),
);
