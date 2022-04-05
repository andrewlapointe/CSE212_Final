'''
Read all comments and complete the program.

This is a binary search tree. The tree is ordered numerically. 
The larger number goes on the right child. Smaller on the left.

Your task is to implement a search function to determine if a value is 
present in the tree (boolean).

'''


class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None # pointer to parent Node in tree

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None: # checks to see if there is a root
            self.root = Node(value)
        else:
            self._insert(value, self.root) # runs the private function which adds the new Node. 

    def _insert(self, value, current): 
    # this is a recursive function. It will run on each Node starting from the root until it finds a place to insert the new Node
        if value < current.value:
            if current.left_child == None:
                current.left_child = Node(value)
                current.left_child.parent = current # set parent
            else:
                self._insert(value,current.left_child)
        elif value > current.value:
            if current.right_child == None:
                current.right_child = Node(value)
                current.right_child.parent = current # set parent
            else:
                self._insert(value, current.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self): # prints the tree from top to bottom, left to right
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, current):
        if current != None:
            self._print_tree(current.left_child)
            print(str(current.value))
            self._print_tree(current.right_child)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current):
        # This is where you come in. Write a recursive function which checks each Node and compares its value
        # to the value being inserted. This function can be modled after existing ones in this program.
        # If the value is found, return True, else False.
        if value == current.value:
            return True
        elif value < current.value and current.left_child != None:
            return self._search(value, current.left_child)
        elif value > current.value and current.right_child != None:
            return self._search(value, current.right_child)
        return False 

    def fill_tree_random(self, num_ints = 30, max_int = 500):
        import random
        for i in range(num_ints):    
            self.insert(random.randint(0, max_int))
            i += 1

def test_function(tree_object, search_value = 35):
    import random
    for i in range(1, random.randint(2,20)):
        tree_object.insert(random.randint(0,100))
    tree_object.insert(search_value)
    for i in range(1, random.randint(2,20)):
        tree_object.insert(random.randint(0,100))
    

root = binary_search_tree()
test_function(root)
print(root.print_tree())
print(root.search(35)) # should evaluate to True
print(root.search(10000)) # should evaluate to False