function csomagolas(mennyiseg) {
   return new Promise((resolve, reject) => {
      if (mennyiseg < 10) {
         resolve(mennyiseg);
      } else {
         reject("Túl sok csomag!");
      }
   });
}

function elindul(csomagmennyiseg) {
   csomagolas(csomagmennyiseg)
      .then(() => console.log("SIKERES CSOMAGOLAS!"))
      .catch((e) => console.log(e));
}
