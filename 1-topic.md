<!-- 1. What is a data structure?

2. What is "Big O"?

1. What is it?

3. How efficient is it?

4. How would the data structure be used in Python -->

# Stack

## What is a Stack?

A stack is on of the easiest data structures to understand because it is used in the physical world all of the time.

Imagine you have a "stack" of pancakes. Whenever you have a hot pancake off the griddle you add it to the top of the pile. This is called a "push()". When someone is hungry they take a pancake from the top. This is a "pop()".

![stack diagram](images\stackdiagram.jfif)

Much like the pancakes, the oldest piece of data remains at the bottom. In data structures this is a principle known as Last On/First Off (LO/FO).

## Big O

### What is "Big O" Notation?

O notation is is a measure of the efficiency of a system. The higher the degree of O the less efficient. For example O(n<sup>2</sup>) is better than O(n<sup>3</sup>), but worse than O(n).

If a program has a O(n) that means that the number of operations it preforms will increase linearly as the size of the data increases and O(n<sup>2</sup>) will increase exponentially, etc.

### What is the Big O of Stack operations?

All operations on stacks (push and pop) have a O(1) also known as constant time. This is the fastest that any function can be. This makes the stack a great choice for quick operations.

## Stacks in Python

A stack can be created using a python list.

```python
list = []
```

The built in pop() and append() work well to add

Consider the following code.

```python
list = []
list.append(3)
list.append(4)
list.pop()
list.append(2)
print(list)
```

The output would be:

```python
[3,2]
```

-[Link Back to Welcome](0-welcome.md)
