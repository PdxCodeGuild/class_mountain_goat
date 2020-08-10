
# Regular Expressions

Regular expressions or 'regex' are a way to match patterns in strings. They can be executed in nearly any programming language. They can be used to validate a phone number or address in an input field on a website, or to find the occurrences of a phrase in a block of text, etc.

- [Regex101](https://regex101.com)
- [RegexOne](https://regexone.com/)
- [RegexLib](https://regexlib.com/)
- [Regexr](https://regexr.com/)
- [Regular Expressions in Python](../1%20Python/docs/Regular%20Expressions%20in%20Python.md)
- [Regular Expressions in JavaScript](../3%20JavaScript/docs/Regular%20Expressions%20in%20JavaScript.md)

--------

- [Overview](#overview)
- [Character Match: `abc`, `.`](#character-match-abc-)
- [Line Match: `^`, `$`](#line-match--)
- [Repeats: `?`, `*`, `+`](#repeats---)
- [Escapes](#escapes)
- [Character Classes](#character-classes)
- [Character Sets](#character-sets)
- [Captures](#captures)
- [Named Captures](#named-captures)


## Overview

- `abc123..` match a character literally
- `.` matches any character except a newline
- `\d` matches any digit character (0-9)
- `\s` matches any whitespace character (space, \t, or \n)
- `\w` matches any word character (A-Z, a-z, 0-9, and _)
- `[]` define a character class
- `^` within a character class, matches everything BUT what follows
- `$` matches the end of a string, or just before the next newline
- `*` matches 0 or more occurrences
- `+` matches 1 or more occurrences
- `?` matches 0 or 1 occurrences

## Character Match: `abc`, `.`

Most characters match themselves.

```re
david s
```
> **david s**<br/>
> David s<br/>
> hello **david s**<br/>
> hello **david s** today<br/>

We can use `.` to match any character.

```re
davi. s
```
> **david s**<br/>
> **davix s**<br/>
> davidd s<br/>

## Line Match: `^`, `$`

- Carrot `^` matches the beginning of a line
- Dollar sign `$` matches the end of a line

```re
^fire
```
> **fire** hydrant<br/>
> no fire here<br/>

```re
fire$
```
> wood **fire**<br/>
> fire wood<br/>


## Repeats: `?`, `*`, `+`

There are some special characters that mark how many times the previous character should repeat.

The `?` character means one or zero times.

```re
rhu?ba?rb
```
> **rhbrb**<br/>
> **rhubrb**<br/>
> **rhubarb**

The `+` character means at least one time.

```re
sna+cks
```
> **snacks**<br/>
> sncks<br/>
> **snaaaaaacks**

The `*` character means zero or more times.

```re
sna*cks
```
> **snacks**<br/>
> **sncks**<br/>
> **snaaaaaacks**

## Escapes

If you want to use any special characters literally, use backslash `\` in front of it.

```re
Hello\.
```
> **Hello.**<br/>
> Hellox

## Character Classes

Groups of characters that are used in the same sorts of ways are called **classes**.

- `.` matches any any character
- `\d` matches digits
- `\s` matches white space (space, tab, newline)
- `\w` matches "word" characters (letters, numbers, and underscore)

Each group still only matches one character, but repeat characters can be used on them.

```re
\d+\s\w+
```
> **12 a5**<br/>
> 1f ap<br/>
> **12\ta**<br/>

## Character Sets

If you want to be more discerning than a whole character class, you can use a **set**. Put all the characters you want to allow in square brackets `[]`. Each set still only matches one character, but repeat characters can be used on them.

```re
[bp]anana
```
> **banana**<br/>
> **panana**<br/>
> pbanana

```re
snack[sx]*
```
> **snacksxsssx**

You can specify **ranges** of characters with dash `-`, so dash must be escaped in a character set. A super common range is all letters `[a-zA-Z]` since `\w` also includes digits.

```re
My Name Is: [a-zA-Z]+
```
> **My Name Is: David**<br/>
> My Name Is: C4t

## Captures

You can group together parts of a match into a **capture**, which is like a "sub-match", using parentheses `()`. You can then use the repeat modifiers on the whole capture.

More useful than that, is when the regular expression library matches text, it will save which parts of the text match each capture by the order they appear (1, 2, etc.). This is always one-indexed.

```re
(hot+)+dogs
```
> **hotdogs**<br/>
> **hothotthotttdogs**

```re
(\d\d\d)-(\d\d\d)-(\d\d\d\d)
```
> **123-456-7890**

## Named Captures

Instead of just remembering the text that matched each capture by the order it appears in the whole regular expression, you can also use a **named capture**. It is still a sub-match specified in parentheses `()`, but with `?P<NAME>` first inside.

```re
(?P<first_name>.+) (?P<last_name>.+)
```
> **bob dole**


