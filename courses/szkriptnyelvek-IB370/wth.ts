const inputs: string[] = [
   'e2k2d1n1e2',
   'k4n2'
]

const reduce_path_distance = (path: string): number => {
   let x: number = 0,
      y: number = 0
   let coords: [typeof x, typeof y][] = [[x, y]]
   let _path = path.split('')

   for (let i = 0; i < _path.length; i += 2) {
      let dir = _path[i]
      let step_count = parseInt(_path[i + 1])

      for (let j = 0; j < step_count; j++) {
         if (dir === 'e') y++
         if (dir === 'd') y--
         if (dir === 'k') x++
         if (dir === 'n') x--

         coords.push([x, y])
      }
   }

   let visited: typeof coords = [coords.shift()!]

   coords.forEach((e) => {
      const idx = visited.findIndex((pos) => {
         return pos[0] === e[0] && pos[1] === e[1]
      })

      if (idx === -1) visited.push(e)
      else visited.length = idx + 1
   })

   // console.log('\ncoords:', coords)
   // console.log('visited:', visited)

   return visited.length - 1
}

inputs.forEach((e) => {
   console.log(`${e}: ${reduce_path_distance(e)}`)
})
