# Stack

## What is a Set?

A set is a collection of unique, unordered pieces of data. Meaning that there can be no duplicate values and the order does not matter. The data held in a set must be immutable.

## What is the Big O of Set operations?

So long as a the data fits the criteria of a set, it is a great choice for its efficiency. Each of its operations add(), update(), remove(), discard(), clear() have an efficiency of O(1).

This is as fast as a function can be (constant time).

## Sets in Python

### Creating a Set ----

An empty set can be created as follows:

```python
empty_set = set()
print(empty_set)
```

Output:

```python
set()
```

For a set with integers (or other data types):

```python
int_set = {1,2,3,4}
print(int_set)
```

Output:

```python
{1,2,3,4}
```

Sets can also be made using any other immutable data type (or types), such as stings, floats, etc. They cannot be made using lists or dictionaries.

If repeat elements are used they will be dropped from the set.

```python
duplicate_set = {1,1,2,2,3,3,4,4,}
print(duplicate_set)
```

Output:

```python
{1,2,3,4}
```

### Set Functions ----

<span style="color: blue">add()</span> - Used to add a new element to the set.

```python
int_set = {1,2,3,4}
int_set.add(5)
print(int_set)
```

Output:

```python
{1,2,3,4,5}
```

<span style="color: blue">update()</span> - Used to add multiple new elements to a set at once. New elements can be passed as a set or list

```python
int_set = {1,2,3,4}
int_set.update({5,6,7,8})
print(int_set)
```

Output:

```python
{1,2,3,4,5,6,7,8}
```

<span style="color: blue">remove()/discard()</span> - Used to remove an element from the set. The only difference between the two is that remove() raises a KeyError if the element to be removed is not present.

```python
int_set = {1,2,3,4}
int_set.remove(3)
print(int_set)
```

Output:

```python
{1,2,4}
```

remove() and discard() can also both be given multiple elements at once.

<span style="color: blue">clear()</span> - removes all elements from a set

```python
int_set = {1,2,3,4}
int_set.clear()
print(int_set)
```

Output:

```python
set()
```

-[Link Back to Welcome](0-welcome.md)
