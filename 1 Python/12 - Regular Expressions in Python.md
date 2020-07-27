# Regular Expressions in Python

1. [Raw Strings: `r''`](#raw-strings-r)
2. [Match: `re.match(pattern, text)`](#match-rematchpattern-text)
3. [Search: `re.search(pattern, text)`](#search-researchpattern-text)
4. [Splitting: `re.split(pattern, text)`](#splitting-resplitpattern-text)
5. [Find All: `re.findall(pattern, text)`](#find-all-refindallpattern-text)
6. [Compiling Regular Expressions](#compiling-regular-expressions)

You can find out more about regular expressions [here](https://docs.python.org/3.6/howto/regex.html#regex-howto) and [here](https://docs.python.org/3.6/library/re.html#re-syntax).

## Raw Strings: `r''`

When writing regular expressions in Python as string literals, you should put an `r` before your string literal, so you can more easily write and read backslashes.

```python
s1 = 'we can\'t write \\ as easily, but escapes \' work'
s2 = r'we can write \ more easily, but escapes \" dont work'
print(s1) # we can't write \ as easily, but escapes ' work
print(s2) # we can write \ more easily but escapes \" dont work
```

## Match: `re.match(pattern, text)`


```python
import re
result = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
result.group(0)     # The entire match 'Isaac Newton'
result.group(1)     # The first parenthesized subgroup 'Isaac'
result.group(2)     # The second parenthesized subgroup 'Newton'
result.group(1, 2)  # Multiple arguments give us a tuple ('Isaac', 'Newton')
```




## Search: `re.search(pattern, text)`







TODO







`match` and `search` both use a regular expression to find occurrences of a pattern in a string. The difference between them is that `match` only checks for a match at the beginning of a string, while `search` searches the entire string.

```python
import re
re.match("c", "abcdef")    # no match
re.search("c", "abcdef")   # match
re.search("^c", "abcdef")  # no match
re.search("^a", "abcdef")  # match
```

If the pattern isn't found, the result will be `None`, allowing us to use these functions in an `if` clause.

```python
import re
regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24"):
    ...
```

We can also use `match` and `search` to find the location and text that was matched.

- `start` returns the start of the match
- `end` returns the end of the match
- `group()` and `group(0)` return the full match
- `group(1)`, `group(2)`, etc return the capture groups in order from left to right


```python
import re
regex = r"([a-zA-Z]+) (\d+)"
result = re.search(regex, "June 14")

print(result.start()) # the beginning of the match, 0
print(result.end()) # the end of the match, 7

print(result.group()) # same as result.group(0), 'June 14'
print(result.group(1)) # 'June'
print(result.group(2)) # '24'
```

## Splitting: `re.split(pattern, text)`

`split` works just like it does with strings, but allows for regular expressions rather than splitting on a particular string.

```python
import re
s = "Hello! Is this a question? This is a statement."
print(re.split('[.?!]', s))
```

## Find All: `re.findall(pattern, text)`

TODO

## Compiling Regular Expressions

`compile` allows us to 'compile' a regular expression, this allows us to use special syntax when defining the regex, and allows us to re-use a regex without re-writing it.

```python
import re
reg_exp = re.compile(r'Hello, (\w+)', re.I)
match = reg_exp.search('Why hello, Alice.')
 # find the position of the first match
match.start()  # 4
```





