



// let fruits = ['apples', 'bananas', 'plums']
// let index = 0
// console.log(fruits[index++]) // apples
// index = 0
// console.log(fruits[++index]) // bananas



// function randint(a, b) {
//     return Math.floor(a + Math.random()*(b-a+1))
// }
// function randchoice(arr) {
//     let index = Math.floor(Math.random()*arr.length)
//     return arr[index]
// }

// let i = 0
// let fruits = ['apples', 'bananas', 'plums']
// while (i < 100) {
//     // console.log(Math.floor(Math.random()*10))
//     // console.log(Math.random()*2-1)
//     // console.log(randint(5, 10))
//     console.log(randchoice(fruits))
//     i++
// }



// while (true) {
// }

// let i = 0
// for (; i < 10; ++i) {
// }

// for (;;) {
//     break
// }



// let fruits = ['plums', 'cherries', 'apples', 'bananas', 'zucchini']
// fruits.sort()
// console.log(fruits)

let nums = [10, 20, 102]
nums.sort() // sorts by alphabetical order by default
nums.sort(function(a, b) {
    if (a < b) {
        return -1
    } else if (a > b) {
        return 1
    } else {
        return 0
    }
})
console.log(nums)



// function double_numbers(nums) {
//     for (let i=0; i<nums.length; ++i) {
//         nums[i] = nums[i]*2
//     }
// }
// nums = [1, 2, 3, 4]
// double_numbers(nums)
// console.log(nums)


function perform_operation(nums, f) {
    // for i in range(len(nums)):
    for (let i=0; i<nums.length; ++i) {
        nums[i] = f(nums[i])
    }
}
nums = [1, 2, 3, 4]
// function double(x) {
//     return x * 2
// }
// perform_operation(nums, double)
perform_operation(nums, function(x) {
    return Math.pow(x, 5)
})
console.log(nums)












// let name = prompt("Please enter your name");
// alert("Hello " + name + "! How are you today?");


// let i = 0
// while (i < 100) {
//     alert(i)
//     i += 1
// }