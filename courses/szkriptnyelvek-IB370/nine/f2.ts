function csomagolas(_case: string[], item: string | null): boolean {
   if (item) {
      _case.push(item)
      return true
   }

   return false
}
