# integer-tree

##### NeuroScouting Dev Technical Problem #1

### Overview
At the very start, the `validate()` function takes in the command-line arguments and makes two checks. The first one ensures that a tree depth is provided, and the second one makes sure it is a valid value. Once validation is complete, `initialize_tree()` creates an empty tree (comprised of `Node()`s) of our desired depth by recursively traversing it in pre-order and making filler nodes, filled with ones. After we have the tree structure, `populate_tree()` traverses it in level-order and calculates all of the node values. Finally, `display_tree()` reads the data in the tree and formats it nicely to then print it.

### Organization
There are no external dependencies; the only imported module is Python's built-in `sys`, for reading the depth value from the command-line.
The `Node()` class can be instantiated with just a single node value, but can optionally also take a parent node and a left/right position, and comes with methods for: finding the tree depth from that node (`.depth()`), finding the node's siblings (`.get_siblings()`), populating the node's children (`.make_children()`), and returning all of the nodes at a given depth (`.nodes_at_depth()`).

### Control Flow
The main function always starts with the validation check, then the tree initialization recurses through itself until it reaches the given depth. We then iterate over each tree level to populate the next one based on each node's siblings. Finally, the display function iterates over each level to format the values based on the size of the tree.

### Example Usage
```
$ python integer-tree.py 5
                 _____________001_____________
                /                             \
         _____001_____                   _____001_____
        /             \                 /             \
     _001_           _002_           _002_           _001_
    /     \         /     \         /     \         /     \
  001     003     003     004     004     003     003     001
  / \     / \     / \     / \     / \     / \     / \     / \
001 004 004 006 006 007 007 008 008 007 007 006 006 004 004 001
```
