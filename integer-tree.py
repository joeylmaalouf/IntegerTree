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

  def depth(self):
    """ Recurse down the tree until we reach a leaf. """
    depth = 0
    node = self
    while node:
      depth += 1
      node = node.left
    return depth

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
    yielding all of the nodes at the specified level. """
    if current_level >= depth:
      yield self
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
    depth = int(argv[1])
    if depth <= 0:
      print("Error: Tree depth must be positive.")
      sys.exit(1)
    return depth
  except ValueError:
    print("Error: Tree depth must be a valid integer.")
    sys.exit(1)


def initialize_tree(depth, current_level = 1, tree = None):
  """ Given a tree depth, recursively create
  an actual tree of the desired size. """
  # make the root if none is found
  if not tree:
    tree = Node(1)

  # if we haven't hit the limit, recurse
  # through the children until we do
  if current_level != depth:
    # we can't just create the children here because
    # their values depend on those of their parents' siblings,
    # who may or may not yet be created (since this is pre-order)
    tree.left = Node(1, tree, "left")
    tree.right = Node(1, tree, "right")
    initialize_tree(depth, current_level + 1, tree.left)
    initialize_tree(depth, current_level + 1, tree.right)
  return tree


def populate_tree(tree):
  """ Given our tree structure, iterate through the
  levels of the tree and make the children as we go. """
  for d in range(1, tree.depth()):
    # we can create the children here because this is level-order,
    # so all of the parents and siblings are already created
    for n in tree.nodes_at_depth(d):
      n.make_children()


def display_tree(tree):
  """ Given the tree structure, display it with proper formatting. """
  depth = tree.depth()
  for counter in range(depth):
    # get all of the values that will be printed
    level_values = [n.value for n in tree.nodes_at_depth(counter + 1)]
    # calculate the proper width values for each segment based on the level
    starting_spaces = 2 ** (depth - counter - 1) if counter < depth - 1 else 0
    underscores = max(0, starting_spaces - 2)
    node_spaces = starting_spaces * 2 + (3 if counter < depth - 2 else 1)
    out_slash_spaces = starting_spaces * 2 + 1
    in_slash_spaces = underscores * 2 + 1
    # display the current level of values, with spaces and underscores repeated for formatting
    # also include the slashes unless we're at the bottom-most level
    nodestring = " " * (starting_spaces + (1 if counter < depth - 2 else 0))
    for value in level_values:
      nodestring += "{0}{2:03d}{0}{1}".format("_" * (underscores - 1), " " * node_spaces, value)
    print(nodestring)
    if counter < depth - 1:
      print(" " * starting_spaces + "/{}\\{}".format(" " * in_slash_spaces, " " * out_slash_spaces) * len(level_values))


if __name__ == "__main__":
  depth = validate(sys.argv)
  tree = initialize_tree(depth)
  populate_tree(tree)
  display_tree(tree)
