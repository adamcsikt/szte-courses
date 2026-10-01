/*
   Task:
      - Split an array into chunks of given size.

      Rules:
         - Function takes two parameters: an array and a chunk size (positive integer).
         - Return an array of arrays.
         - If chunk size is invalid, return undefined.

   Example:
      arrayChunk([1,2,3,4,5,6,7], 3)   // [[1,2,3],[4,5,6],[7]]
      arrayChunk([1,2,3], 1)   // [[1],[2],[3]]
*/

function arrayChunk(array, chunkSize) {
   if (!Array.isArray(array)) return undefined;
   if (typeof chunkSize !== "number" || chunkSize < 1) return undefined;

   return array.reduce((acc, e, i) => {
      if (i % chunkSize === 0) {
         acc.push([e]);
      } else {
         acc[acc.length - 1].push(e);
      }
      return acc;
   }, []);
}

console.log(arrayChunk([1, 2, 3, 4, 5, 6, 7], 3));
console.log(arrayChunk([1, 2, 3], 1));
