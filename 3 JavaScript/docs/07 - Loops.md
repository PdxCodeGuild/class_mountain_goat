
# Loops

- [While-Loops](#while-loops)
- [For-Loops](#for-loops)
  - [Iterating over a String](#iterating-over-a-string)
  - [Iterating over an Array](#iterating-over-an-array)
  - [Iterating over an Object](#iterating-over-an-object)
- [Continue and Break](#continue-and-break)

## While-Loops

While-loops will run while the given condition is `true`.

```javascript
let i = 0
while (i < 5) {
    console.log(i)
    i++
}
```
> 0
> 1
> 2
> 3
> 4


## For-Loops

For-loops have three parts, separated by semi-colons. The first is the **initialization**, the second is the **condition** and the third is the **increment**. These are simply the parts of the `while` loop from above re-arranged.

```javascript
// for (initialization; condition; increment)
for (let i=0; i<5; ++i) {
    console.log(i)
}
```
> 0
> 1
> 2
> 3
> 4

### Iterating over a String

### Iterating over an Array

### Iterating over an Object

iterate over the indices of a string
      01234
let s = 'hello'
for (let i=0; i<s.length; ++i) {
    console.log(s[i])
}

for i in range(len(s)):
    print(s[i])

iterate over the indices of an array
let fruits = ['apples', 'bananas', 'plums']
for (let i=0; i<fruits.length; ++i) {
    console.log(fruits[i])
}

let fruits = ['apples', 'bananas', 'plums']
iterate over the indices
for (i in fruits) {
    console.log(fruits[i])
}
iterate over the elements
for (fruit of fruits) {
    console.log(fruit)
}

let s = 'hello'
iterate over the indices of a string
for (i in s) {
    console.log(s[i])
}
iterate over the characters of a string
for (char of s) {
    console.log(char)
}

## Continue and Break

