class Utazas {
   _tavolsag;
   _celpont;

   constructor(tavolsag, celpont) {
      this._tavolsag = tavolsag;
      this._celpont = celpont;
   }

   kozeledes(tav) {
      this._tavolsag = Math.max(this._tavolsag - tav, 0);
   }

   leparkolas() {
      return new Promise((resolve, reject) => {
         console.log("Parkolas folyamatban...");

         this._tavolsag == 0 ? resolve(this._celpont) : reject("PUFF!");
      });
   }
}
