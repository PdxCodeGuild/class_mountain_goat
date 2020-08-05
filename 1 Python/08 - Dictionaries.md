# Dictionaries

**Dictionaries** or 'dicts'  provide an unordered, mutable, sequence of key-value pairs or a mapping between keys and values. For more information check the [official docs](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict). Keys have to be unique, values do not. Any _immutable_ value (int, float, string, tuple) can be a key, thus lists and other dicts can't be keys. Values can be any type.

- [Defining Dictionaries](#defining-dictionaries)
- [Accessing a Value with a Key: `dict[key]`](#accessing-a-value-with-a-key-dictkey)
- [Adding a Key-Value Pair: `dict[key] = value`](#adding-a-key-value-pair-dictkey--value)
- [Updating a Key-Value Pair: `dict[key] = value`](#updating-a-key-value-pair-dictkey--value)
- [Removing a Key-Value Pair: `del dict[key]`](#removing-a-key-value-pair-del-dictkey)
- [Checking if a Key Exists: `key in dict`](#checking-if-a-key-exists-key-in-dict)
- [Combining Dictionaries: `dict1.update(dict2)`](#combining-dictionaries-dict1updatedict2)
- [Retrieving Keys and Values](#retrieving-keys-and-values)
- [Order](#order)
- [Conversions](#conversions)


## Defining Dictionaries

Dictionary literals are written using curly braces, and key-value pairs defined with colons and separated by commas.

```python
{'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
```

## Accessing a Value with a Key: `dict[key]`

The values of a dictionary are accessed by using the square-brackets with the key, similarly to how we access a specific element from a list using its index.

```python
product_to_price = {'apple': 1.0, 'banana': 1.5, 'pear': 0.75}
print(product_to_price['apple'])  # 1.0
print(product_to_price['pear'])  # 0.75
print(product_to_price['grapes'])  # Throws KeyError
```

## Adding a Key-Value Pair: `dict[key] = value`

```python
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price['apple'] = 2.0
print(product_to_price)  # {'apple': 2.0, 'pear': 1.5, 'grapes': 0.75}
```

## Updating a Key-Value Pair: `dict[key] = value`

Values can then be added or updated by using the assignment operator `=`.

```python
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price['banana'] = 0.25
print(product_to_price) # {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75}
```

## Removing a Key-Value Pair: `del dict[key]`

You can delete a key-value pair using the `del` operator.

```python
product_to_price = {'apple': 1.0, 'banana': 1.5, 'pear': 0.75}
del product_to_price['apple']
print(product_to_price) # {'banana': 1.5, 'pear': 0.75}
```

## Checking if a Key Exists: `key in dict`

To check if a dictionary contains a key, use `in`

```python
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
if 'apple' in product_to_price:
    print('apple ' + str(product_to_price['apple'])) # 'apple 1.0'
```

## Combining Dictionaries: `dict1.update(dict2)`

To combine two dictionaries, use the `.update()` type method. Note that it changes the given dict and does not return a new one.

```python
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price.update({'banana': 0.25})
product_to_price  #> {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75}
```

## Retrieving Keys and Values

There are a few type methods that allow you to view different parts of the dictionary. All produce sequences and not proper lists, so cast them to a list to use them normally.

```python
list(product_to_price.keys())  #> ['pear', 'apple', 'grapes']
list(product_to_price.values())  #> [0.75, 1.0, 1.5]
list(product_to_price.items())  #> [('grapes', 0.75), ('apple', 1.0), ('pear', 1.5)]
```

## Order

Dictionaries are unordered; there is no guarantee the same order will come out at each call. Call `sorted()` on the results if you need a stable order.

```python
sorted(product_to_price.keys())  #> ['apple', 'grapes', 'pear']
```

## Conversions

You can cast a sequences of two-tuples to a dictionary using `dict()`. This means `.items()` and `dict()` are inverses.

```python
names_and_fav_colors = [('Alice', 'red'), ('David', 'green')]
print(dict(names_and_fav_colors))  #> {'Alice': 'red', 'David': 'green'}
dict(names_and_fav_colors.items()) == names_and_fav_colors  #> True
```

# Dict Comprehensions

Dict comprehensions also look similar to list comprehensions, but with curly braces and colons.

```py
names_to_ages = {'Amanda': 90, 'David': 50}
names_to_ages = {name: age / 2 for name, age in names_to_ages.items()}
print(names_to_ages) # {'Amanda': 45, 'David': 25}
```
