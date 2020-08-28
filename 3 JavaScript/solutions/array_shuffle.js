


// a b c d e f g
// i         j
// a b c d e f g
//   i   j
// f b c d e a g
//     ij
// f d c b e a g
//     j i
// f d c b e a g
//         i
// f d b c e a g



// fisher-yates shuffle algorithm
function shuffle(arr) {
    for (let i=0; i<arr.length; ++i) {
        let j = Math.floor(Math.random()*arr.length)

        let t = arr[i]
        arr[i] = arr[j]
        arr[j] = t

    }
}




//          0    1    2    3    4    5    6
let arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
shuffle(arr)
console.log(arr)


// let i = 2
// let j = 6

// WRONG WAY =============
// arr[i] = arr[j]
//   0    1    2    3    4    5    6
// ['a', 'b', 'g', 'd', 'e', 'f', 'g']

// arr[j] = arr[i]
//   0    1    2    3    4    5    6
// ['a', 'b', 'g', 'd', 'e', 'f', 'g']


// RIGHT WAY ====================

// let t = arr[i]
//   0    1    2    3    4    5    6
// ['a', 'b', 'c', 'd', 'e', 'f', 'g']
// t = c

// arr[i] = arr[j]
//   0    1    2    3    4    5    6
// ['a', 'b', 'g', 'd', 'e', 'f', 'g']
// t = c

// arr[j] = t
//   0    1    2    3    4    5    6
// ['a', 'b', 'g', 'd', 'e', 'f', 'c']
// t = c
