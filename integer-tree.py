import sys


class Node(object):
  """ A single node in the integer tree. """
  def __init__(self, value, parent = None, pos = None):
    super(Node, self).__init__()
    self.value = value
    self.parent = parent
    self.pos = pos
    self.left = None
    self.right = None

  def __str__(self):
    """ String representation of the node. """
    return str(self.value)

  def make_children(self):
    """ Using the node's position under its parent,
    calculate its left and right child values. """
    lval = self.value + self.parent.left.value if self.pos == "right" else self.value
    rval = self.value + self.parent.right.value if self.pos == "left" else self.value
    self.left = Node(lval, self, "left")
    self.right = Node(rval, self, "right")
    return self


def validate(argv):
  """ Given the argument values, make sure that we have
  a tree depth, and that it's a valid integer. """
  # if no depth is provided, show the user how to do so
  if len(argv) < 2:
    print("Usage: {} <depth>".format(argv[0]))
    sys.exit(1)

  # if the depth isn't a valid int, error out
  try:
    return int(argv[1])
  except ValueError:
    print("Error: Tree depth must be a valid integer.")
    sys.exit(1)


def make_tree(depth, current = 0):
  """ Given a tree depth, create an actual tree
  that follows the problem requirements. """
  if current == depth:
    n = Node(1).make_children() # example usage
    return n
  else:
    return make_tree(depth, current + 1)


def display_tree(tree):
  """ Given the tree structure, display it with proper formatting. """
  print(" {}\n{} {}".format(tree, tree.left, tree.right))


if __name__ == "__main__":
  depth = validate(sys.argv)
  tree = make_tree(depth)
  display_tree(tree)