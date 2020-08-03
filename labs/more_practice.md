

# More Practice


## Problem 1: Pretty Numbers

Convert an integer into a pretty string with commas `12345678` to `12,345,678`

## Problem 2: Pretty Bytes

Convert a number of bytes `1567123` into a pretty form `1.5 mb`. The `round` function can take two parameters, the number and the number of decimal places to round to `print(round(1.2345, 2))` will print `1.23`.

## Problem 3: Palindrome

A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a `word that's equal to its own reverse`.


Write a function `check_palindrome(word)` which takes a string, and returns True if the string's a palindrome, or False if it's not.

```
enter a word: racecar
'racecar' is a palindrome
enter a word: palindrome
'palindrome' is not a palindrome
```

## Problem 4: Anagram

Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. `anagram` and `nag a ram`.

Write another function `check_anagram(word1, word2)` that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

1. Convert each word to lower case (`lower`)
2. Remove all the spaces from each word (`replace`)
3. Sort the letters of each word (`sorted`)
4. Check if the two are equal

```
enter the first word: anagram
enter the second word: nag a ram
'anagram' and 'nag a ram' are anagrams
```

