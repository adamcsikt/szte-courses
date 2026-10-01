function kereses(obj) {
   return [...Object.values(obj)].reduce((acc, curr) => acc + curr, 0);
}
