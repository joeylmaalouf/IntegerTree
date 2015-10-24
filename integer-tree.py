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

  def get_siblings(self):
    """ Find the siblings to the node, where siblings are defined as adjacent
    entries on the same level, regardless of sharing a parent node. """
    siblings = { "left": None, "right": None }
    parent_siblings = self.parent.get_siblings() if self.parent else { "left": None, "right": None }
    if self.pos == "left":
      siblings["right"] = self.parent.right
      siblings["left"] = parent_siblings["left"].right if self.parent.parent and parent_siblings["left"] else None
    elif self.pos == "right":
      siblings["left"] = self.parent.left
      siblings["right"] = parent_siblings["right"].left if self.parent.parent and parent_siblings["right"] else None
    return siblings

  def make_children(self):
    """ Using the node's position under its parent,
    calculate its left and right child values. """
    siblings = self.get_siblings()
    lval = (self.value + siblings["left"].value) if siblings["left"] else self.value
    rval = (self.value + siblings["right"].value) if siblings["right"] else self.value
    self.left = Node(lval, self, "left")
    self.right = Node(rval, self, "right")

  def nodes_at_depth(self, depth, current_level = 1):
    """ Recurse down the tree until we reach the desired depth,
    yielding all of the node values at the specified level. """
    if current_level == depth:
      yield self.value
    if self.left and self.right and current_level < depth:
      for nodeval in self.left.nodes_at_depth(depth, current_level + 1):
        yield nodeval
      for nodeval in self.right.nodes_at_depth(depth, current_level + 1):
        yield nodeval


def validate(argv):
  """ Given the argument values, make sure that we have
  a tree depth, and that it's a valid integer. """
  # if no depth is provided, show the user how to do so
  if len(argv) < 2:
    print("Usage: {} <depth>".format(argv[0]))
    sys.exit(1)

  # if the depth isn't a valid int, error out
  try:
    depth = int(argv[1])
    if depth <= 0:
      print("Error: Tree depth must be positive.")
      sys.exit(1)
    return depth
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
    # get all of the values that will be printed
    level_values = list(tree.nodes_at_depth(counter + 1))
    # calculate the proper width values for each segment based on the level
    starting_spaces = 2 ** (depth - counter - 1) if counter < depth - 1 else 0
    underscores = max(0, starting_spaces - 2)
    node_spaces = starting_spaces * 2 + 3
    out_slash_spaces = starting_spaces * 2 + 1
    in_slash_spaces = underscores * 2 + 1
    # display the current level of values, with spaces and underscores repeated for formatting
    # also include the slashes unless we're at the bottom-most level
    nodestring = " " * starting_spaces
    for value in level_values:
      nodestring += "{0}{2}{0}{1}".format("_" * underscores, " " * node_spaces, value)
    print(nodestring)
    if counter < depth - 1:
      print(" " * (starting_spaces - 1) + "/{}\\{}".format(" " * in_slash_spaces, " " * out_slash_spaces) * len(level_values))


if __name__ == "__main__":
  depth = validate(sys.argv)
  tree = make_tree(depth)
  display_tree(tree, depth)
