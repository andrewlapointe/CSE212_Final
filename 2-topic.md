# Stack

## What is a Set?

A set is a collection of unique, unordered pieces of data. Meaning that there can be no duplicate values and the order does not matter. The data held in a set must be immutable.

## What is the Big O of Set operations?

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

<span style="color: blue">add()</span> - to add a new element to the set

```python
int_set = {1,2,3,4}
int_set.add(5)
print(int_set)
```

Output:

```python
{1,2,3,4,5}
```

<span style="color: blue">update()</span> - to add multiple new elements to a set at once. New elements can be passed as a set or list

```python
int_set = {1,2,3,4}
int_set.update({5,6,7,8})
print(int_set)
```

Output:

```python
{1,2,3,4,5,6,7,8}
```
