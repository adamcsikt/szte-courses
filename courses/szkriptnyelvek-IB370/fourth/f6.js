function bazis(arr_of_obj) {
   return arr_of_obj
      .filter((e) => e.tipus === "szorny")
      .map((e) => e.veszelyesseg)
      .reduce((acc, curr) => acc + curr, 0);
}
