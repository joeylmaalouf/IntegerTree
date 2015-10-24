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

  def nodes_at_depth(self, depth, current_level = 1):
    """ Recurse down the tree until we reach the desired depth,
    yielding all of the nodes at the specified level. """
    if current_level == depth:
      yield self.value
    if self.left and self.right and current_level < depth:
      for node in self.left.nodes_at_depth(depth, current_level + 1):
        yield node
      for node in self.right.nodes_at_depth(depth, current_level + 1):
        yield node


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


def make_tree(depth, current_level = 1, tree = None):
  """ Given a tree depth, recursively create an actual
  tree that follows the problem requirements. """
  # make the root if none is found
  if not tree:
    tree = Node(1)

  # if we haven't hit the limit, recurse
  # through the children until we do
  if current_level != depth:
    tree.make_children()
    make_tree(depth, current_level + 1, tree.left)
    make_tree(depth, current_level + 1, tree.right)

  return tree


def display_tree(tree, depth):
  """ Given the tree structure, display it with proper formatting. """
  for counter in range(depth):
    # calculate the proper width values for each segment based on the level
    occurrences = 2 ** counter
    starting_spaces = 2 ** (depth - counter - 1) if counter < depth - 1 else 0
    underscores = max(0, starting_spaces - 2)
    node_spaces = starting_spaces * 2 + 3
    out_slash_spaces = starting_spaces * 2 + 1
    in_slash_spaces = underscores * 2 + 1
    # display the current line of values, with spaces and underscores repeated for formatting
    # also include the slashes unless we're at the bottom-most level
    print(" " * starting_spaces + "{0}*{0}{1}".format("_" * underscores, " " * node_spaces) * occurrences)
    if counter < depth - 1:
      print(" " * (starting_spaces - 1) + "/{}\\{}".format(" " * in_slash_spaces, " " * out_slash_spaces) * occurrences)


if __name__ == "__main__":
  depth = validate(sys.argv)
  tree = make_tree(depth)
  for i in range(depth):
    print(list(tree.nodes_at_depth(i + 1)))
  display_tree(tree, depth)
