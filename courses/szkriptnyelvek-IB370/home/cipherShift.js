/*
   Task:
      Implement a Caesar-like cipher. The function takes two parameters:
         - A string (message).
         - A shift number (positive or negative).

      Rules:
         - Only shift letters A–Z and a–z.
         - Preserve case (uppercase stays uppercase).
         - Non-letter characters remain unchanged.

      If shift is larger than 26, wrap around with modulo.

   Example:
      cipherShift("Hello, World!", 3)   // "Khoor, Zruog!"
      cipherShift("abc", -1)            // "zab"
*/

function cipherShift(baseMessage, shiftIndex) {
   if (typeof baseMessage !== "string" || typeof shiftIndex !== "number")
      return;

   shiftIndex %= 26;

   let shiftedMessage = [...baseMessage].reduce((acc, ch) => {
      let code = ch.charCodeAt(0);
      if (65 <= code && code <= 90)
         return (acc += String.fromCharCode(
            ((code - 65 + shiftIndex + 26) % 26) + 65,
         ));
      if (97 <= code && code <= 122)
         return (acc += String.fromCharCode(
            ((code - 97 + shiftIndex + 26) % 26) + 97,
         ));
      return (acc += ch);
   }, "");

   return shiftedMessage;
}

console.log(cipherShift("Hello, World!", 3));
console.log(cipherShift("abc", -1));
