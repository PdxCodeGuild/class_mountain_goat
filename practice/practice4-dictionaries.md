
# Practice Problems: Dictionaries


## Problem 1

Write a function that returns `True` if the given dictionary has the given key, `False` otherwise.

```python
def has_key(d, key):
    ...
print(has_key({'a': 1, 'b': 2}, 'a')) # True
print(has_key({'a': 1, 'b': 2}, 'c')) # False
```

## Problem 2

Write a function that returns `True` if the given dictionary is empty, `False` otherwise.

```python
def is_empty(d):
    ...
print(is_empty({})) # True
print(is_empty({'a': 1, 'b': 2})) # False
```

## Problem 3

Write a function that finds and returns the **key** for the given **value**, if the value is not in the dictionary, it should return `None`.

```python
def find_key(d, value):
    ...
print(find_key({'a': 1, 'b': 2}, 1)) # a
print(find_key({'a': 1, 'b': 2}, 3)) # None
```

## Problem 4

Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.

```python
def reverse_dict(d):
    ...
print(reverse_dict({'a': 1, 'b': 2})) # {1: 'a', 2: 'b'}
```

## Problem 5

Write a function that mergest two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.

```python
def merge(list1, list2):
    ...
print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}
```


## Problem 6

Write a function that mergest two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.

```python
def merge(list1, list2):
    ...
print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}
```