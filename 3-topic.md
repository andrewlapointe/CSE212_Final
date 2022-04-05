# Tree

## What is a Tree?

So far all of the data structures we have been looking at were linear data structures. A tree is a non-linear structure used to represent hierarchical data.

An example of hierarchical data commonly arranged in a tree is the family tree.

![tree diagram](images/structure-of-tree.jpeg)

As seen above the tree is made of nodes. A parent is a node which has a descendent, or child. The root is the origin, or top of the structure, and leaves are childless nodes.

<!-- ## What is the Big O of Tree operations? -->

## Trees in Python

### Creating a Tree ----

To create a tree in python we will first need a Node class. For this example we will be creating a binary tree, which means that each parent can have at most two children.

<span style="color: green">#Creating the Node class</span>

```python
class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
```

<span style="color: green">#Creating the Root with a value of 10</span>

```python
root = Node(10)
```

<span style="color: green">#Creating the Root's children</span>

```python
root.left = Node(12)
root.right = Node(3)
print(root.data, root.left.data, root.right.data)
```

Output:

```python
10,12,3
```

This is the most basic implementation of the tree. In real code there would be a class created to handle insertions, deletions, etc. The Node class, however, remains the same.

### Tree Functions ----

Tree functions are great for their efficiency. A search function can be as fast as O(log n).

This is done through recursion.

-[Example Problem](python/tree_problem.py)

-[Example Problem Solution](python/tree_problem_solution.py)

-[Link Back to Welcome](0-welcome.md)
